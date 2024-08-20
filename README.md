# USA States Guessing Game

## Overview

The "USA States Guessing Game" is an interactive Python game where players guess the names of U.S. states on a map. It utilizes the `turtle` library for graphical representation and `pandas` for data management. The game aims to help users learn the states of the U.S. by providing visual feedback on their guesses and generating a CSV file listing the states they haven't guessed correctly.

## Features

- Displays a U.S. map where players can guess state names.
- Uses a CSV file (`50_states.csv`) to retrieve state coordinates and compares user inputs with these states.
- Visually marks the guessed state names on the map at the correct positions.
- Saves the states that were not guessed into a CSV file (`states_to_learn.csv`) with their indices for further review.

## Files

- `main.py`: The main script that runs the game.
- `states.py`: Defines the `States` class to handle state representation and interactions on the map.
- `50_states.csv`: CSV file containing state names and their coordinates.
- `blank_states_img.gif`: Image of the U.S. map used in the game.
