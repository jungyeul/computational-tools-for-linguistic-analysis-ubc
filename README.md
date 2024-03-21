# LING 242 Computational Tools for Linguistic Analysis 
### @UBC (Winter Term 2 2023/24)

![](https://raw.githubusercontent.com/jungyeul/computational-tools-for-linguistic-analysis-ubc/main/labs/LING242.png)


## schedule
| date |	description	 |course materials |
| ------------ | ------------ | ------------  |
| 2024 |  | [[syllabus](https://www.overleaf.com/read/twjqrgnvwzdq)] |
| Lecture 0 | *shell commands*  |  |
|  |   | [[Lecture 0 slides](https://www.overleaf.com/read/fqqrwxqkjmtb)], [[Lab 0 slides](https://www.overleaf.com/read/djddcbxmfqhj)], [[lab suppl - command lines in PC](https://docs.google.com/presentation/d/1KZxnS9p1-nAVYxKCkWT7EsyqbdiLRWvfjATUBZaAPcg/edit?usp=sharing) (Yadong)] |
|  |  |  [[Assignment 0](https://github.com/jungyeul/computational-tools-for-linguistic-analysis-ubc/blob/main/labs/lab0/lab0.ipynb) (Due 11:59PM on Jan 25)] [[Assignment 0 described](https://github.com/jungyeul/computational-tools-for-linguistic-analysis-ubc/blob/main/labs/lab0/lab0_description.ipynb) (Jasbrina)] |
| Lecture 1 | **preprocessing**  |  |
|   | *sentence boundary detection*   |   Suggested Readings:  <ul><li>[[Sentence Boundary Detection and the Problem with the U.S.](http://aclweb.org/anthology/N/N09/N09-2061.pdf)]</li><li>[[Sentence Boundary Detection: A Long Solved Problem?](http://aclweb.org/anthology/C/C12/C12-2096.pdf)]</li></ul> |
|  |  *tokenization*  |  Suggested Readings:  <ul><li>[[Tokenization: Returning to a Long Solved Problem](http://aclweb.org/anthology/P/P12/P12-2074.pdf)]</li></ul>  |
|  |   | [[Lecture 1 slides](https://www.overleaf.com/read/scpjfcgjvqyt)], [[Lab 1 slides](https://www.overleaf.com/read/nfnzdfpcvnqq)] [[JP-algorithm](./labs/lab1/jp/jp-algorithm-ling242.ipynb) (Junrui)]  |
|  |  |  [[Assignment 1](./labs/lab1/lab1.ipynb) (Due 11:59PM on Feb 8)] [[Assignment 1 described](./labs/lab1/lab1_description.ipynb) (Kiki)] |
|  |  |  [[Assignment 1 in the class](https://colab.research.google.com/drive/19gdnQ1K6O2aVYX3adWLfXZJ5_AO5jrPH?usp=sharing)] |
| Lecture 2  | **lm**  |  |
|   |   | Suggested Readings:  <ul><li>[[Chap. 3, N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)], [Speech and Language Processing (3rd ed. draft)](https://web.stanford.edu/~jurafsky/slp3/)</li></ul>  |
|  |   | [[Lecture 2 slides](https://www.overleaf.com/read/fwxbpssbqkkm)], [[Lab 2 slides](https://www.overleaf.com/read/zkqkxkvjdrrb)]  |
|  |  |  [[Assignment 2](./labs/lab2/lab2.ipynb) (Due 11:59PM on Feb 22)] [[Assignment 2 described](./labs/lab2/lab2_description.ipynb) (Marcell)] |
| Lecture 3 | **pos tagging & sequence labeling algorithms**  | |
|  | *morphosyntax tasks in nlp & hmm* |  Suggested Readings:  <ul><li>[[Chap. 8, Sequence Labeling for Parts of Speech and Named Entities](https://web.stanford.edu/~jurafsky/slp3/8.pdf)], Speech and Language Processing (3rd ed. draft)</li>  <li>[[Chunking](https://www.clips.uantwerpen.be/conll2000/chunking/)], CoNLL-2000 Shared Task</li> <li>[[Language-Independent Named Entity Recognition](https://www.clips.uantwerpen.be/conll2003/ner/)], CoNLL-2003 Shared Task</li><li>[[Semantic Role Labeling](http://www.lsi.upc.edu/~srlconll/)], CoNLL-2004 and CoNLL-2005 Shared Tasks</li> </ul>  |
|  |   | [[Lecture 3 slides](https://www.overleaf.com/read/hxwyvymgyxsy)], [[Lab 3 slides](https://www.overleaf.com/read/drrppbcnfdhy)] |
|  |   | [[Assignment 3](./labs/lab3/lab3.ipynb) (Due 11:59PM on March 7)] [[Assignment 3 described](./labs/lab3/lab3_description.ipynb) (Andrew)] |
| Lecture 4 | **syntax**  | |
|  | *parsing* |  Suggested Readings:  <ul><li>[Chap. 12, [Constituency Grammars](https://web.stanford.edu/~jurafsky/slp3/12.pdf)], Speech and Language Processing (3rd ed. draft)</li>   <li>[Chap. 13, [Constituency Parsing](https://web.stanford.edu/~jurafsky/slp3/13.pdf)]</li>   <li>[Chap. 14, [Dependency Parsing](https://web.stanford.edu/~jurafsky/slp3/14.pdf)]</li> </ul>  |
|  |   | [[Lecture 4 slides](https://www.overleaf.com/read/qbymzwsmjrxf)], [[Lab 4 slides](https://www.overleaf.com/read/vcxhmpjgnwzf)] |
||| [[ptb examples](./labs/lab4/ptb-examples.ipynb)] [[ptb ud examples](./labs/UD.pdf)] [[CNF conversion](./labs/lab4/ling242_syntax.ipynb)] |
||| [[Assignment 4](./labs/lab4/lab4.ipynb) (Due 11:59PM on March 21)] [[Assignment 4 described](./labs/lab4/lab4_description.ipynb) (Annabelle)]  |
| Lecture 5 | **classification**  | |
|  |  | [[Lecture 5 slides](https://www.overleaf.com/read/mmxnxpbkrgmh)], [[Lab 5 slides](https://www.overleaf.com/read/qtfbvxhdqvnv)] |
|  |   | [[Assignment 5](./labs/lab5/lab5.ipynb) (Due 11:59PM on April 4)] [[Assignment 5 described](./labs/lab5/lab5_description.ipynb) (Leah)]  |
| Lecture 6 | **morphology**  | |
|  | *morphological segmentation*  | Suggested Readings:  <ul><li>[[Empirical Methods for Compound Splitting](http://www.aclweb.org/anthology/E03-1076)]</li> <li>[[Morphological Segmentation Inside-Out](https://www.aclweb.org/anthology/D16-1256/)]</li><li>[[Unsupervised Discovery of Morphemes](http://aclweb.org/anthology/W02-0603)]</li></ul>  |
|  | *morphological paradigm* | Suggested Readings:  <ul><li>[[Supervised Learning of Complete Morphological Paradigms](https://www.aclweb.org/anthology/N13-1138)]</li></ul>  |
| |   | [[Lecture 6 slides](https://www.overleaf.com/read/dddsbnghbhwd)], [Lab 6 slides] |
||| [Assignment 6]  |
| Lecture 7 | **machine translation**  | |
|  | *document & word alignment*  |  |
|  | *smt & nmt* |  |
|   |   | [Lecture 7 slides] |
| Lecture 8 | **semantics**  | |
|   |   | [Lecture 8 slides] |





- [lecture] 9:30-10:45AM on Monday and Wednesday 
- [lab] 10-11:30AM Friday (Bring Your Own Laptop)


## office hours
* Jungyeul (Instructor): 6-7PM on Thursday (in-person [ORCH 4018], online [[zoom](https://ubc.zoom.us/j/4232149833?pwd=NDRpUFR4VjVWM2Qyd2sweGpNaFBadz09)]), (email: jungyeul _at_ mail.ubc.ca)

## reference materials
* _Speech and Language Processing_ (3rd ed. draft) [[link](https://web.stanford.edu/~jurafsky/slp3/)]
