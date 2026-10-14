import tkinter as tk
from tkinter import messagebox
import random

# Window setup
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")
root.configure(bg="#1e1e2f")

# Variables
current_player = "X"
board = [""] * 9
buttons = []
score_x = 0
score_o = 0
vs_ai = True  # True = play with computer

# Title
title = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24, "bold"),
                 bg="#1e1e2f", fg="#00f5ff")
title.pack(pady=10)

# Scoreboard
score_label = tk.Label(root, text="Player X: 0   Player O: 0",
                       font=("Arial", 14),
                       bg="#1e1e2f", fg="white")
score_label.pack()

# Turn label
turn_label = tk.Label(root, text="Turn: X",
                      font=("Arial", 16),
                      bg="#1e1e2f", fg="#ffcc00")
turn_label.pack(pady=10)

# Frame for board
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

# Functions
def check_winner():
    win_combinations = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    
    for a,b,c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    
    if "" not in board:
        return "Draw"
    
    return None

def update_score(winner):
    global score_x, score_o
    if winner == "X":
        score_x += 1
    elif winner == "O":
        score_o += 1
    
    score_label.config(text=f"Player X: {score_x}   Player O: {score_o}")

def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    turn_label.config(text="Turn: X")
    
    for btn in buttons:
        btn.config(text="", bg="#2b2b3c")

def ai_move():
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        move = random.choice(empty)
        board[move] = "O"
        buttons[move].config(text="O", fg="#ff4d6d")

def on_click(i):
    global current_player
    
    if board[i] == "":
        board[i] = current_player
        buttons[i].config(text=current_player,
                          fg="#00ff9f" if current_player == "X" else "#ff4d6d")
        
        winner = check_winner()
        
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                messagebox.showinfo("Game Over", f"{winner} Wins!")
                update_score(winner)
            reset_board()
            return
        
        current_player = "O" if current_player == "X" else "X"
        turn_label.config(text=f"Turn: {current_player}")
        
        if vs_ai and current_player == "O":
            root.after(500, ai_turn)

def ai_turn():
    global current_player
    
    ai_move()
    
    winner = check_winner()
    if winner:
        if winner == "Draw":
            messagebox.showinfo("Game Over", "It's a Draw!")
        else:
            messagebox.showinfo("Game Over", f"{winner} Wins!")
            update_score(winner)
        reset_board()
        return
    
    current_player = "X"
    turn_label.config(text="Turn: X")

# Create buttons
for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 20, "bold"),
                    width=5, height=2,
                    bg="#2b2b3c", fg="white",
                    activebackground="#3c3c5c",
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Control buttons
control_frame = tk.Frame(root, bg="#1e1e2f")
control_frame.pack(pady=15)

restart_btn = tk.Button(control_frame, text="Restart",
                        font=("Arial", 12),
                        bg="#00f5ff", fg="black",
                        command=reset_board)
restart_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(control_frame, text="Exit",
                     font=("Arial", 12),
                     bg="#ff4d6d", fg="white",
                     command=root.quit)
exit_btn.grid(row=0, column=1, padx=10)

root.mainloop()