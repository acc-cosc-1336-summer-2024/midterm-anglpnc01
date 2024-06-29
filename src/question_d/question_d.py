#write functions here, don't add input('') statements here!
#create a function with parameters kilometers and minutes
#returns miles per hour or mph and 'error' if out of range or conditions


def get_miles_per_hour(kilometers, minutes):

    conversion = .621371

    minutes /= 60
    
    mph = kilometers * conversion / minutes

    

    if kilometers <= 0:
        print('Invalid Entry')

    print(mph)

    return mph


    

