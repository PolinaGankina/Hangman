# Creating list of secret words and choosing randomly one
import re
import random
word_file = open("Harry_Potter.txt")
write_file=open("HP_Clean.txt","w")
for line in word_file:
    x1=line.replace("\"","")
    x=re.sub("^[A-Z]","0",x1)
    write_file.write(x)
write_file.close()
word_list = [re.findall("[A-Z]\w+",line) for line in open("HP_Clean.txt")]
w = sum([word for word in word_list if len(word)>0],[])
s = set(w) | set()
w1=[]
[w1.append(word)for word in list(s)if len(word)>=5]
w2 = random.choice(w1)
secret_word = w2.upper()
#Depending on the chosen difficulty level hiding the letters and showing the hidden word
level_of_difficulty=input("Choose word difficulty:Easy\\Hard: ")
if level_of_difficulty=="Easy":
    secret_list=list(secret_word)
    i=0
    while i<len(secret_list):
        secret_list[i]="-"
        i+=random.randrange(1,len(secret_list))
        show_word="".join(secret_list)
    #print ("Hidden word: ",show_word)
else:
    for i in secret_word:
        show_word = secret_word[0]+"-"*(len(secret_word)-2)+secret_word[-1]
    #print ("Hidden word: ",show_word)

#Creating hangman message
Hangman_parts={5:"his leg",4:"two legs",3:"two legs and his body",2:"two legs, his body and his arm",1:"two legs, his body and two arms",
               0:"his neck, he is dead, muahahah!"}