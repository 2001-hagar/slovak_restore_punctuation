#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import modules
from transformers import pipeline
import pandas as pd
from nltk.tokenize import sent_tokenize
from termcolor import colored
import gradio as gr


# In[ ]:


#the function which restore,correct and heighlight punctuations in the text
def restore_punc(text):
    sents=sent_tokenize(text) #splitting the pragraph into sents
    new_text="" #for the text with correct punctuation
    labels=['.','!',',',':','?','-',";"] #the options of punctuations
    for sent in sents:
        sent = ''.join(ch for ch in sent if ch not in labels)#remove punctuation from the sent
        text_word=sent.split() #split the sent to words
        words=text_word[:] #create a copy of the list of the words 
        unmasker = pipeline('fill-mask', model='gerulata/slovakbert')#using slovakbert to predict the correct punctuation
        for i in range(1,len(text_word)+1):
            text_word.insert(i,'<mask>')#to put the mask after every word in the sent
            sent=" ".join(text_word)#collect the words to create the set again
            text_with_punc=unmasker(sent)#predict the correct punc after every word
            if text_with_punc[0]['token_str'] in labels:
                #save the heighlighted word with corect punc
                words[i-1]=colored(words[i-1]+text_with_punc[0]['token_str'], 'green', attrs=['reverse', 'blink'])
            text_word=words[:]#copy the words list to text_word list to put the mask at the right position in the next iteration
        new_text+= " ".join(words)#collect the words with the write punc to add every sent to collect the paragraph again
    print(f'original text:')
    print(f'{text}')
    print('---------------------------------------')
    print(f'modified text:')
    print(f'{new_text}')




    




# In[ ]:


restore_punc( )  #write here the text to restore its punctuation


# In[ ]:


#the function which restore,correct in the text
def restore_punc_with_interface(text):
    sents=sent_tokenize(text) #splitting the pragraph into sents
    new_text="" #for the text with correct punctuation
    labels=['.','!',',',':','?','-',";"] #the options of punctuations
    for sent in sents:
        sent = ''.join(ch for ch in sent if ch not in labels)#remove punctuation from the sent
        text_word=sent.split() #split the sent to words
        words=text_word[:] #create a copy of the list of the words 
        unmasker = pipeline('fill-mask', model='gerulata/slovakbert')#using slovakbert to predict the correct punctuation
        for i in range(1,len(text_word)+1):
            text_word.insert(i,'<mask>')#to put the mask after every word in the sent
            sent=" ".join(text_word)#collect the words to create the set again
            text_with_punc=unmasker(sent)#predict the correct punc after every word
            if text_with_punc[0]['token_str'] in labels:
                #save the word with corect punc
                words[i-1]=words[i-1]+text_with_punc[0]['token_str']
            text_word=words[:]#copy the words list to text_word list to put the mask at the right position in the next iteration
        new_text+= " ".join(words)#collect the words with the write punc to add every sent to collect the paragraph again
    return new_text


# In[ ]:


#create an interface with input text and output text
interface = gr.Interface(fn=restore_punc_with_interface, inputs="text", outputs="text")
interface.launch(share=True)


# In[ ]:





# In[ ]:




