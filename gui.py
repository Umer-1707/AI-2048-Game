import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

from board import Initialize_Board, make_move, spawn_new_tile
from expectimax import get_best_move, get_valid_moves


# 🎨 COLORS
COLOR_MAP = {
    0: ("ghost white", "black"),
    2: ("light goldenrod yellow", "black"),
    4: ("goldenrod", "black"),
    8: ("orange", "white"),
    16: ("dark orange", "white"),
    32: ("tomato", "white"),
    64: ("red3", "white"),
    128: ("orchid1", "white"),
    256: ("medium orchid", "white"),
    512: ("medium purple", "white"),
    1024: ("purple3", "white"),
    2048: ("DeepPink3", "white")
}


# =========================
# 🚀 MAIN APP
# =========================
def main_app():
    root = tk.Tk()
    root.title("2048 Game")
    root.geometry("900x650")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    load_home(root)
    root.mainloop()


# =========================
# 🏠 HOME (SPLASH)
# =========================
def load_home(root):
    frame = tk.Frame(root)
    frame.grid(sticky="nsew")

    canvas = tk.Canvas(frame, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    original_img = Image.open("assets/splash.png")

    def go_to_game():
        frame.destroy()
        load_game(root)

    start_btn = tk.Button(
        root,
        text="Start Game",
        command=go_to_game,
        font=("Helvetica", 14, "bold"),
        fg="black",
        bg="#F5E6D3",
        activebackground="#EAD7C0",
        bd=0,
        padx=50,
        pady=5
    )

    quit_btn = tk.Button(
        root,
        text="Quit",
        command=root.quit,
        font=("Helvetica", 14, "bold"),
        fg="black",
        bg="#F5E6D3",
        activebackground="#EAD7C0",
        bd=0,
        padx=50,
        pady=5
    )

    def resize_bg(event):
        canvas.delete("all")

        resized = original_img.resize((event.width, event.height))
        bg = ImageTk.PhotoImage(resized)

        canvas.bg = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # 🎯 BUTTON POSITION
        y = int(event.height * 0.89)
        x = event.width // 2

        canvas.create_window(x - 145, y, window=start_btn)
        canvas.create_window(x + 140, y, window=quit_btn)

    canvas.bind("<Configure>", resize_bg)


# =========================
# 🎮 GAME SCREEN
# =========================
def load_game(root):
    frame = tk.Frame(root)
    frame.grid(sticky="nsew")

    board = Initialize_Board()
    score = 0

    title = tk.Label(frame, text="2048 Game with AI Assistance",
                     font=("Helvetica", 18, "bold"))
    title.pack(pady=10)

    grid_frame = tk.Frame(frame, bg="#D6CFC7")
    grid_frame.pack()

    tiles = [[tk.Label(grid_frame, width=6, height=3,
                       font=("Helvetica", 20, "bold"))
              for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            tiles[i][j].grid(row=i, column=j, padx=5, pady=5)

    suggestion_label = tk.Label(frame, text="", bg="light cyan", font=("Helvetica", 16))
    suggestion_label.pack(pady=10)

    quit_btn = tk.Button(frame, text="Quit",
                         bg="firebrick2",
                         font=("Helvetica", 14, "bold"),
                         command=lambda: show_score(root, frame, score))
    quit_btn.pack(pady=5)

    score_label = tk.Label(frame, text="Score: 0",
                           font=("Helvetica", 14))
    score_label.pack(pady=5)

    def update():
        for i in range(4):
            for j in range(4):
                val = board[i][j]
                bg, fg = COLOR_MAP.get(val, ("white", "black"))
                tiles[i][j].config(text=str(val) if val else "", bg=bg, fg=fg)

        suggestion = get_best_move(board)
        suggestion_label.config(text=f"AI Suggestion: {suggestion}")
        score_label.config(text=f"Score: {score}")

    def key(event):
        nonlocal board, score

        moves = {
            'w': 'up', 'a': 'left', 's': 'down', 'd': 'right',
            'Up': 'up', 'Down': 'down', 'Left': 'left', 'Right': 'right'
        }

        key = event.keysym if event.keysym in moves else event.char
        
        if key in moves:
            new_board = make_move(np.copy(board), moves[key])

            if not np.array_equal(new_board, board):
                board = spawn_new_tile(new_board)
                score += 1
                update()

                if not get_valid_moves(board):
                    show_score(root, frame, score)

    root.bind("<Key>", key)
    update()


# =========================
# 🏁 SCORE SCREEN
# =========================
def show_score(root, old_frame, score):
    old_frame.destroy()

    frame = tk.Frame(root)
    frame.grid(sticky="nsew")

    tk.Label(frame, text=f"Total Score: {score}",
             font=("Helvetica", 24, "bold"),
             fg="firebrick").pack(pady=50)

    tk.Button(frame, text="Back to Home", font=("Helvetica", 14, "bold"),bg="#F5E6D3", fg="black", command=lambda: [frame.destroy(), load_home(root)]
              ).pack()


# =========================
# ▶ START
# =========================
if __name__ == "__main__":
    main_app()