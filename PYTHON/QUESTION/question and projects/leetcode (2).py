# Write a program that reflects these changes and lets you practice with the concept of lists. 
# Your task is to:

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: 
# John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following 
# members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.
# By the way, are you a Beatles fan? (The Beatles is one of Greg's favorite bands. 
# But wait...who's Greg...?)

beatless=[]
j=["John Lennon", "Paul McCartney","George Harrison"]
beatless.append(j[0])
beatless.append(j[1])
beatless.append(j[2])

# print(beatless)
k=["Stu Sutcliffe","Pete Best"]
for i in range (len(k)):
    # print(k)
    beatless.append(k[0+i])
print(beatless)

del beatless[3:5]    
print(beatless)

beatless.insert(0,"Ringo Starr")
print(beatless)