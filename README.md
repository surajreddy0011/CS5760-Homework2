# CS5760 Natural Language Processing – Homework 2
**University of Central Missouri – Fall 2026**

**Student Name:** Suraj Sirikonda
**Student ID:** 700779845

## Files
| File | Description |
|---|---|
| `Homework_2_answers.docx` | Part I written answers (Q1–Q5) |
| `q5_metrics.py` | Part I Q5: precision, recall, macro and micro averages from the confusion matrix |
| `bigram_lm.py` | Part II Q1: bigram language model using MLE |

## How to run
```
python q5_metrics.py
python bigram_lm.py
```
No extra libraries needed (only Python 3).

## q5_metrics.py
- Takes the 3x3 confusion matrix (rows = system, columns = gold).
- Precision = TP / row total, Recall = TP / column total.
- Macro = average of the per-class scores; Micro = total TP / total items.
- Result: Macro P/R = 0.365, Micro P/R = 0.389.

## bigram_lm.py
- Reads the 3-sentence training corpus.
- Counts unigrams and bigrams.
- Uses MLE: P(w2|w1) = C(w1 w2) / C(w1).
- `sentence_prob()` multiplies the bigram probabilities of a sentence.
- Result: P(S1) = 0.333, P(S2) = 0.167 → the model prefers S1 because it has fewer bigrams and they are more likely.
