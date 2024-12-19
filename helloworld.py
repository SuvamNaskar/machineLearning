import time

# hello = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
hello = [104, 101, 108, 108, 111, 119, 111, 114, 108, 100]
world = []

char = 97
c = 0
flag = 0

while char <= 122:
    for j in world:
        print(j, end=" ")
    if char == hello[c]:
        world.append(chr(char))
        print(chr(char), end=" ")
        if c < 9:
            c += 1
        else:
            flag = 1
        char = 96
    else:
        if char >= 97 and len(world) <=9:
            print(chr(char), end=" ")
            time.sleep(0.23)
        if flag == 1:
            print("  ==\n========================")
            break

    print()

    char += 1