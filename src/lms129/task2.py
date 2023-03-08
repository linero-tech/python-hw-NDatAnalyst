from to_do import TODO


def task2(number):
    result = number
    if number > 1:
        # loop from 2 to n / 2
        for i in range(2, int(number/2)+1):
            #If number is divisible by any number
            #between 2 and n / 2 not prime'''
            if (number % i) == 0:
                print(False)
            else:
                print(True)
    else:
        print(False)
    return result

if __name__ == "__main__":
    print(task2(27))


