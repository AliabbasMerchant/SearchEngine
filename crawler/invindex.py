from pprint import pprint as pp
from crawler.stopword import token
import spacy
from itertools import chain


class InvertedIndex():
    def __init__(self,filepath):
        self.Counter = 0
        self.file=filepath
        self.dict1={}

     #function to count lines in a file
    def count(self):
        with open(self.file,'r') as f:
           # Reading from file
            Content = f.read()
            self.CoList = Content.split("\n")
            for i in self.CoList:
                if i:
                    self.Counter += 1
        return self.Counter

    def Index(self):
        with open(self.file,'r') as f:
            self.url=f.readline()
        #making dictionary of {Url:tokens} format

            for j in range(self.count()):

                self.dict1.update(token(self.CoList[j]).tokenizer())
                print(f"------------------updating dict-{j}------------------------------")
        
                self.url = f.readline()
        
        tkns=list(val for key,val in self.dict1.items())
        flattened = [val for sublist in tkns for val in sublist]
        invindex = {word:set(txt for txt, wrds in self.dict1.items() if word in wrds) for word in flattened}
        print('\nInverted Index')
        self.Inverted_Index={k: sorted(v) for k, v in invindex.items()}
        pp(self.Inverted_Index,width=300,compact=True)

    def synonyms(self):
        data=" ".join(str(i) for i in chain(list(self.Inverted_Index.keys())))

        nlp = spacy.load("en_core_web_lg")
        tokens = nlp(data)
       # for token in self.tokens:
            #print(token.text, token.has_vector, token.vector_norm, token.is_oov)

        for token1 in tokens:
            for token2 in tokens:
                if ((token2.vector_norm) and (token1.vector_norm)) :
                    if(token1.similarity(token2) > 0.65):
                        print(token1.text, token2.text, token1.similarity(token2))




Invert=InvertedIndex("crawled_file")
Invert.Index()
