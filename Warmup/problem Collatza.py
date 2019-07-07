"""
Collatz algoritm solution
"""

def collatz(number):
    print(number)
    if number == 1:
        return
    elif number % 2 != 0:
        return collatz(number * 3 + 1)
    else:
        return collatz(number // 2)


if __name__ == '__main__':
    x = int(input('Please provide a number: '))
    collatz(x)