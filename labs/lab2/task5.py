"""
На вход подается доменное имя сайта. Необходимо вывести все домены по порядку
начиная с домена первого уровня.
"""

if __name__ == '__main__':
    domain = str(input())
    s = ""
    j = len(domain)
    for i in range(len(domain)):
        if(domain[-i] == "."):
            s = domain[-i + 1:j]
            print(s)
            j = -i
    s = domain[0:j]
    print(s)
