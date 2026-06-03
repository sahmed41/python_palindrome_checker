import string_operation
import validation

userInput = input("Please enter a word: ")
if userInput == "":
    print("Empty")


print(validation.palindrom_checker(userInput, string_operation.reverse_word(userInput)))