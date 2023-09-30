#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    if length > 0:
        fibonacci.append(0)
        if length > 1:
            fibonacci.append(1)
            if length > 2: 
                i = 2
                while i <length:
                    fibonacci.append(
                        fibonacci[i - 1] + fibonacci[i - 2])
                    i += 1
    print(fibonacci)