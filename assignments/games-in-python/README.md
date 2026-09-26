
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python to practice string manipulation, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Description

Create the initial game setup using a predefined list of words. Randomly select one word, create a hidden display for it, and give the player a limited number of incorrect guesses.

#### Requirements

Completed program should:

- Store at least five possible words in a list.
- Randomly select one word from the list.
- Display one underscore for each letter in the selected word.
- Set and display the number of incorrect guesses available.

### 🛠️ Implement the Guessing Loop

#### Description

Add a loop that accepts letter guesses and updates the game until the player reveals the word or runs out of incorrect guesses.

#### Requirements

Completed program should:

- Accept one letter as input for each guess.
- Reveal every matching letter in the hidden word.
- Track and display incorrect guesses remaining.
- Prevent a repeated guess from being counted more than once.
- End when the player guesses the word or has no guesses remaining.
- Display a clear win message or lose message when the game ends.
