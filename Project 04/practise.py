import json

from difflib import get_close_matches

  
data=json.load(open("data.json"))
 
def dictionary(word):
    if word in data:
       return data[word] 
    
    elif word.title() in data:
         return data[word.title()] 
     
    elif word.upper() in data:
         return data[word.upper()] 
     
    elif word.lower() in data:
         return data[word.lower()]
    
    elif  len(get_close_matches(word , data.keys())) > 0:
         print("did you mean %s insteads" %get_close_matches(word,data.keys())[0])
         MATCH=input("enter y for and n for no : ")
         
         if MATCH== "y": 
              return data[get_close_matches(word,data.keys())[0]]
         
         elif MATCH=="n":
              print("this word is not avail dictionary.")
     
         else:
              print("you input not match to y or n.")   
         
      
    else:
          print("this word is not avail in dictionary.")

      
word=input("Enter the word : ")
p=dictionary(word)

if type(p) == list:
    for item in p:
         print(item)
else:
  print(p)