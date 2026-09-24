# Part II Q1: Bigram language model with MLE
from collections import Counter

# 1. training corpus
corpus = ["<s> I love NLP </s>",
          "<s> I love deep learning </s>",
          "<s> deep learning is fun </s>"]

# 2. unigram and bigram counts
unigrams, bigrams = Counter(), Counter()
for sent in corpus:
    words = sent.split()
    unigrams.update(words)
    bigrams.update(zip(words, words[1:]))

print("Unigram counts:", dict(unigrams))
print("Bigram counts:", dict(bigrams))

# 3. MLE bigram probability: P(w2|w1) = C(w1 w2) / C(w1)
def bigram_prob(w1, w2):
    if unigrams[w1] == 0:
        return 0.0
    return bigrams[(w1, w2)] / unigrams[w1]

# 4. probability of a sentence = product of its bigram probabilities
def sentence_prob(sentence):
    words = sentence.split()
    prob = 1.0
    for w1, w2 in zip(words, words[1:]):
        prob *= bigram_prob(w1, w2)
    return prob

# 5. test on both sentences
s1 = "<s> I love NLP </s>"
s2 = "<s> I love deep learning </s>"
p1, p2 = sentence_prob(s1), sentence_prob(s2)
print(f"P(S1) = {p1:.4f}")
print(f"P(S2) = {p2:.4f}")

# 6. which one the model prefers
if p1 > p2:
    print("Model prefers S1 because it has a higher probability "
          "(fewer bigrams and each one is more likely).")
else:
    print("Model prefers S2 because it has a higher probability.")
