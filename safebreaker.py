

num_tries = 0
num_check = 0
num_x = 0

import secrets

def main():
  print('Welcome to safebreaker')
  #print('Enter \'h\' for help")

  raw_input_str = input('> ')
  print(raw_input_str)

  input_int = int(raw_input_str)

  print(check_input(input_int))

def has_doubles(n):
    return len(set(str(n))) < len(str(n))

def check_input(input_str):
  input_int = int(input_str)
  return has_doubles(input_int)

def gen_solution():
  result = 9999
  while has_doubles(result):
    result = secrets.randbelow(10000)
  return result

if __name__ == "__main__":
  print(gen_solution())
  #main()
