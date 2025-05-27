tab = int(input("tabuada do: "))

while tab <= 10:
    num = 1

    while num <= 10:
        print(f"{tab} x {num} = {tab*num}")
        num += 1
    tab += 1