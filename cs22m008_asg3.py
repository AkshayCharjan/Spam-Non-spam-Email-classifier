import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt

def testing_spam(testing_folder):
  spam=glob.glob("enron1\\spam\\*.txt")  #C:\Users\ASUS\Downloads\PRML ASG dataset new\enron1\ham
  ham=glob.glob("enron1\\ham\\*.txt")
  print(len(spam))
  print(len(ham))
  ham_dict={}
  super_dict={}
  spam_dict={}
  for email in ham:
    file=open(email,"r")
    words=file.read()
    file.close()
    words=words.replace("\n"," ")
    words=set(words.split(" "))
    for w in words:
      if w.isalpha():
        w=w.lower()
        if w in ham_dict.keys():
          ham_dict[w]+=1
          super_dict[w]+=1
        else: 
          ham_dict[w]=1
          super_dict[w]=1
  
  for email in spam:
    with open(email,"r",encoding='latin1') as file:
      words=file.read()
      file.close()
      words=words.replace("\n"," ")
      words=set(words.split(" "))
      for w in words:
        if w.isalpha():
          w=w.lower()
          if w in spam_dict.keys():
            spam_dict[w]+=1
            super_dict[w]+=1
          else: 
            spam_dict[w]=1
            if w not in super_dict.keys():
              super_dict[w]=0
            else:
              super_dict[w]+=1
  totalWords_ham=0
  for words in ham_dict:
    totalWords_ham+=ham_dict[words]

  totalWords_spam=0
  for words in spam_dict:
    totalWords_spam+=spam_dict[words]

  sorted_super_dict = sorted(super_dict,key=super_dict.get,reverse=True)[:2200]
  count_ham=0
  count_spam=0
  spam=glob.glob(testing_folder)
  for file in spam:
    with open(file,"r",encoding='latin1') as f:
      words = f.read()
      f.close()
      words=words.replace("\n"," ")
      words =words.split(" ")
      ham_len=len(ham)
      spam_len=len(spam)
      h=ham_len/(ham_len+spam_len)
      s=spam_len/(ham_len+spam_len)
      for w in sorted_super_dict:
              if w in ham_dict.keys() and w in words:
                  h*=ham_dict[w]/ham_len
              elif w in ham_dict:
                  h*=1-(ham_dict[w]/ham_len)
      for w in sorted_super_dict:
              if w in spam_dict.keys() and w in words:
                  s*=spam_dict[w]/spam_len
              elif w in spam_dict:
                  s*=1-(spam_dict[w]/spam_len)

      if (h<=s):
          count_spam+=1
          print("1")
      else :
          count_ham+=1
          print("0")
 
testing_folder ="test\\*.txt"
testing_spam(testing_folder)