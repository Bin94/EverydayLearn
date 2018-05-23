import random

def create_number(number, long):
    str = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    b = []
    for i in range(number):
        a = ''
        for j in range(long):
            a +=random.choice(str)
        b.append(a)
    return b

if __name__ == '__main__':
    number = int(input('number:'))
    long = int(input('long:'))
    print(create_number(number,long))