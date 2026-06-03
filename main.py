import string_operation
import validation

userInput = input("Please enter a word: ")



print(validation.palindrom_checker(userInput, string_operation.reverse_word(userInput)))