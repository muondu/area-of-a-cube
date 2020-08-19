def cube(number):
    """AREA OF A CUBE"""
    global cubes
    cubes = number * number * number
    print(cubes)
    # return cubes

def by_three(number):
    if number % 3 == 0:
         cube(number)
    else:
        print(False)
by_three(18)