import tkinter as tk
import random

def generate_puzzle():
    # Define the pieces and their starting positions on a chessboard
    pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
    positions = [0, 1, 2, 3, 4, 5, 6, 7]

    # Define the movement rules for each piece
    movement_rules = {
        'rook': [(0, 1), (1, 0)],
        'knight': [(1, 2), (2, 1)],
        'bishop': [(1, 1)],
        'queen': [(0, 1), (1, 0), (1, 1)],
        'king': [(0, 1), (1, 0), (1, 1)]
    }

    # Shuffle the pieces and their starting positions
    random.shuffle(pieces)
    random.shuffle(positions)

    # Validate the puzzle by checking the movement rules for each piece
    valid_puzzle = False
    while not valid_puzzle:
        valid_puzzle = True
        for i in range(8):
            for j in range(i+1, 8):
                dx = abs(positions[i] - positions[j])
                dy = abs(i - j)
                if (dx, dy) not in movement_rules.get(pieces[i], []):
                    valid_puzzle = False
                    random.shuffle(pieces)
                    random.shuffle(positions)
                    break
            if not valid_puzzle:
                break

    # Update the labels with the new puzzle
    for i in range(8):
        labels[i].config(text=f"{positions[i] + 1}. {pieces[i]}")

# Create the GUI
root = tk.Tk()
root.title("Chess Puzzle Generator")

# Add labels for the pieces and their positions
labels = []
for i in range(8):
    label = tk.Label(root, text="", font=("Arial", 16))
    label.grid(row=i, column=0)
    labels.append(label)

# Add a button to generate a new puzzle
button = tk.Button(root, text="Generate", font=("Arial", 16), command=generate_puzzle)
button.grid(row=8, column=0)

# Run the GUI
root.mainloop()
