import os
import random

from string import ascii_letters, ascii_uppercase
from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

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

def get_input(guess_num, guesses):
    while True:
        guesses[guess_num] = input(f"Guess {guess_num} : ").upper()
        if len(guesses[guess_num]) != 5:
            print("Please enter a 5 letter word")
            continue
        elif not guesses[guess_num].isalpha():
            print("Please enter only alphabets")
            continue
        else:
            break
    return guesses[guess_num]

def guess_display(guesses, random_word):

		# correct_chars = set()
		# for char, correct in zip(user_input, random_word):
		# 	if char == correct:
		# 		correct_charchars.add(char)

		# misplaced_chars = set(user_input) & set(random_word) - correct_chars

		# wrong_chars = set(user_input) - set(random_word)


		# print("Correct letters:", ", ".join(sorted(correct_chars)))
		# print("Misplaced letters:", ", ".join(sorted(misplaced_chars)))
		# print("Wrong letters:", ", ".join(sorted(wrong_chars)))
		# print("\n")

	# char_status = {char: char for char_status in ascii_uppercase}

	for guess in guesses:
		styled_guess = []

		for char, correct in zip(guess, random_word):
			if char == correct:
				style = "bold white on green"
			elif char in random_word:
				style = "bold white on yellow"
			elif char in ascii_letters:
				style = "white on #666666"
			else:
				style = "dim"
			styled_guess.append(f"[{style}]{char}[/]")

		console.print("".join(styled_guess), justify="center")
	# console.print("\n" + "".join(char_status.values()), justify="center")

def game_over(random_word):
	refresh_page(headline="Game Over")
	console.print(f"\n[bold white on red]You failed to guess the word. The word is: {random_word}[/]")


def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")



def main():

	random_word = load_file_and_get_word()


	guesses = ["_" * 5] * 5

	# main process

	guessed_word = False

	for guess_num in range(1,6):
		
		refresh_page(headline=f"Guess {guess_num}")
		guess_display(guesses, random_word.upper())

		guesses.append(get_input(guess_num, guesses))

		

		if random_word.upper() == guesses[guess_num]:
			refresh_page(headline = "Game over")
			console.print(f"[bold on green]The word is {random_word} and you guessed it correctly![/]\n")
			guessed_word = True
			break

	if not guessed_word:
		game_over(random_word)
    	

if __name__ == '__main__':
	main()
