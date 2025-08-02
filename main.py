import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.buttons = []
        self.first_click = None
        self.matches_found = 0
        self.can_click = True
        
        # Create letters for the game (8 pairs)
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
        random.shuffle(self.letters)
        
        # Create the game grid
        for i in range(4):
            for j in range(4):
                button = tk.Button(root, text="", width=10, height=5,
                                 command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
                
    def button_click(self, row, col):
        index = row * 4 + col
        
        if not self.can_click or self.buttons[index]['text'] != "":
            return
            
        # Show the letter
        self.buttons[index]['text'] = self.letters[index]
        
        # First card of the pair
        if self.first_click is None:
            self.first_click = index
            return
            
        # Second card of the pair
        self.can_click = False
        self.root.after(1000, lambda: self.check_match(index))
        
    def check_match(self, second_index):
        if self.letters[self.first_click] == self.letters[second_index]:
            self.matches_found += 1
            if self.matches_found == 8:
                messagebox.showinfo("Congratulations!", "You've won the game!")
        else:
            # If no match, hide both cards
            self.buttons[self.first_click]['text'] = ""
            self.buttons[second_index]['text'] = ""
            
        self.first_click = None
        self.can_click = True

def main():
    root = tk.Tk()
    root.configure(bg='lightgray')
    game = MemoryGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
