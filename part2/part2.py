from math import pow, sqrt, fabs
import string

def min_enclosing_rectangle(radius, x, y):
    if radius < 0:
        return
    x1 = x - radius
    y1 = y - radius
    print("(" + str(x1) + ", " + str(y1) + ")")
    return

def series_sum():
    n = int(input("Please enter a non-negative integer: "))
    if n < 0:
        return
    sum = 1000
    for i in range (0, n):
        sum += 1/pow(i + 1, 2)
    print(sum)
    return

def pell(n):
    if n < 0:
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return 2 * pell(n - 1) + pell(n - 2)

def countMembers(s):
    characters = ["\\", ",",  "!", "2", "3", "4", "5", "6", "e", "f", "g", "h", "i", "j", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]
    count = 0
    for letter in s:
        for character in characters:
            if letter == character:
                count += 1
    print(count)
    return

def casual_number(s):
    count_num = 0
    count_minus = 0
    count_comma = 0
    count_letter = 0
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for letter in s:
        for number in numbers:
            if letter == number:
                count_num += 1
                break
        else:
            if letter == "-":
                count_minus += 1
            elif letter == ",":
                count_comma += 1
            else:
                count_letter += 1
    if count_minus > 1:
        return
    if count_num < 1:
        return
    if count_letter > 0:
        return
    print(s.replace(",", ""))
    return

def alienNumbers(s):
    count = 0
    for letter in s:
        if letter == "T":
            count += 1024
        elif letter == "y":
            count += 598
        elif letter == "!":
            count += 121
        elif letter == "a":
            count += 42
        elif letter == "N":
            count += 6
        elif letter == "U":
            count += 1
    print(count)
    return

def encrypt(s):
    encrypt = ""
    for i in range(0, int(len(s)/2)):
        encrypt += s[len(s) - i - 1]
        encrypt += s[i]
    if len(s) % 2 == 1:
        encrypt += s[int(len(s)/2)]

    print(encrypt)
    return

def oPify(s):
    result = ""
    for i in range(0, len(s) - 1):
        result += s[i]
        if (s[i].islower() or s[i].isupper()) and (s[i + 1].islower() or s[i + 1].isupper()):
            if s[i].islower():
                result += "o"
            elif s[i].isupper():
                result += "O"
            if s[i + 1].islower():
                result += "p"
            elif s[i + 1].isupper():
                result += "P"
    result += s[len(s) - 1]
    print(result)
    return

def nonrepetitive(s):
    for i in range(0, len(s) - 1):
        for j in range(1, int((len(s) - i)/2) + 1):
            if s[i:i + j] == s[i + j:i + j * 2]:
                print("False")
                return False
    print("True")
    return True

min_enclosing_rectangle(1, 1, 1)
min_enclosing_rectangle(4.5, 10, 2)
min_enclosing_rectangle(-1, 10, 2)
min_enclosing_rectangle(500, 1000, 2000)

#series_sum()
#series_sum()
#series_sum()

print(pell(0))
print(pell(1))
print(pell(2))
print(pell(3))
print(pell(-45))
print(pell(6))

countMembers("\\")
countMembers("2\'")
countMembers("1\'")
countMembers("2aAb3?eE'_13")
countMembers("one, Two")

casual_number("251")
casual_number("1,251")
casual_number("1251")
casual_number("-97,251")
casual_number("-97251")
casual_number("-,,,,")
casual_number("--97,251")
casual_number("-")
casual_number("-1,000,001")
casual_number("999,999,999,876")
casual_number("-2")

alienNumbers("a!ya!U!NaU")
alienNumbers("aaaUUU")
alienNumbers("")

encrypt("Hello, world")
encrypt("1234")
encrypt("12345")
encrypt("1")
encrypt("123")
encrypt("12")
encrypt("Secret Message")
encrypt(",'4'r")

oPify("aa")
oPify("aB")
oPify("ooo")
oPify("ax1")
oPify("abcdef22")
oPify("abcdef22x")
oPify("aBCdef22x")
oPify("x")
oPify("123456")

nonrepetitive("")
nonrepetitive("a")
nonrepetitive("zrtzghtghtghtq")
nonrepetitive("abcab")
nonrepetitive("12341341")
nonrepetitive("44")