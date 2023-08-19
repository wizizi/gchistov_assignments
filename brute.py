def deceasarChar(c, k):
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        orchar = ord(c) - k - ord('A')
        if orchar < 0:
            orchar = ord('Z') + orchar + 1
        else:
            orchar += ord('A')
        return chr(orchar)
    else:
        return c

def deceasarMessage(m, k):
    newm = ""
    for c in m:
        newm += deceasarChar(c, k)
    return newm

def crack(txt):
    m = txt.upper()
    for i in range(1, 26):
        print(deceasarMessage(m, i))


crack(input('Input encrypted line: '))