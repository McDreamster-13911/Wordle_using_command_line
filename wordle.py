import os
import random

# file_name = "word_list.txt"
# directory = "/Wordle Word List"
# file_path = os.path.join(directory, file_name)

def load_file_and_get_word():

	script_directory = os.path.dirname(os.path.abspath(__file__))

	relative_file_path = os.path.join(script_directory, 'Wordle Word List', 'word_list.txt')

	with open(relative_file_path) as f:
		list_of_words = []
		for line in f:
			list_of_words.append(line.strip().upper())

	return random.choice(list_of_words)

def get_input(guess_num):

    while True:
        user_input = input(f"Guess {guess_num} : ")
        
        if len(user_input) != 5 and user_input.isalpha() is True:
            print("Please enter a 5 letter word and it should contain only letters")
            continue
        
        elif len(user_input) != 5:
            print("Please enter a 5 letter word")
            continue
        elif not user_input.isalpha():
            print("Please enter only alphabets")
            continue
        else:
            break
    return user_input.upper()

def guess_display(user_input, random_word):

		correct_chars = set()
		for char, correct in zip(user_input, random_word):
			if char == correct:
				correct_chars.add(char)

		misplaced_chars = set(user_input) & set(random_word) - correct_chars

		wrong_chars = set(user_input) - set(random_word)


		print("Correct letters:", ", ".join(sorted(correct_chars)))
		print("Misplaced letters:", ", ".join(sorted(misplaced_chars)))
		print("Wrong letters:", ", ".join(sorted(wrong_chars)))
		print("\n")


def game_over(random_word):
	print(f"You failed to guess the word. The word is: {random_word}")


def main():

	random_word = load_file_and_get_word()

	# main process

	guessed_word = False

	for guess_num in range(1,6):
		
		user_input = get_input(guess_num)

		guess_display(user_input.upper(), random_word.upper())

		if random_word.upper() == user_input.upper():
			print(f"The word is {random_word} and you guessed it correctly!\n")
			guessed_word = True
			break

	if not guessed_word:
		game_over(random_word)
    	

if __name__ == '__main__':
	main()
