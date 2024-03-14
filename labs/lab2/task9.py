"""
Человек вводит на сайте номер телефона, ему позволено для удобства использовать
кроме плюса и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы. Уберите их из ввода.
"""

if __name__ == '__main__':
    number = str(input())
    s = ""
    for i in range(len(number)):
        if(number[i] != "-" and number[i] != ")" and number[i] != "(" and number[i] != " "):
            s += number[i]
    print(s)