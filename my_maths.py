def calculate():
    value1 = str(input("Add, Multiply, Divide or Subtract\n")).upper()
    value2 = int(input("Enter a number\n"))
    value3 = int(input("Enter a number\n"))

    while value1 != "ADD" or "SUBTRACT" or "DIVIDE" or "MULTIPLY":
        if value1 == "ADD":
            result = value2 + value3
            print(f"{value2} + {value3} = {result}")
            break

        elif value1 == "MULTIPLY":
            result = value2 * value3
            print(f"{value2} * {value3} = {result}")
            break

        elif value1 == "DIVIDE":
            result = value2 / value3
            print(f"{value2} / {value3} = {result}")
            break

        elif value1 == "SUBTRACT":
            result = value2 - value3
            print(f"{value2} - {value3} = {result}")
            break
            
        print("Invalid input")
        value1 = str(input("Add, Multiply, Divide or Subtract\n"))


calculate()
