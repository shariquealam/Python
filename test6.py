


def find_replace(input, p1, p2):
    updated = list(input[:])
    Flage1 = True
    Flage2 = True

    for i in range(len(p1)):
        if p1[i] != updated[i]:
            Flage1 = False
            break

    if Flage1 == True:
        for i in range(len(p1)):
            if updated[i].islower():
                updated[i] = chr(ord(updated[i]) - ord('a') + ord('A'))
            else:
                updated[i] = chr(ord(updated[i]) - ord('A') + ord('a'))

    for j in range(len(p2)):
        if (p2[len(p2)-1-j] != updated[len(updated)-1-j]):
            Flage2 = False
            break


    if Flage2 == True:
        for i in range(len(p2)):
            if updated[len(updated)-1-i].islower():
                updated[len(updated)-1-i] = chr(ord(updated[len(updated)-1-i]) - ord('a') + ord('A'))
            else:
                updated[len(updated)-1-i] = chr(ord(updated[len(updated)-1-i]) - ord('A') + ord('a'))

    return "".join(updated)



input = 'aBdcdjfhksjhfnQws23838#Qws'
P1 = 'aBdc'
P2 = 'Qws'


print find_replace(input, P1, P2)


    # AbDC-----qWS

