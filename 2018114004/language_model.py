import nltk
import re
from collections import Counter
import sys 
import random

ngrams_c = {}
ngram = []
unigram = []
bigram = []
trigram = []

def find_val(gram):
    if len(gram) == 0:
        return sum(ngrams_c[1].values())
    if gram in ngrams_c[len(gram)].keys():
        return ngrams_c[len(gram)][gram] 
    else:
        return 0

def witten2(gram):
    unique = 0
    for c in ngrams_c[len(gram)+1].keys():
        if(c[:-1] == gram):
            
            unique += 1
    k = float(unique + int(find_val(gram)))
    if(k != 0):
        return (unique / k)
    else:
        return random.uniform(0.00001,0.0001)

def witten(gram):
    x = len(gram)
    if x == 1:
        return find_val(gram) / sum(ngrams_c[1].values())
    if(find_val(gram[:-1]) != 0):
        return ((1 - witten2(gram[:-1])) * (find_val(gram) / find_val(gram[:-1]))) + (witten2(gram[:-1]) * witten(gram[:-1]))
    else:
        return random.uniform(0.00001, 0.0001) +  (witten2(gram[:-1]) * witten(gram[:-1]))
    
def kneser(gram, maxi):
    x = len(gram)
    d = 0.75
    if find_val(gram[:-1]) == 0:
        lamda = random.uniform(0,1)
        term = random.uniform(0.00001,0.0001)
    else:
        if x == maxi:
            term = max(0,find_val(gram)-d)/find_val(gram[:-1])
        else:
            term = max(0,(sum(token[1:] == gram for token in ngrams_c[len(gram) + 1].keys()) - d)) / find_val(gram[:-1])
        lamda = d * sum(token[:-1] == gram[:-1] for token in ngrams_c[len(gram)].keys()) / find_val(gram[:-1])
    if x == 1:
       return term
    else:
        return term + lamda * kneser(gram[:-1], maxi)
    
    

def preprocessing(lines):
    for text in lines:
        text = text.lower()
    
        text = text.replace(')', '')
        text = text.replace('--', ' ')
        text = text.replace(';', ' .')
        text = text.replace('!', ' .\n')
        text = text.replace('?', ' ?\n')
        text = text.replace(',', '')  
        text = text.replace(',\n', '.\n')       
        text = re.sub(r'(?m)^\}.*\n?', '', text)
        text = re.sub('[*]','', text)
        text = re.sub('\n+','\n',text)
    return lines

if __name__ == '__main__':
    n = int(sys.argv[1])
    t = sys.argv[2]
    f=open(sys.argv[3], "r")
    
    print("Preprocessing")
    
    text = f.readlines()
    text = preprocessing(text)    
    

    for x in text:
        words = nltk.word_tokenize(x)
        # print(len(words))
        
        for w in range(0,len(words)):
            unigram.append(tuple(words[w]))
              
    ngrams_c[1] = Counter(unigram) 

    for x in text:
        words = nltk.word_tokenize(x)

        for w in range(0,len(words)-1):
            bigram.append(tuple(words[w:w+2]))
           
    ngrams_c[2] = Counter(bigram)

    for x in text:
        words = nltk.word_tokenize(x)
        for w in range(0,len(words)-2):
            trigram.append(tuple(words[w:w+3]))

    ngrams_c[3] = Counter(trigram)        
    for x in text:
        words = nltk.word_tokenize(x)
        for w in range(0,len(words)-n+1):
            ngram.append(tuple(words[w:w+n]))
        
            # trigram = 
   
    ngrams_c[4] = Counter(ngram)             
    # print(ngrams_c[n])

    print("Preprocessing done")  

    inp = input("Input sentence: ")

    inp = preprocessing(inp)

    words = nltk.word_tokenize(inp)
    tex = []
    ngram_inp = []

    for x in range(0,len(words)-n+1):
        tex.append(tuple(words[x:x+n]))

    ngram_inp = Counter(tex)
    
    p = 1
    if t == 'k':
         for gram in ngram_inp:
            p *= kneser(gram, len(gram))    
    elif t == 'w':
        
        for gram in ngram_inp:
            p *= witten(gram)
        
    print(p)
   




























        
        # tex_uni.append(words[x])
        # # tex_uni = Counter(tex_uni)
        # tex_bi.append(words[x:x+2])
        # # tex_bi = Counter(tex_bi)
        # tex_tri.append(words[x:x+3])
        # # tex_tri = Counter(tex_tri)

    # ngram_inp.append(tuple(tex_uni))
    # ngram_inp.append(tuple(tex_bi))
    # ngram_inp.append(tuple(tex_tri))
    # ngram_inp.append(tuple(tex))