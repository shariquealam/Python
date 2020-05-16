
def find_replace(input, p1, p2):
    updated = list(input[:])
    print(updated)

    for i in range(len(p1)):
        if p1[i] == updated[i]:
            if updated[i].islower():
                updated[i] = chr(ord(updated[i]) - ord('a') + ord('A'))
            else:
                updated[i] = chr(ord(updated[i]) - ord('A') + ord('a'))
        else:
            updated = list(input[:])
            break

    temp = updated[:]

    for j in range(len(p2)):
        if (p2[len(p2 ) - 1 -j] == updated[len(updated ) - 1 -j]):
            if updated[len(updated)-1-j].islower():
                updated[len(updated)-1-j] = chr(ord(updated[len(updated)-1-j]) - ord('a') + ord('A'))
            else:
                updated[len(updated)-1-j] = chr(ord(updated[len(updated)-1-j]) - ord('A') + ord('a'))
        else:
            updated = temp[:]
            break

    return "".join(updated)



input = 'aBdcdjfhksjhfnQws23838#Qws'
P1 = 'aBdc'
P2 = 'Qws'


print (find_replace(input, P1, P2))


# AbDC-----qWS

