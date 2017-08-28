#!/usr/bin/python3

import random
import math

l = 20

class BernoulliSampler:
    def __init__(self, c):
        self.p = c
    def __call__(self):
        return (random.random() < self.p)

class BernoulliExpSampler:
    def __init__(self, x, f):
        self.x = x
        self.f = f
        self.c = [math.exp(-2.0**i/f) for i in range(0, l)]
    def __call__(self):
        X = list(map(int, bin(self.x)[:1:-1]))
        for i in range(len(X)-1, -1, -1):
            if X[i] == 1:
                A = BernoulliSampler(self.c[i])
                if not A():
                    return False
        return True

class A_slash_B:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def __call__(self):
        while True:
            if self.A():
                return True
            if not self.B():
                return False

class BernoulliCoshSampler:
    def __init__(self, x, f):
        self.e1 = BernoulliExpSampler(x, f)
        self.e2 = BernoulliExpSampler(x, f)
        self.s  = BernoulliSampler(0.5)
    def __call__(self):
        while True:
            if self.e1():
                return True
            if not (self.e2() or self.s()):
                return False
        

def main():
    c = 0
    for i in range(int(1e6)):
        B = BernoulliCoshSampler(11, 10)
        if B():
            c+=1
    print(c)

if __name__ == "__main__":
    main()
