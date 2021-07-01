

num_tries = 0
num_check = 0
num_x = 0


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


if __name__ == "__main__":
  main()
