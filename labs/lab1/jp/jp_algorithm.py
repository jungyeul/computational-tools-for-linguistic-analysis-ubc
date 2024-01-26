import argparse
import io
import sys
class UDError(Exception):
    pass

def _decode(text):
    return text if sys.version_info[0] >= 3 or not isinstance(text, str) else text.decode("utf-8")

def _encode(text):
    return text if sys.version_info[0] >= 3 or not isinstance(text, unicode) else text.encode("utf-8")

def load_txt(file):
    # Internal representation classes
    class UDRepresentation:
        def __init__(self):
            # Characters of all the tokens in the whole file.
            # Whitespace between tokens is not included.
            self.characters = []
            # List of UDSpan instances with start&end indices into `characters`.
            self.tokens = []
            # List of UDSpan instances with start&end indices into `characters`.
            self.sentences = []
    class UDSpan:
        def __init__(self, start, end):
            self.start = start
            # Note that self.end marks the first position **after the end** of span,
            # so we can use characters[start:end] or range(start, end).
            self.end = end

    ud = UDRepresentation()
    index, sentence_start = 0, None
    while True:
        line = file.readline()
        if not line:
            break
        line = _decode(line.rstrip("\r\n"))
        
        ud.sentences.append(UDSpan(index, 0))
        
        for token in line.split(" "):
            # Save token
            ud.characters.extend(token)
            ud.tokens.append(UDSpan(index, index + len(token)))
            index += len(token)
        
        # End of sentence
        ud.sentences[-1].end = index
    
    return ud

def evaluate(gold_ud, system_ud):
    class Score:
        def __init__(self, gold_total, system_total, correct, aligned_total=None):
            self.correct = correct
            self.gold_total = gold_total
            self.system_total = system_total
            self.aligned_total = aligned_total
            self.precision = correct / system_total if system_total else 0.0
            self.recall = correct / gold_total if gold_total else 0.0
            self.f1 = 2 * correct / (system_total + gold_total) if system_total + gold_total else 0.0
            self.aligned_accuracy = correct / aligned_total if aligned_total else aligned_total
    
    class AlignmentSpan:
        def __init__(self, start, end):
            self.start = start
            # Note that self.end marks the first position **after the end** of span,
            # so we can use characters[start:end] or range(start, end).
            self.end = end
            self.align_count = 1
    
    def sentence_score(gold_sentences, system_sentences):
        correct, gi, si = 0, 0, 0
        gold_align, system_align = 0, 0
        while gi < len(gold_sentences) and si < len(system_sentences):
            if isinstance(gold_sentences[gi], AlignmentSpan) and isinstance(system_sentences[si], AlignmentSpan):
                gold_align += gold_sentences[gi].align_count - 1 
                system_align += system_sentences[si].align_count - 1
            else:
                correct += 1
            gi += 1
            si += 1
            
        return Score(len(gold_sentences) + gold_align, len(system_sentences) + system_align, correct)
    
    def align_tokens(sent_gold_tokens, sent_system_tokens):
        i = 0 # gold
        j = 0 # sys
        max_index = max(len(sent_gold_tokens), len(sent_system_tokens))
        ret_gold_tokens = []
        ret_system_tokens = []
        for x in range(0, max_index):
            if sent_gold_tokens[i].start == sent_system_tokens[j].start and \
                sent_gold_tokens[i].end == sent_system_tokens[j].end:
                ret_gold_tokens.append(sent_gold_tokens[i])
                ret_system_tokens.append(sent_system_tokens[j])
            else:
                ret_gold_tokens.append(AlignmentSpan(sent_gold_tokens[i].start, sent_gold_tokens[i].end))
                ret_system_tokens.append(AlignmentSpan(sent_system_tokens[j].start, sent_system_tokens[j].end))
                
                def loop(gi, si):
                    # Check if the next sentence has the same start
                    if sent_gold_tokens[gi].end == sent_system_tokens[si].end:
                        
                        # Check if the next sentence has the same end
                        if si + 1 < len(sent_system_tokens) and gi + 1 < len(sent_gold_tokens):
                            if sent_gold_tokens[gi + 1].end == sent_system_tokens[si + 1].end:
                                return False
                        
                        # Check if the current sentence is the last one
                        elif si == len(sent_system_tokens) - 1 and gi == len(sent_gold_tokens) - 1:
                            return False
                    
                    # Keep going
                    return True
                
                while loop(i, j):
                    if ret_gold_tokens[-1].end > ret_system_tokens[-1].end:
                        j += 1
                        ret_system_tokens[-1].end = sent_system_tokens[j].end
                        ret_system_tokens[-1].align_count += 1
                    else:
                        i += 1
                        ret_gold_tokens[-1].end = sent_gold_tokens[i].end
                        ret_gold_tokens[-1].align_count += 1
                    
                    if i >= len(sent_gold_tokens) or j >= len(sent_system_tokens):
                        break
            
            i += 1
            j += 1
            if i >= len(sent_gold_tokens) or j >= len(sent_system_tokens):
                break
        return ret_gold_tokens, ret_system_tokens
    
    def jp_align(gold_ud, system_ud):
        gold_tokens, system_tokens, gold_sentences, system_sentences = \
            gold_ud.tokens, system_ud.tokens, gold_ud.sentences, system_ud.sentences
        gi, si = 0, 0
        gold_token_pointer, system_token_pointer = 0, 0
        Lpairs = []
        Rpairs = []
        Ltokens = []
        Rtokens = []
        max_sent_index = max(len(gold_sentences), len(system_sentences))
        
        def get_tokens_list(tokens, start, end, pointer):
            ret_list = []
            for i in range(pointer, len(tokens)):
                if tokens[i].start >= start and tokens[i].end <= end:
                    ret_list.append(tokens[i])
                    pointer += 1
                else:
                    break
            return ret_list, pointer
        
        for x in range(max_sent_index):
            assert gold_sentences[gi].start == system_sentences[si].start
            
            # $L_{i{\not\sqcup}}$ == $R_{j\not\sqcup}$
            if gold_sentences[gi].end == system_sentences[si].end:
                Lpairs.append(gold_sentences[gi])
                Rpairs.append(system_sentences[si])
            else:
                Lpairs.append(AlignmentSpan(gold_sentences[gi].start, gold_sentences[gi].end))
                Rpairs.append(AlignmentSpan(system_sentences[si].start, system_sentences[si].end))
                
                # Rpair and Lpair should not be empty here
                assert Rpairs and Lpairs
                
                def loop(gi, si):
                    # Check if the next sentence has the same start
                    if gold_sentences[gi].end == system_sentences[si].end:
                        
                        # Check if the next sentence has the same end
                        if si + 1 < len(system_sentences) and gi + 1 < len(gold_sentences):
                            if gold_sentences[gi + 1].end == system_sentences[si + 1].end:
                                return False
                        
                        # Check if the current sentence is the last one
                        elif si == len(system_sentences) - 1 and gi == len(gold_sentences) - 1:
                            return False
                    
                    # Keep going
                    return True
                
                while loop(gi, si):
                    if Lpairs[-1].end > Rpairs[-1].end:
                        si += 1
                        Rpairs[-1].end = system_sentences[si].end
                        Rpairs[-1].align_count += 1
                    else:
                        gi += 1
                        Lpairs[-1].end = gold_sentences[gi].end
                        Lpairs[-1].align_count += 1
                    
                    if gi >= len(gold_sentences) or si >= len(system_sentences):
                        break
            
            sent_gold_tokens, gold_token_pointer = \
                get_tokens_list(gold_tokens, Lpairs[-1].start, Lpairs[-1].end, gold_token_pointer)
            sent_system_tokens, system_token_pointer = \
                get_tokens_list(system_tokens, Rpairs[-1].start, Rpairs[-1].end, system_token_pointer)
            
            sent_gold_tokens, sent_system_tokens = align_tokens(sent_gold_tokens, sent_system_tokens)
                
            assert sent_gold_tokens[0].start == sent_system_tokens[0].start
            assert sent_gold_tokens[-1].end == sent_system_tokens[-1].end
            Ltokens.extend(sent_gold_tokens)
            Rtokens.extend(sent_system_tokens)
            
            gi += 1
            si += 1
            
            if gi >= len(gold_sentences) or si >= len(system_sentences):
                break
        return Ltokens, Rtokens, Lpairs, Rpairs

    # Check that the underlying character sequences do match.
    if gold_ud.characters != system_ud.characters:
        index = 0
        while index < len(gold_ud.characters) and index < len(system_ud.characters) and \
                gold_ud.characters[index] == system_ud.characters[index]:
            index += 1

        raise UDError(
            "The concatenation of tokens in gold file and in system file differ!\n" +
            "First 20 differing characters in gold file: '{}' and system file: '{}'".format(
                "".join(map(_encode, gold_ud.characters[index:index + 20])),
                "".join(map(_encode, system_ud.characters[index:index + 20]))
            )
        )
    
    gold_ud.tokens, system_ud.tokens, gold_ud.sentences, system_ud.sentences = jp_align(gold_ud, system_ud)
    return {
        "Sentences": sentence_score(gold_ud.sentences, system_ud.sentences),
        "Tokens": sentence_score(gold_ud.tokens, system_ud.tokens)}

def load_txt_file(path):
    _file = open(path, mode="r", **({"encoding": "utf-8"} if sys.version_info >= (3, 0) else {}))
    return load_txt(_file)