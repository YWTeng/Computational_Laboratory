print('''Today we will play a game called sliding puzzle. Enter 
the number n (3<=n<=10), you can get a table of n*n, which contains 
number from 1 to (n*n-1) and a space. You need to move the numbers 
(switch the position of numbers and spaces). Let the result be ordered 
numbers and the space at the end of the table.
For example, if n=4, then the final result will be expressed as
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15     ''')

# When a non-integer is entered, the program will report
# error and let the user re-enter it.
while True:
    try:
        size = int(input("Enter the number n (3<=n<=10) of size:"))
        break
    except ValueError:
        print('Notice: input is not an integer.')

# First generate an ordered list of n*n
# The last digit is a space
puzzle = []
for i in range(1, size ** 2):
    puzzle.append(i)
puzzle.append(" ")

# Record this list as puzzle_final
# which is the last thing to be achieved
puzzle_final = puzzle.copy()

# def print_puzzle, let the list be printed as puzzle
def print_puzzle(puzzle):
    output = ""
    count = 0
    for i in puzzle:
        output = output + str(i) + " " * (4 - len(str(i)))
        count = count + 1
        if count == size:
            print(output)
            output = ""
            count = 0

# Use input to indicate the letters be used to represent left, right, up, down
left = input("Enter the letter you want to use to represent left:")
right = input("Enter the letter you want to use to represent right:")
up = input("Enter the letter you want to use to represent up:")
down = input("Enter the letter you want to use to represent down:")

# def move_puzzle, consider the changes in the positions of numbers and spaces
# in the puzzle when move is left, right, up, and down. If it cannot be moved,
# the program will pass directly without moving.
def move_puzzle(move):
    position = puzzle.index(" ")
    if move == left:
        if (position + 1) % size == 0:
            pass
        else:
            puzzle[position] = puzzle[position + 1]
            puzzle[position + 1] = " "
    elif move == right:
        if position % size == 0:
            pass
        else:
            puzzle[position] = puzzle[position - 1]
            puzzle[position - 1] = " "
    elif move == up:
        if position > size * size - size - 1:
            pass
        else:
            puzzle[position] = puzzle[position + size]
            puzzle[position + size] = " "
    elif move == down:
        if position < size:
            pass
        else:
            puzzle[position] = puzzle[position - size]
            puzzle[position - size] = " "
    else:
        print("Enter the right move chosen")

# def test_puzzle, consider the position of the space to indicate the suggested
# operation that can be done, and synthesize it into a sentence
def test_puzzle(puzzle):
    position = puzzle.index(" ")
    suggest = {"left-": left, "right-": right, "up-": up, "down-": down}
    if (position + 1) % size == 0:
        del suggest["left-"]
    elif position % size == 0:
        del suggest["right-"]
    elif position > size * size - size - 1:
        del suggest["up-"]
    elif position < size:
        del suggest["down-"]

    sentence = ""
    for direction in suggest.items():
        sentence = sentence + direction[0] + direction[1] + " "
    return sentence

# Use random to randomly generate a number b within 1-500 to indicate the number
# of steps to be taken, and randomly select left, right, up, and down at each step
# to form a random puzzle that can be used in the game
import random
b = random.randint(1, size ** 4)
for i in range(b):
    a = random.choice([left, right, up, down])
    move_puzzle(a)

# new randomized, solvable puzzle
print_puzzle(puzzle)

# def play, use a while loop to ensure that the game will
# repeat the loop until the puzzle reaches ordered
def play(puzzle):
    way = 0
    while True:
        if puzzle == puzzle_final:
            print("Congratulations! You are succeed in %d ways." % way)
            print("Do you want to continue the game?")
            break
        else:
            move = input("Enter the move you want, suggestion: "+test_puzzle(puzzle)+":")
            move_puzzle(move)
            print_puzzle(puzzle)
            way = way + 1

play(puzzle)

# You can choose to continue the game or exit
choose = input("Enter'q' to end the game, other else to start new one:")

# If you have not opted out, the game will continue.
while True:
    if choose == 'q':
        break
    else:
        while True:
            try:
                size = int(input("Enter the number n (3<=n<=10):"))
                break
            except ValueError:
                print('Notice: input is not an integer.')

        puzzle = []
        for i in range(1, size ** 2):
            puzzle.append(i)
        puzzle.append(" ")
        puzzle_final = puzzle.copy()
        
        import random
        b = random.randint(1, size ** 4)
        for i in range(b):
            a = random.choice([left, right, up, down])
            move_puzzle(a)

        print_puzzle(puzzle)

        play(puzzle)

        choose = input("Enter'q' to end the game, other else to start new one:")
        