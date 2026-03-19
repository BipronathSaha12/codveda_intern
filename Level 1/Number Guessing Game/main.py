import random
class GaussingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.gusses = 0
    
    def guess(self, number):
        self.gusses +=1
        if number == self.number:
            return "Congratulations! You've guessed the number in {} guesses.".format(self.gusses)
        elif number < self.number:
            return "Too low! Try again."
        else:
            return "Too High! Try again."

if __name__ == "__main__":
    game = GaussingGame()
    while True:
        user_input = int(input("Enter your guess (between 1 and 100): "))
        result = game.guess(user_input)
        print(result)
        if "Congratulations" in result:
            break
    