from to_do import TODO

def task3(radius):
    '''do not override the radius by creating
      another one eg, radius = 2. You
       can also test h/w against the e.g.
       given by Humberto in this case 2
       and the result was 12.57'''
    result = 2.0 * 3.1416 * radius
    '''You must also always keep the 
    'return' word as shown below'''
    return result

if __name__ == "__main__":
    result = task3(radius=2.0)
    print(result)

    '''you can also print the result by 
     typing: 
     print(task3(radius=2.0)) or
     print(task3(radius=0.0)) or
     print(task3(radius=5.0)) this
     will also give you results for
     each of the print lines'''