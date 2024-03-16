"""
Для введенного в десятичном коде натурального числа найти представление в двоичном,
восьмеричном и шестнадцатеричном кодах. Если введено не натуральное число, вывести
диагностику: «Неверный ввод». Использовать встроенные возможности языка python
запрещено.
"""

def decToBin(n):
    s = ""
    while (n > 0):
        s = str(n % 2) + s
        n = n // 2
    return s

def decToOct(n):
    s = ""
    while (n > 0):
        s = str(n % 8) + s
        n = n // 8
    return s

def decToHex(n):
    s = ""
    while (n > 0):
        m = n % 16
        if(m == 10): s = "A" + s
        elif(m == 11): s = "B" + s
        elif(m == 12): s = "C" + s
        elif(m == 13): s = "D" + s
        elif(m == 14): s = "E" + s
        elif(m == 15): s = "F" + s
        else: s = str(m) + s
        n = n // 16
    return s

def main():
    try:
        n = int(input())
        if (n < 1):
            raise ValueError
    except ValueError:
        print("Неверный ввод")
        exit()

    print("bin: " + decToBin(n))
    print("oct: " + decToOct(n))
    print("hex: " + decToHex(n))

if __name__ == '__main__':
    main()