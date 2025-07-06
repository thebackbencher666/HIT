🕹️ SpaceShooter: Arcade-Style Space Battle
SpaceShooter is a 2D arcade-style multiplayer space battle game built in Python with Pygame. Engage in head-to-head spaceship duels, dodge bullets, earn points, and try to beat the high score!

🚀 Features
Two-player local controls

Bullet collision and health tracking

Dynamic scoring and high score system

Start screen, end screen, and replay options

Pixel-perfect sprite visuals with space background

Sound effect support (optional)

Modular and extensible codebase

📦 Folder Structure
bash
SpaceShooter/
├── Assets/
│   ├── spaceship_yellow.png
│   ├── spaceship_red.png
│   ├── space.png
│   └── sounds/
│       ├── fire.wav
│       ├── hit.wav
│       └── background.mp3
├── scores.txt
├── src/
│   ├── main.py
│   ├── game.py
│   ├── menu.py
│   └── scoreboard.py
└── README.md
🧑‍💻 Setup Instructions
Install Python (≥ 3.8): Download here

Install Pygame:

bash
pip install pygame
Clone or Download This Repository

Run the Game:

bash
python src/main.py
You can also run main.py from PyCharm or any other Python IDE.

🎮 Controls
Player	Action	Key
Yellow	Move	W / A / S / D
Yellow	Fire	Left Ctrl
Red	Move	Arrow Keys
Red	Fire	Right Ctrl
🏆 Scoring System
Earn points for successful hits.

Score is shown in-game and in the end screen.

Highest score is saved to scores.txt.

🔊 Sound Setup
Add sound effects to Assets/sounds/:

fire.wav – Bullet fire

hit.wav – Ship hit

background.mp3 – Looping background music

Don't have sounds? Grab free assets from Pixabay or OpenGameArt.

💻 Packaging into Executable (Optional)
Use PyInstaller:

bash
pip install pyinstaller
pyinstaller --onefile --add-data "Assets;Assets" src/main.py
Resulting .exe will be in the dist/ folder.

🧑‍🎨 Credits
Developed by Arif Assets from OpenGameArt and Pixabay
![Screenshot 2025-07-06 105950](https://github.com/user-attachments/assets/e0a51691-99c6-4459-987b-98ced1acdeb6)

