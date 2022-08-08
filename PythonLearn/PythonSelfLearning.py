import math
import datetime

def arithmetic(a,b,c):
 if(c== '+'):
  print (a+b)
 elif(c == '-'):
    print(a-b)
 elif(c == '*'):
    print(a*b)
 elif(c == a/b):
    print(a/b)
 else:
    print("Неизвестная операция")

arithmetic(2, 3, '*')
    
def is_year_leap(year):
    if(year%400 == 0 or year%4==0):
        return True
    else:
        return False

print(is_year_leap(1550))

def square(side):
    S = side**2
    P = 4 * side
    D = math.sqrt(S*2)
    cor = (S, P, D,)
    return cor

def season(monthNumber):
    if (monthNumber == 12 or monthNumber == 1 
    or monthNumber == 2 ):
     print("Зима")
    elif(monthNumber>2 and monthNumber<=5):
     print("Весна")
    elif(monthNumber>5 and monthNumber<=6):
     print("Лето")
    elif(monthNumber>6 and monthNumber<12):
     print("Осень")
    else:
     print("Введите число")

     season(2)

def bank(a, years):
    a = a + (a * 0.1) * years
    return a

print(bank(100, 2))    

def is_prime(number):
    if(number>0 and number < 1001):
      for i in range(2,number) :
        if(number%i == 0 ):
            return False
            break
        else:
            return True    
    else:
        print("Введите число в диапозоне от 0 до 1000")

print(is_prime(3))

def date (day, month, year):
    d = datetime.date(1987, 12, 4)
    if (d.day == day and d.month == month and d.year == year):
        return True
    else:
        return False    
print(date(4,12,1987))

def XOR_cipher(stroka, key):
    encrioted_st = ""
    for letter in stroka:
        encrioted_st +=chr(ord(letter)^key)
    return encrioted_st

print(XOR_cipher('папа', 8))
encript_st = XOR_cipher('папа', 8)
print(XOR_cipher(encript_st, 8))

        