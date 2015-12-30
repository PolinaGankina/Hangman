def Hangman_game():
    print ("""Oh no!\nVoldemort has got Harry in his clutches!\nThe only way to save him \nis to guess the word related to the magic world that was hidden by an evil spell.\nWill you help Harry?\n""")

#Creating list of hidden words and then choosing one randomly
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
        print ("Hidden word: ",show_word)
    else:
        for i in secret_word:
            show_word = secret_word[0]+"-"*(len(secret_word)-2)+secret_word[-1]
        print ("Hidden word: ",show_word)

#Creating hangman message
    Hangman_parts={5:"his leg",4:"two legs",3:"two legs and his body",2:"two legs, his body and his arm",1:"two legs, his body and two arms",
               0:"his neck, he is dead, muahahah!"}

# Guessing the missing letters and counting attempts
    letter_list=[]
    Number_attempts=6
    while Number_attempts>0 and secret_word != show_word:
        Number_attempts-=1
        player_input=input("Choose letter: ")
        letter=player_input.upper()
        if letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print ('Input must be a letter')
        else:
            if letter in letter_list:
                print ("You already used this letter, try another one")
                Number_attempts+=1
            else:
                if letter in secret_word:
                    show_list=list(show_word)
                    for i in range(len(secret_word)):
                        if secret_word[i]==letter:
                            show_list[i]=letter
                            show_word="".join(show_list)
                    print("Hidden word:",show_word)
                    letter_list.append(letter)
                    Number_attempts+=1
                else:
                    print("Oops, wrong,","Harry is hanging by",Hangman_parts[Number_attempts],".", Number_attempts, "attempts left")
                    letter_list.append(letter)
    else:
        if show_word==secret_word:
            print(secret_word)
            player_decision =input("Hurrah! You have guessed the magic word and Harry disapparated right under Voldermorts, em..snake holes! Wanna play again?(Yes\\No)")
        else:
            player_decision=input("Game over! Wanna try to save Harry again?(Yes\\No)")
    if player_decision=="No":
        print ("Good bye!")
    else:
        Hangman_game()

Hangman_game()








