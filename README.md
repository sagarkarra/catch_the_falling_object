# 🎮 Catch the Falling Objects Game Using Python Tkinter

A fun and interactive **Catch the Falling Objects** game developed using **Python** and **Tkinter**. In this game, the player controls a basket using the keyboard to catch randomly falling colored balls. The game offers multiple difficulty levels, keeps track of the player's score, counts missed objects, and ends after five misses.

---

## 📌 Features

- 🎯 Catch falling objects using a movable basket
- 🎮 Three difficulty levels:
  - Easy
  - Medium
  - Hard
- ⌨️ Keyboard controls (Left and Right Arrow keys)
- 🌈 Randomly generated colored balls
- 📊 Live score tracking
- ❌ Miss counter
- 🛑 Game Over after five missed objects
- 🔄 Restart game option
- ⬅️ Back to main menu option
- 🖥️ Simple and attractive graphical user interface

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- Canvas Widget
- Random Module

---

## 📂 Project Structure

```text
Catch-the-Falling-Objects/
│
├── main.py          # Main game source code
└── README.md        # Project documentation
```

---

## 📋 Requirements

- Python 3.x

Tkinter is included with Python, so no additional installation is required.

To verify Tkinter installation:

```bash
python -m tkinter
```

---

## 🚀 How to Run

1. Download or clone the repository.

2. Navigate to the project folder.

3. Run the game:

```bash
python main.py
```

4. Select a difficulty level to begin playing.

---

## 🎮 How to Play

1. Launch the game.
2. Choose one of the following difficulty levels:
   - Easy
   - Medium
   - Hard
3. Move the basket using:
   - ⬅️ Left Arrow Key
   - ➡️ Right Arrow Key
4. Catch the falling colored balls with the basket.
5. Each successfully caught ball increases your score by **1**.
6. Missing a ball increases the miss count.
7. The game ends after **5 misses**.
8. Click **Restart** to play again or **Back** to return to the main menu.

---

## 🎯 Game Rules

- Catch every falling ball.
- Each caught ball adds **1 point**.
- Missing **5 balls** ends the game.
- Higher difficulty levels increase the falling speed of the balls.

---

## 🎚️ Difficulty Levels

| Level | Ball Speed |
|--------|-----------:|
| Easy   | Slow |
| Medium | Medium |
| Hard   | Fast |

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| ⬅️ Left Arrow | Move Basket Left |
| ➡️ Right Arrow | Move Basket Right |

---

## 🧠 Game Logic

- A ball is created at a random horizontal position.
- The ball falls continuously toward the basket.
- If the basket catches the ball:
  - Score increases.
  - A new ball is generated.
- If the ball reaches the bottom:
  - Miss count increases.
  - A new ball is generated.
- When misses reach **5**, the game displays **Game Over** along with the final score.

---

## 🎯 Learning Outcomes

This project demonstrates:

- GUI development using Tkinter
- Canvas-based game development
- Keyboard event handling
- Collision detection
- Animation using `after()`
- Random object generation
- Game loop implementation
- Score and state management

---

## 🔮 Future Enhancements

- 🎵 Add background music and sound effects
- 🏆 High score leaderboard
- ❤️ Multiple lives system
- ⏸️ Pause and resume functionality
- 🌟 Bonus objects with extra points
- 💣 Dangerous objects to avoid
- 🎨 Improved graphics and animations
- 📈 Progressive difficulty increase
- 💾 Save high scores locally
- 🌙 Dark mode theme

---

## ⚠️ Limitations

- Single-player game only.
- High scores are not saved.
- No sound effects or background music.
- Game progress is not stored after closing.
- Limited object types (only colored balls).
