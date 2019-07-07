"""
Napisz funkcję do której przekazywana jest lista liczb całkowitych.
Zwróć true jeśli liczba 1 pojawia się na koncu lub na poczatku listy.
załóż że lista ma conajmniej jeden element
"""

def trueifone(numbers):
    start = numbers[0]
    end = numbers [-1]
    boolean = (start == '1' or end == '1')
    return boolean


if __name__== '__main__':
    while True:
        user_list = input('Provide number: ').split(' ')
        print(trueifone(user_list))

        decision = input('Do you want to break y/n: ')
        if decision.lower() == 'y':
            break
    print('Thank You')
