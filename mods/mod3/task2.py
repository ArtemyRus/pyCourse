"""
Для введенного в десятичном коде натурального числа найти представление в двоичном,
восьмеричном и шестнадцатеричном кодах. Если введено не натуральное число, вывести
диагностику: «Неверный ввод»
"""

def main():
    try:
        n = int(input())
        print(f"bin: {bin(n)}\noct: {oct(n)}\nhex: {hex(n)}")
    except ValueError:
        print("Неверный ввод")

if __name__ == "__main__":
    main()