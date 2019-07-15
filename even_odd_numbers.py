from functools import reduce

total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print(total)
#i = int(input("Enter a number\n"))
#
#if(i % 2 == 0):
#    print (f"{i} is an Even Number")
#else:
#    print (f"{i} is an Odd Number")

numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]

def is_even(numbers): return numbers % 2 == 0



def is_odd(numbers): return numbers %  2 == 1
    
    

print(list(filter(is_even, numbers)))
print(list(filter(is_odd, numbers)))
print(list((filter(lambda numbers: numbers%2==0, numbers))))
print(list((filter(lambda numbers: numbers%2==1, numbers))))
