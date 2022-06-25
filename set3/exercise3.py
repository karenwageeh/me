"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """


print("\nWelcome to the guessing game!")
print("A number between _ and _ ?")


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """
    while True:
        user_input = input(f"input value between {low} and {high} ")
        try:
            num = int(user_input)
            if num > low and num < high:
                return num
            else:
                print(f"{num} is not between {low} and {high} ")
        except Exception as e:
            print(f"{user_input} isn't an integer. Enter an integer please\n({e})")


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        userin = input(message)
        try:
            num = int(userin)
            return num
        except:
            print("this is not a number")


def advancedGuessingGame():
    print("\nWelcome to the guessing game!")
    print("Enter an upperBound: ")
    upper_bound = super_asker(0, 100)
    print("Enter an lowerBound: ")
    lowerBound = super_asker(0, upper_bound - 1)
    print(f"OK then, a number between {lowerBound} and {upper_bound} ?")

    actualNumber = random.randint(lowerBound, upper_bound)

    while True:
        guessedNumber = not_number_rejector("Guess a number: ")
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            return "You got it!"
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")

    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
