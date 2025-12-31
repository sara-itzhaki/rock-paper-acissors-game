Rock, Paper, Scissors Game

A simple and interactive "Rock, Paper, Scissors" game built with Python. This project allows a user to play against the computer and includes instructions for creating a standalone executable (EXE) file.

## Game Description
The game follows the classic rules:
* **Rock** beats **Scissors**.
* **Scissors** beats **Paper**.
* **Paper** beats **Rock**.
The user enters their choice, and the computer makes a random selection. The result is displayed immediately.

---

## Getting Started

### 1. Download the Project
Clone this repository or download the source code:
```bash
git clone <your-repository-url>
cd <project-folder-name>
2. Create a Virtual Environment
To keep dependencies organized, create and activate a virtual environment:

Windows:

PowerShell

python -m venv venv
.\venv\Scripts\activate
3. Install Requirements
Install the necessary dependencies (including PyInstaller for building the EXE):

Bash

pip install -r requirements.txt
Creating the Executable (EXE)
You can package the script into a single executable file that runs on Windows without requiring Python:

Build the EXE: Run the following command in your terminal:

Bash

pyinstaller --onefile main.py
Locate the Output: After the process finishes, navigate to the newly created dist folder.

Run the Game: Double-click main.exe inside the dist folder to start playing!

How to Play
Run the program.

Type rock, paper, or scissors and press Enter.

Type q at any time to quit the game.