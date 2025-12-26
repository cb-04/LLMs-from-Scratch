import re

class SimpleTokenizer:
    def __init__(self,vocab):
        '''
        self.str_to_int: User-defined mapping from token to token id
        self.int_to_str: User-defined mapping from token id to token
        '''
        self.str_to_int = vocab
        self.int_to_str = {integer:item for item,integer in vocab.items()}

    def encode(self,text):
        '''
        preprocessed: List of tokens taken from "text" split wherever the mentioned punctuations appear and stripped of white spaces
        ids: List of token ids
        '''
        preprocessed = re.split(r'([,.:;?_!"()\]]|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int
            else "<|unk|>" for item in preprocessed
        ]
        ids = [self.str_to_int[item] for item in preprocessed] 
        return ids
    
    def decode(self,ids):
        '''
        text: Text obtained after joining all the tokens at index values "ids" in order with an addition of a white space between each token and replaced by the aforementioned punctuations
        '''
        text = " ".join([self.int_to_str[id] for id in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text