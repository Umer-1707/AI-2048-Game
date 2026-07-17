# 🎮 2048 Game with AI Move Guidance

I created this 2048 game using Python with a clean graphical interface and an integrated AI assistant.
The goal was not just to recreate the classic game, but to enhance it with **smart move suggestions** using an AI algorithm.

This project combines **game logic, GUI design, and AI decision-making** into one simple yet effective application.

## 🚀 Features

* Classic 2048 gameplay
* AI Move Suggestions (Expectimax Algorithm)
* Arrow Key Controls (↑ ↓ ← →)
* Clean Tkinter GUI
* Splash Screen with responsive background
* Real-time Score Tracking
* Smooth and minimal UI design

## 🧠 AI Logic

The AI in this project is based on the **Expectimax algorithm**.

Unlike Minimax, 2048 includes randomness (new tiles appear randomly), so Expectimax is a better fit.

The AI evaluates moves based on:

* Available empty cells
* Maximum tile value
* Expected future board states

This allows it to suggest smarter and more reliable moves during gameplay.

## 🛠️ Tech Stack

* Python
* Tkinter (GUI)
* NumPy (Board operations)
* Pillow (Image handling)

## 📁 Project Structure

```
2048-AI-Game/
│── main.py
│── gui.py
│── board.py
│── expectimax.py
│── splash.png
│── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone <your-repo-link>
cd 2048-AI-Game
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the project:

```
python main.py
```

## ⚠️ Notes

* Make sure `splash.png` is in the root directory
* Works best in full-screen mode
* Arrow keys are recommended for smoother gameplay

## 💡 Why I Built This

I wanted to explore how AI algorithms can be applied to simple games to improve decision-making.

This project helped me understand:

* Game logic implementation
* AI algorithms (Expectimax)
* GUI design using Tkinter
* Handling user input and events

## 🚧 Future Improvements

* Better AI heuristic (monotonicity, smoothness)
* Tile animations
* Sound effects
* Restart button / game menu
* AI auto-play mode

## 👨‍💻 Author

**Umer Ahmed**

## ⭐ Final Thoughts

This project is more than just a game — it's a combination of logic, design, and AI working together.

Feel free to fork, modify, or improve it 🚀
