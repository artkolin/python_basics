"""
Compare two persons
"""

def com(rating):
    sum_a = 0
    sum_b = 0
    for i in rating:
        if a[i] > b[i]:
            sum_a += 1
        if b[i] > a[i]:
            sum_b += 1
        if a[i] == b[i]:
            return


if __name__ == '__main__':
    #input_rating = input('Provide rating: ').strip().split(' ')
    a = list(map(int, input('Provide rating for candidate A: ').rstrip().split()))
    b = list(map(int, input('Provide rating for candidate B: ').rstrip().split()))
    print(com(a, b))