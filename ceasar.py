def ceasarChar(c, k):
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return chr((ord(c) + k - ord('A')) % 26 + ord('A'))
    elif ord(c) >= ord('a') and ord(c) <= ord('z'):
        return chr((ord(c) + k - ord('a')) % 26 + ord('A'))
    else:
        return c

def ceasarMessage(m, k):
    newm = ""
    for c in m:
        newm += ceasarChar(c, k)
    return newm

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

mode = 'w'
while mode != 'e' and mode != 'd':
    mode = input("Do you wish to (e)ncrypt or to (d)ecrypt?")
    if mode != 'e' and mode != 'd':
        print("Wrong command! Use e or d")

needKey = True
key = 0
while needKey:
    try:
        key = int(input("Enter the key:"))
        if(key < 0):
            raise Exception("negative key")
        needKey = False
    except:
        print("Invalid key, try again.")

if mode == 'e':
    m = input("Enter the message to encrypt: ")
    print(ceasarMessage(m, key))
elif mode == 'd':
    m = input("Enter the message to decrypt: ")
    print(deceasarMessage(m, key))
