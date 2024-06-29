#write functions here, don't add input('') statements here!
def test_config():
    return True


def get_bonus_pay_amount(sales):
    
    if sales >= 0 and sales <= 499:
        bonus_5 = .05
        bonus_amount = sales * bonus_5
        
        print(int(bonus_amount))
        #return int(bonus_amount)
    
    elif sales >= 500 and sales <= 999:
        bonus_6 = .06
        bonus_amount = sales * bonus_6
        print(int(bonus_amount))
        #return int(bonus_amount)

    elif sales >= 1000 and sales <= 1499:
        bonus_7 = .07
        bonus_amount = sales * bonus_7
        print(int(bonus_amount))
        #return int(bonus_amount)

    elif sales >= 1500 and sales <= 1999:
        bonus_8 = .08
        bonus_amount = sales * bonus_8
        print(int(bonus_amount))
        #return int(bonus_amount)

    else:
        print('Invalid Arguments')
        return 'Invalid Arguments'
        
    
    return bonus_amount






