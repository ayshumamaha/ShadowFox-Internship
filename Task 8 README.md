# Hangman Word Guessing Game

## Overview

This project implements a console-based Hangman word guessing game using Python.

A word is randomly selected from a predefined list, and the player attempts to reveal the hidden word by guessing individual letters within a limited number of attempts.

## Objectives

- Implement a Python-based guessing game.
- Randomly select a hidden word.
- Accept and validate user input.
- Track correct and incorrect guesses.
- Dynamically display game progress.
- Implement win and loss conditions.

## Technologies Used

- Python 3.x
- Random module
- Lists
- Strings
- Loops
- Conditional statements

## Workflow

1. Import the `random` module.
2. Create a list of possible words.
3. Randomly select a word.
4. Display hidden-letter placeholders.
5. Accept a letter from the user.
6. Check whether the letter exists in the word.
7. Reveal correctly guessed letters.
8. Reduce attempts for incorrect guesses.
9. Continue until the word is guessed or attempts are exhausted.

## Game Logic

Correct guesses reveal matching letters in the hidden word.

Incorrect guesses reduce the number of remaining attempts.

The game ends when:

- The complete word is successfully guessed, or
- The player runs out of attempts.

## Learning Outcomes

The project strengthens understanding of loops, conditional logic, randomization, strings, lists, input handling, and interactive program design.

## Author

M. Ayshwarya
