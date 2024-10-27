#!/usr/bin/env python3
import random

def main():
    num_tries = 0
    print('******** Welcome to Safe Breaker ********\n')
    #print('Enter h for help')

    #prompt for number of tries
    while True:
        print('Enter the number of tries [default 10]: ')
        num_tries = input('> ')
        if num_tries == '':
            num_tries = 10
            break
        num_tries = int(num_tries)
        if num_tries <= 4 or num_tries > 20:
            print(f'Number of tries {num_tries} is invalid! Try again')
        else:
            break

    code_solution = gen_4_digit_code()
    #print(f'{code_solution=}')

    while num_tries > 0:
        while True:
            print('Guess the code')
            code_guess = input('> ')
            if check_input(code_guess) is True:
                break
            else:
                print('Incorrect input! try again')
        num_tries -=1

        #find the number of Vs and the number of Xs
        num_v, num_x = check_code(code_guess, code_solution)
        #print (f'V={num_v}\tX={num_x}\tTries left: {num_tries}')

        #build the print out
        print('  ',end='')
        for i in range(num_v):
            print('V',end='')
        for i in range(num_x):
            print('X',end='')
        print(f'\t\tTries left: {num_tries}')

        # if the code was solved
        if num_v == 4:
            print(f'Safe Opened! The code was {code_solution}\n')
            return

    # if we are out of tries
    print(f'Game Over! Answer: {code_solution}\n')

def check_code(guess, solution):
    num_v = 0
    num_x = 0
    for i in range(4):
        if guess[i] == solution[i]:
            num_v += 1
        elif guess[i] in solution:
            num_x += 1
    return num_v, num_x

def check_input(s):
    #this checks if the code has repeating digits
    if len(s) != len(set(s)):
        return False
    #this checks if the string is exactly 4 characters
    if len(s) != 4:
        return False
    #this checks if there are only digits in the string
    if not all(char in '0123456789' for char in s):
        return False
    return True

def gen_4_digit_code():
    return ''.join(random.sample('0123456789', 4))

if __name__ == '__main__':
    main()
