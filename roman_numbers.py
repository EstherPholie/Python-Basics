def roman_numbers():
    number = int(input("Enter a number between 1 and 4999\n"))
    numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL", 
        50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
    
    for key, value in numerals.items():
        if number == key:
            print(value)
        
#    if number in numerals.keys():
 #       print(numerals.values())
            
    


roman_numbers()
