#기본 계산기
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multifly(a, b):
    return a*b

def divide(a, b):
    return a/b

def get_sum(n):
    return n(n+1)/2

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num