import random
dictionary = ['blue', 'red', 'green', 'yellow', 'brown', 'black']

graphs = [
"""       -----------
       |     |
       |     
       |    
       |    
       |    
       |    
       -----------""" ,
"""       -----------
       |     |
       |     O
       |    
       |     
       |    
       |    
       -----------""",
"""       -----------
       |     |
       |     O
       |     |    
       |     |
       |    
       |    
       -----------""",
"""       -----------
       |     |
       |     O
       |    _|    
       |     |
       |    
       |    
       -----------""",
"""       -----------
       |     |
       |     O
       |    _|_    
       |     |
       |    
       |    
       -----------""",
"""       -----------
       |     |
       |     O
       |    _|_    
       |     |
       |    |
       |    
       -----------""",
"""       -----------
       |     |
       |     O
       |    _|_
       |     |
       |    | |
       |    
       -----------"""     
]


def winning_prompt():
    print ("You won! Would you like to play another round?")
    next_round = input("Y/N >" )
    if next_round.capitalize().startswith("Y"):
        return True
    else:
        return False


def losing_prompt():
    print ("You lost! Would you like to play another round?")
    next_round = input("Y/N >" )
    if next_round.capitalize().startswith("Y"):
        return True
    else:
        return False

def print_instructions():
    print("This is the hangperson game!")
    print()
    print(graphs[0])
    print()

def game():
    play_again = True
    while play_again == True:
        print_instructions()
        i = 0
        word = random.choice(dictionary)
        char_list = list(word) #turn string into list
        wrong_letters = []
        right_letters = ["_"] * len(word)
        print (right_letters)

        while i < len(graphs)-1:
            letter = input("Guess a letter> ")

            if letter in char_list:
                index = [i for i, x in enumerate(char_list) if x == letter] # multiple occurance
                print (index)
                for j in index:
                    right_letters[j] =letter
                print (graphs[i])
                print ('word',right_letters)
                print ("List of wrong guesses", wrong_letters)

                if "_" not in right_letters:
                    break

            elif letter in word:
                letter_list = list(letter)
                for k in letter_list:
                    right_letters[char_list.index(k)] = k
                print (graphs[i])
                print ('word',right_letters)
                print ("List of wrong guesses", wrong_letters)
                
                if "_" not in right_letters:
                    break
            else:
                if letter not in wrong_letters:
                    wrong_letters.append(letter)
                    i += 1
                else:
                    print ("You guessed this already!")

                print (graphs[i])
                print ('word',right_letters)
                print ("List of wrong guesses", wrong_letters)
                
        if "_" not in right_letters:
            play_again = winning_prompt()
        else:
            play_again = losing_prompt()
    


game()