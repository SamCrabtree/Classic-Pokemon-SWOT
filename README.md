# Classic Pokemon SWOT 

In the Original Red, Blue, and Yellow games, there were 15 pokemon types including Normal, Fire, Water, Grass, Electric, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost and Dragon. Each of these types has advantages, and disadvantages 

The Classic Pokemon SWOT program allows you to choose your dream original pokemon team and then maps out your teams Strengths, Weaknesses, Oppurtunities, and Threats so you as a pokemon trainer can balance your team to poke-nirvana on your way to beat Gary and the Elite Four! 


## Goals of this Program 

1. Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.	

- This is done using the main() program function.

2. Connect to an external/3rd party API and read data into the app. 

- This is done by utilizing the Pokemon API.  

3. Visualize data in a graph, chart, or other visual representation of data.

- This is done using pie charts with Matplotlib. 

4. Utilize a virtual environment and document library dependencies in a requirements.txt file.
- This is done both via Poetry and the traditional requirements.txt file. 

## Setup and Install

### Via Requirements.txt
1. Clone the Repository to your local device. 
2. Navigate to the project folder with terminal or gitbash and create a virtual envioronment. 
- Windows
`code`python -m -venv venv
- Mac/Linux
`code`python3 -m -venv venv
3. Activate your virtual environment 
- Windows 
`code`venv\Scripts\activate.bat
- Mac/Linux
`code`source venv/bin/activate
4. Install the requirements.txt file using the following comand 
`code`pip install -r requirements.txt


### Via Poetry
1. Clone the Repository to your local device.
2. Install Poetry to your device. (For more information about poetry check out https://python-poetry.org/ )
3. Open the folder in terminal or gitbash and type 
`code`Poetry Shell
4. Next, install the required programs from the pyproject.toml file by typing 
`code`Poetry Install


## Running The Program

1. Once you have activate your virtual environment above
- For Windows: 
`code`python program.py

- For Mac/Linux:
`code`python3 program.py

2. You will be prompted to enter the names of the pokemon you wish to add to your theoretical team. In the event you do not know the names of the original 151 pokemon or their spelling, you can enter "list" at anytime to get a list of their spellings. Note that the team 

3. Once you finish, you will be presented with three figures. The first wil display your Dream Teams elemental buildup, the second will show which elements you will absolutely dominate in combat, and the third will show you what pokemon elements to look out for!  

