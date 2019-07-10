def work():
    astericks = ""
    count = 0
    times = 3
    while count <= times:
        astericks = "****"
        print(astericks)
        count += 1

def work1():
    astericks = ""
    count = 0
    while len(astericks) != 4:
        astericks += "*"
        print(astericks)
        count += 1
        while len(astericks) == 4:
            astericks -= ""
            print(astericks)

    

work1()

