from to_do import TODO


def task4(base, height):
    '''you have to add in the calculation
     for working out area of a triangle'''
    result = 0.5 * base * height
    return result

if __name__ == "__main__":
    print(task4(base=5.0, height=10.0)) #25
    print(task4(base=0.0, height=10.0)) #0.0
    print(task4(base=5.0, height=0.0)) #0.0
'''you can also lose the base&height & 
replace with just the numbers eg
print(task4(5.0, 10.0))'''