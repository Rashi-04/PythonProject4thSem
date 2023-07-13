import random
import time

# function to create visual image of hangman.
def hangman_visual(turns):
		if turns == 5:
			print("________      ")
			print("|      |      ")
			print("|             ")
			print("|             ")
			print("|             ")
			print("|             ")
		elif turns == 4:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|             ")
			print("|             ")
			print("|             ")
		elif turns == 3:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /       ")
			print("|             ")
			print("|             ")
		elif turns == 2:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|\     ")
			print("|             ")
			print("|             ")
		elif turns == 1:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|\     ")
			print("|     /       ")
			print("|             ")
		else:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|\     ")
			print("|     / \     ")
			print("|             ")          
			print(f"GAME OVER!\nBETTER LUCK NEXT TIME.")          


# driver function.                        
def main():
    name = input("Hey Player!\nEnter your name : ")
    print("GOOD LUCK", name)
    time.sleep(1)
    num = int(input("""We have five categories for you :\nFor fruits enter 1\nFor vegetables enter 2\nFor birds enter 3\nFor animals enter 4\nFor flowers enter 5\n"""))
    if(num == 1):
        choices = ["apple", "mango", "banana", "grapes", "pineapple", "guava", "papaya","cherry", "orange", "watermelon"]
    elif(num == 2):
        choices = ["carrot", "tomato", "patato", "cabbage", "brinjal", "onion", "ladyfinger"]
    elif(num == 3):
        choices = ["sparrow", "bulbul", "parrot", "peacock", "crow", "eagle", "pigeon", "duck", "vulture"]
    elif(num == 4):
        choices = ["dog", "cat", "cow", "buffalo", "rabbit", "horse", "elephant", "bear", "fox"]
    elif(num == 5):
        choices = ["rose", "lily", "daisy", "sunflower", "lavender", "daffodil"]
    else:
        print("Please enter correct number next time.")
        return
    # selecting random object from list using random module.
    selected = random.choice(choices)  
    print("\nStart guessing...\n")
    # creating screen halt using time molule.
    time.sleep(0.5)
    # print(selected)
    newguess = ""
    turns = 5
    while(turns>0):
        flag = 0
        for char in selected:
            if char in newguess:
                print(char, end = "")
            else:
                print("_", end = "")
                flag -= 1
        if(flag == 0):
            time.sleep(1)
            print(f"\nWELL PLAYED {name}! YOU WON:)\n")
            break        
        time.sleep(0.5)
        print()
        guess = input("guess your character : ") 
        newguess += guess
        if(guess not in selected):
            turns -= 1
            hangman_visual(turns)
            if(turns != 0):
                print("wrong!") 
                print("you have", turns, "lives left... be careful!")
                  


if __name__ == "__main__":
       main()