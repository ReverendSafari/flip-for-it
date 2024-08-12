Flip for it is a simple command line python tool to emulate flipping a coin/rolling a die or set of dice etc

How to use:

##### Step One - Pull Repository

In your terminal of choice type in
``` git clone https://github.com/ReverendSafari/flip-for-it.git ```

##### How to run the program
This is a command line based application, you will use cl arguments to run the program.

The first argument after the program's name is always going to be the type of activity you would like to simulate or "help" to remind you of how it works

Currently the choices to simulate are "Coin" for a coin flip "Dice" to simulate rolling dice, and "Raffle" for simulating a raffle

###### Other needed arguments

For "Dice" you should follow with two extra arguments, the first for the number of dice you wish to roll, and the second to dictate how many sides should be on the dice getting rolled

EX: ``` python flip.py Dice 3 6 ```
Executing this command would siumlate rolling 3 six sided dice

Note: Both arguments must be positive integers under 100000, violating this rule or missing an argument will result in an error message

For "Raffle" you need one extra argument, a comma separated list of choices you would like in the raffle 

EX: ``` python flip.py Raffle pizza,pasta,sushi ```
Executing this command would simulate a raffle drawing with equal odds of selecting pizza, pasta, or sushi

Note: The list can NOT contain spaces, and it cannot be empty. Also if you wish to increase the odds of a certain option being selected simply repeat that item in the list as many times as you wish