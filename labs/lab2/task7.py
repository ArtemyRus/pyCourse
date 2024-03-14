"""
На вход подается строка s и символ i. Необходимо найти количество символов i,
расположенных в начале строки.
"""

def foo(s :str, c) -> int:
    count = 0
    for i in range(len(s)):
        if(s[i] == c):
            while(i < len(s) and s[i] == c):
                i += 1
                count += 1
            break
    return count

if __name__ == '__main__':
    inputStr = str(input())
    symb = str(input())
    print(foo(inputStr, symb))