import sys
from random import *
from math import pow, sqrt, fabs

def subtraction():
    minuend = randint(0, 9)
    subtrahend = randint(0, 9)
    difference = minuend - subtrahend
    answer = int(input("What is result of " + str(minuend) + "-" + str(subtrahend) + "?"))
    if answer == difference:
        return True
    else:
        return False

def exponentiation():
    base = randint(0, 9)
    exponent = randint(0, 9)
    power = pow(base, exponent)
    answer = int(input("What is result of " + str(base) + "^" + str(exponent) + "?"))
    if answer == power:
        return True
    else:
        return False

def primary_school_quiz(flag, n):
    num = 0
    if flag == 0:
        for i in range (0, n):
            print("Question " + str(i + 1) + ":")
            if subtraction():
                num += 1
    elif flag == 1:
        for i in range (0, n):
            print("Question " + str(i + 1) + ":")
            if exponentiation():
                num += 1
    return num

def primary_school():
    print("************************************************************************")
    print("*                                                                      *")
    print("*  __Welcome to my math quiz-generator for primary school students.__  *")
    print("*                                                                      *")
    print("************************************************************************")

    input(str(name) + ". What would you like to practice?")
    flag = int(input("0 for subtraction\n1 for exponentiation\n"))
    n = int(input("How many practice questions would you like to do? "))
    print(str(name) + ". What would you like to practice?")

    right_cnt = primary_school_quiz(flag, n)
    return right_cnt/n

def high_school_eqsolver(a, b, c):
    print("The quadratic equation " + str(a) + "*x^2 + " + str(b) + "*x + " + str(c) + " = 0")
    p = pow(b, 2) - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        print("is satisfied for all numbers x")
    elif a == 0 and b == 0:
        print("is satisfied for no number x")
    elif a == 0:
        print("has the following root/solution: " + str((-c)/b))
    elif p > 0:
        print("has the following real roots:\n" + str((-b+sqrt(p))/(2*a)) + " and " + str((-b-sqrt(p))/(2*a)))
    elif p == 0:
        print("has only one solution, a real root:\n" + str((-b)/(2*a)))
    elif p < 0:
        print("has the following two complex roots:\n" + str((-b)/(2*a)) + " + i " + str(sqrt(fabs(p))/(2*a)) + "\n and\n" + str((-b)/(2*a)) + " + i " + str(sqrt(fabs(p))/(2*a)))
    return

def high_school():
    print("**********************************************************")
    print("*                                                        *")
    print("*  __quadratic equation, a*x^2 + b*x + c = 0, slover.__  *")
    print("*                                                        *")
    print("**********************************************************")

    flag = input(str(name) + ", would you like a quadratic equation sloved?(Y/N)")
    while (flag == "Y"):
        print("Good choice!")
        a = int(input("Enter a number the conefficient a:"))
        b = int(input("Enter a number the conefficient b:"))
        c = int(input("Enter a number the conefficient c:"))
        high_school_eqsolver(a, b, c)
        flag = input(str(name) + ", would you like a quadratic equation sloved?(Y/N)")
    return

print("*************************************************************")
print("*                                                           *")
print("*  __Welcome to my math quiz-generator / equation-solver__  *")
print("*                                                           *")
print("*************************************************************")

name = input("What is your name? ")
input("Hi " + str(name) + ". Are you in?")
school = int(input("1 for primary school\n2 for high school or\n3 for none of the above?\n"))

if school == 1:
    right_rate = primary_school()

    if right_rate >= 0.9:
        print("Congratulations " + str(name) + "! You'll probably get an A tomorrow. Now go eat your dinner and go to sleep.\nGood bye " + str(name) + "!")
    elif right_rate >= 0.7:
        print("You did well " + str(name) + ", but I know you can do better.\nGood bye " + str(name) + "!")
    else:
        print("I think you need some more practice " + str(name) + ".\nGood bye " + str(name) + "!")
elif school == 2:
    high_school()
    print("Good bye " + str(name) + "!")
else:
    print(str(name) + " you are not a target audience for this software.\nGood bye " + str(name) + "!")