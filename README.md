# Maze Game
					

## Description

It's the implementation of a video game project. 
You are character stuck up in a Maze. To escape you have to get all items
and kill the guardian.

## Requirements
	Python3 , pygame and random to be installed.

	- setting.py is the screen set.
	- the folder class contains all the class.
	- you can run the programm with main.py. 

## How to install

**Create you project folder**
- create a repertory project
- create your folder "ressource"

**Create a virtual environment** 
- In the computer terminal write python pip install -m venv "env name"
- activate your virtual environment => env/Scripts/activate.ps1

**Install pygame**
- Activate your virtual environment 
- write the command python pip install pygame

## How these work

**Class folder**
Contains 2 classes representing the framework the game, Maze and MacGyver. Both are wrapping 
up by pygame with game class.
**Maze** is a dictionnary with keys tuple representing coordinates and values representing
wall, way, etc.
**MacGyver** is a rect who move only if destination is in the maze's grid and is a way. He can get items in his inventory and knock out the guardian if he get all items in the inventory.
**Game**
This class contains all element of the game symbolise by pictures.

**screen.py**
Contains 2 functions.The first use to draw the maze. The second use to create a game loop.

**settings.py**
Constants. 

**Maze.txt**
The maze.