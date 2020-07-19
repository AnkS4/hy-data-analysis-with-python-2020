#!/usr/bin/env python3

class Rational(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"{self.a}/{self.b}"
    def __mul__(num1, num2):
        return Rational(num1.a*num2.a, num1.b*num2.b)
    def __truediv__(num1, num2):
        return Rational(num1.a*num2.b, num1.b*num2.a)
    def __add__(num1, num2):
        return Rational(num1.a*num2.b + num2.a*num1.b, num1.b*num2.b)
    def __sub__(num1, num2):
        return Rational(num1.a*num2.b - num2.a*num1.b, num1.b*num2.b)
    def __eq__(num1, num2):
        return num1.a == num2.a and num1.b == num2.b
        #num1.a*num2.b == num2.a*num1.b
    def __gt__(num1, num2):
        return num1.a*num2.b > num2.a*num1.b
        '''
        if num1.b == num2.b:
            return num1.b > num2.b
        else:
            return num1.a*num2.b > num2.a*num1.b
        '''
    def __lt__(num1, num2):
        return num1.a*num2.b < num2.a*num1.b
        '''
        if num1.b == num2.b:
            return num1.b < num2.b
        else:
            return num1.a*num2.b < num2.a*num1.b
        '''

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
