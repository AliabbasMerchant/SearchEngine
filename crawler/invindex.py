from pprint import pprint as pp
from crawler.stopword import token
import spacy
from itertools import chain
import concurrent.futures


class InvertedIndex():
    def __init__(self,filepath):
        self.Counter = 0
        self.file=filepath
        self.dict1={}

     #function to count lines in a file
    def count(self):
        with open(self.file,'r') as f:
           # Reading from file
            self.Content = f.read()
            self.CoList = self.Content.split("\n")
            for i in self.CoList:
                if i:
                    self.Counter += 1
        return self.Counter

    def Index(self):
        with open(self.file,'r') as f:
            self.url=f.readline()
        #making dictionary of {Url:tokens} format
            for j in range(self.count()):

                self.dict2=token(self.CoList[j]).tokenizer()
                print(token(self.CoList[j]).tokenizer())
                self.dict1.update(self.dict2)
                print(f"updating dict{j}........................")

                self.url = f.readline()
        
        self.tkns=list(val for key,val in self.dict1.items())
        self.flattened = [val for sublist in self.tkns for val in sublist]
        self.invindex = {word:set(txt for txt, wrds in self.dict1.items() if word in wrds) for word in self.flattened}
        print('\nInverted Index')
        self.Inverted_Index={k: sorted(v) for k, v in self.invindex.items()}
        pp(self.Inverted_Index,width=300,compact=True)

    def synonyms(self):
        data=" ".join(str(i) for i in chain(list(self.Inverted_Index.keys())))

        self.nlp = spacy.load("en_core_web_lg")
        self.tokens = self.nlp(data)
       # for token in self.tokens:
            #print(token.text, token.has_vector, token.vector_norm, token.is_oov)

        for token1 in self.tokens:
            for token2 in self.tokens:
                if ((token2.vector_norm) and (token1.vector_norm)) :
                    if(token1.similarity(token2) > 0.65):
                        print(token1.text, token2.text, token1.similarity(token2))

if __name__ == '__main__':

    Invert=InvertedIndex("crawled_file")
    Invert.Index()
