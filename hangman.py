import random
import time
import string
#list of custom words 
words=["Kwantlen","Rai","Zimmerman","Light","Gravity","Space","Razor","Medicine","Horse","Mansion","Company","King","Fire","Octopus","Tiger","Paper","Match"]
#final image displayed if the user won
victory_graphic = [
"""
       
                                                                             We made it!   
                                                                            /
                                                                        O    O
                                                             ' .'; __ /N___/N____
                                                           .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
]
#animates the whale entering the screen
startup_graphic = [
"""
       
                                                                              
                                                                               
                                                                        O    O
                                                             ' .'; __ /N___/N____
                                                           .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
,
"""
  
    
-----,
   /-\ \                                                                        A whale is coming!
 ' .O  `\                                                                     /
|\_______)                                                               O    O
"/ / / /                                                      ' .'; __ /N___/N____
/'/'/'/'                                                      .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
,
"""
___       
   /      
  /       
 /                
/      ,----------------,
\____/'              /-\ \                                                      
                    ' .O  `\                                                  
|          ,--     |\_______)                                           O    O
|       <'   ,     "/ / / /                                  ' .'; __ /N___/N____
'~~~'    /'/'/'/'  / / / / '                                 .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
,
"""
_           ___       
 \,__   __,'',/      
    \/'   ./       
\       /              
\    /      ,--------------,
|   \____/'             /-\ \                                            
 \                    ' .O  `\                                          
   |          ,--     |\_______)                                  O    O
   |       <'   ,     "/ / / /                      '    .'; __ /N___/N____
    `,      '~~~'    /'/'/'/'                          .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
,
"""
____          ____       
 ', \,__   __,'',/     
   \    \/'   ./       
     \       /                 
       \    /      ,--------------,
        |   \____/'            /-\ \                                           
         \                    ' .O  `\                                         
          |          ,--     |\_______)                                 O    O
           |       <'   ,     "/ / / /                       ' .'; __ /N___/N____
            `,      '~~~'    /'/'/'/'                        .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
]
def starting_visual():
  print(startup_graphic[0])
  time.sleep(0.5)
  print(startup_graphic[1])
  time.sleep(0.5)
  print(startup_graphic[2])
  time.sleep(0.5)
  print(startup_graphic[3])
  time.sleep(0.5)
  print(startup_graphic[4])
  time.sleep(0.5)
#creating the whale images, a custom twist instead of the hangman images
image = [
"""
 ____          ____       .  ,,  ,, .
 ', \,__   __,'',/      . .:>}}Y{{<:. .'
   \    \/'   ./       ' .'. ''W' ' .' .
     \       /                 "
       \    /      ,-----------"--,
        |   \____/'            /-\ \                                           Row faster!
         \                    ' .O  `\                                         /
          |          ,--     |\_______)                                 O    O
           |       <'   ,     "/ / / /                       ' .'; __ /N___/N____
            `,      '~~~'    /'/'/'/'                        .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
  ,
"""
 ____        _____         .  ,,  ,, .
 ', \,__   __,'',/      . .:>}}Y{{<:. .'
   \    \/'   ./       ' .'. ''W' ' .' .
     \       /                 "
       \    /      ,-----------"--,
        |   \____/'            /-\ \                                     
         \                    ' .O  `\                                    
          |          ,--     |\_______)                            O    O
           |       <'   ,     "/ / / /                  ' .'; __ /N___/N____
            `,      '~~~'    /'/'/'/'                   .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
,
"""
____            ___       .  ,,  ,, .
 ', \,__   __,'',/      . .:>}}Y{{<:. .'
   \    \/'   ./       ' .'. ''W' ' .' .
     \       /                 "
       \    /      ,-----------"--,
        |   \____/'            /-\ \                                 He's getting closer!
         \                    ' .O  `\                                /
          |          ,--     |\_______)                       O    O
           |       <'   ,     "/ / / /             ' .'; __ /N___/N____
            `,      '~~~'    /'/'/'/'              .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
,
"""
____            ___       .  ,,  ,, .
 ', \,__   __,'',/      . .:>}}Y{{<:. .'
   \    \/'   ./       ' .'. ''W' ' .' .
     \       /                 "
       \    /      ,-----------"--,
        |   \____/'            /-\ \                            Row faster!
         \                    ' .O  `\                           /
          |          ,--     |\_______)                   O    O
           |       <'   ,     "/ / / /          ' .'; __ /N___/N____
            `,      '~~~'    /'/'/'/'           .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
,
"""
___            ___       .  ,,  ,, .
 ', \,__   __,'',/      . .:>}}Y{{<:. .'
   \    \/'   ./       ' .'. ''W' ' .' .
     \       /                 "
       \    /      ,-----------"--,
        |   \____/'            /-\ \                      He's almost got us!
         \                    ' .O  `\                     /
          |          ,--     |\_______)              O    O
           |       <'   ,     "/ / / /    ' .'; __ /N___/N____
            `,      '~~~'    /'/'/'/'     .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
,
"""
___            ___       .  ,,  ,, .
 ', \,__   __,'',/      . .:>}}Y{{<:. .'
   \    \/'   ./       ' .'. ''W' ' .' .
     \       /                 "
       \    /      ,-----------"--,
        |   \____/'            /-\ \                     Row faster!
         \                    ' .O  `\                  /
          |          ,--     |\_______)           O    O
           |       <'   ,     "/ / / / ' .'; __ /N___/N____
            `,      '~~~'    /'/'/'/' .',.'.`/'         /'
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
,
"""
____            ___       .  ,,  ,, .
 ', \,__   __,'',/      . .:>}}Y{{<:. .'
   \    \/'   ./       ' .'. ''W' ' .' .
     \       /                 "
       \    /      ,-----------"--,
        |   \____/'            /-\ \                
         \                    ' .O  `\              
          |          ,--     |\_______)      
           |       <'   ,     "/ / / /   ' .'; _
            `,      '~~~'    /'/'/'/'   .',.'.`/
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
]
image.reverse()
#creating custom messages based on wether the user won or lost
def victory_message():
  v=["Wow, great job you won!","Good job, you escaped the whale!","You barely escaped!","You're better than the whale!"]
  print(random.choice(v))
def lose_message():
  l=["Oh no, the whale got you!","The whale was faster than you!","Wow, you suck","You were so close!","You will escape next time!"]
  print(random.choice(l))
#list of varying responeses(either rude or nice)
def correct_responses():
  c = ["Good guess!","Amazing guess!", "That was a lucky guess","You're an amazing guesser!","You're so lucky",\
      "Wow, I would've never thought of that","You suck","This is too easy for you!","You're just lucky",
      "Luckiest person on earth","You're still terrible"]
  print(random.choice(c))
def incorrect_responses():
  i = ["That was a good try!","Who would even guess that?","So close!","Wow you are terrible at this",\
      "You will get it next time for sure!","That was a horrible guess","Don't give up!", "A monkey would guess better than you",\
      "Keep trying!","You will get it soon!","You should give up","You suck"]
  print(random.choice(i))

def game():
    #setup
    word=random.choice(words).upper()
    while word == "RAI" or word == "ZIMMERMAN":
        word=random.choice(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    #user input

    lives = 6
    starting_visual()
    while len(word_letters) > 0 and lives > 0:
        #displays they hidden word,initial whale image, and words guessed
        print(f"You have {lives} left. You have guessed:" + " ".join(used_letters))
        correct_words = [letter if letter in used_letters else "-" for letter in word]
        print(image[lives])
        print("Word: " , " ".join(correct_words))
        #user's guess
        user_guess=input("Guess a letter: ").upper()
        #adds the user's guess to the used letters list
        if user_guess in alphabet - used_letters:
            print("Checking...")
            time.sleep(1)
            used_letters.add(user_guess)
            #correct guess
            if user_guess in word_letters:
                correct_responses()
                word_letters.remove(user_guess)
                print(" ")
            #incorrect guess
            else:
                incorrect_responses()
                lives = lives - 1
                print("Not in word.")
        
        elif user_guess in used_letters:
            print("You have already selected that letter! Please select a different letter.")
        
        else:
            print("Invalid input.")
    #asks user if the want to quit or continue if they die
    #defeat
    if lives==0:
        print(image[0])
        lose_message()
        print(f"The word was {word}!")
        cont=input("Do you want to play again (Y) or quit (Q)?").upper()
        if cont=="Y":
            game()
        elif cont == "Q":
            print("Exiting in 5 seconds")
            time.sleep(5)
            exit()
        else:
            print("Please select one of the options given.")
    #asks user if the want to quit or continue if they win
    #victory
    else:
        print(victory_graphic[0])
        victory_message()
        print(f"You guessed the word {word}!")
        c=input(f"Do you want to play again (Y) or quit (Q): ").upper()
        if c == "Y":
            game()
        elif c == "Q":
            print("Exiting in 5 seconds")
            time.sleep(5)
            exit()
        else:
            print("Please select one of the options given.")
#initial startup loop asking the user if they want to play or not
while True:
    startup=input("Do you want to play whaleman (Y) or Quit (Q): ").upper()
    if startup == "Y":
        game()
    elif startup == "Q":
        print("Exiting in 5 seconds.")
        time.sleep(5)
        exit()
    else:
        print("Please select one of the options given.")