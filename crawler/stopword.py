import spacy
from bs4 import BeautifulSoup
import requests


class token:
    def __init__(self,links):
        self.link=links

    def textgen(self,link):
        self.access=requests.get(self.link)
        self.getcontent=self.access.content
        self.soup=BeautifulSoup(self.getcontent,'html.parser')
        for script in self.soup(["script","style"]):
           script.extract()
        self.textt=self.soup.get_text()

        return self.textt

    def tokenizer(self,link):
        self.nlp=spacy.load('en_core_web_sm')
        self.doc=self.nlp(self.textgen(self.link))
        self.cha="=,<,>,@,#,$,%,^,&,*,_,-,+,~,`,|,\,/"
        self.setotoken=set()
        for self.token in self.doc:
            if  self.token.is_stop==False and self.token.is_space==False and self.token.is_alpha and self.token.is_punct==False and self.token.like_url==False and self.token.like_num==False and self.token.text not in self.cha and len(self.token.orth_)!=1:
                self.lem=self.token.lemma_
                self.setotoken.add(self.lem)
        print(self.setotoken)


token("https://www.geeksforgeeks.org/").tokenizer("https://www.geeksforgeeks.org/")
