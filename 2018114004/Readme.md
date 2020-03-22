## Aim

To build a language model that uses Witten bell and Kneyser Ney smoothing depending upon the input provided by the user


---------------------------


## Language Model Generation

- First a corpus is provided

- This corpus is then preprocessed for removal of too many spaces, blank lines brackets, assigning meaning to punctuations like "!" , ";", "?" etc.
- Now the nltk tokenizer is used to tokenize the given text before performing any smoothing
- These tokens are then arranges into unigram, bigram, trigram and n-gram 
- Now the input sentence is fed into the model and the probability is calculated

-----------------------------

## Differences in the smoothing model

We used Kneyser Ney smoothing as it uses the concept of absolute discounting interpolation and for lower order n-grams, it adds more weight to the overall
probability when the count for the higher-order n-gram is zero.and the weight decreases when there is a higher order n-gram present.

When witten bell smoothing is applied, it is seen that witten bell has better results when we test on lower order n-gram. 

As we increase the order the result of kneyser ney increases.

***************************************************
