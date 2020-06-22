import spacy
from bs4 import BeautifulSoup
import requests


class token:
    def __init__(self,links):
       self.link=links
       self.dict_of_tokens = dict()
#function to fetch  text from html
    def textgen(self):
        access=requests.get(self.link)
        getcontent=access.content

        soup=BeautifulSoup(getcontent,'html.parser')

        for script in soup(["script","style"]):
           script.extract()
        textt=soup.get_text()

        return textt

    def tokenizer(self):
        nlp=spacy.load('en_core_web_sm')
        doc=nlp(self.textgen())
        character="=,<,>,@,#,$,%,^,&,*,_,-,+,~,`,|,\,/"

        setotoken=set()
        for token in doc:
            if  token.is_stop==False and token.is_space==False and token.is_alpha and \
                    token.is_punct==False and token.like_url==False and \
                    token.like_num==False and token.text not in character and len(token.orth_)!=1:
                lem=token.lemma_
                setotoken.add(lem)
                list_of_tokens=list(setotoken)

                self.dict_of_tokens[self.link]= list_of_tokens

        return self.dict_of_tokens


if __name__ == '__main__':
   print(token("https://www.geeksforgeeks.org").tokenizer())
