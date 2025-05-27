import json
def dictionary():
  
  data=json.load(open("data.json"))
 
  x=input("Enter the word : ")
  
  v=x.lower()
  if v in data:
    return data[v]
  else:
      print("this word is not available")
  return dictionary()
  print(data[v])  
dictionary()