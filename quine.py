def k(s):
    i = 0
    while i < len(s):
        if s[i] == '_':
            print(s[i + 1], end='')
            i += 2
        else:
            print(s[i], end='')
            i += 1
    print("'''" + s + "''')")

k('''def k(s):
    i = 0
    while i < len(s):
        if s[i] == '__':
            print(s[i + 1], end='')
            i += 2
        else:
            print(s[i], end='')
            i += 1
    print("'_''" + s + "'_'')")

k(''')
