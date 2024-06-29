#write functions here, don't add input('') statements here!

#print('Fahr\tCels')
#print('------------')

def get_fahrenheit(celsius):

    print('Fahr\tCels')
    print('------------')

    F = 9/5

    C = 32

    for celsius in range (0, 20 + 1):

        fahrenheit = F * celsius + C

        print(f'{celsius}\t{fahrenheit}')

    return get_fahrenheit
        
    
    