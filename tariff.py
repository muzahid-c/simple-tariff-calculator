# Step tatiff
def Residential(unit):
        if unit > 0 and unit <= 50:
            money = unit * 3.33 # life line
            return round(money,2)
        elif unit > 50 and unit <= 75:
            money = 50 * 3.33 + (3.53-3.33) * 50 + (unit - 50) * 3.53 # step 1, thresold value is 10
            return round(money,2)
        elif unit > 75 and unit <= 200:
            money = 75 * 3.53 + (unit - 75) * 5.01
            return round(money,2)
        elif unit > 200 and unit <= 300:
            money = 75 * 3.53 + (200-75) * 5.01 + (unit - 200) * 5.19
            return round(money,2)
        elif unit > 300 and unit <= 400:
            money = 75 * 3.53 + (200-75) * 5.01 + (300 - 200) * 5.19 + (unit - 300) * 5.42
            return round(money,2)
        elif unit > 400 and unit <= 600:
            money = 75 * 3.53 + (200-75) * 5.01 + (300 - 200) * 5.19 + (400 - 300) * 5.42 + (unit - 400) * 8.51
            return round(money,2)
        elif unit > 600:
            money = 75 * 3.53 + 10 + (200-75) * 5.01 + (300 - 200) * 5.19 + (400 - 300) * 5.42 + (600 - 400) * 8.51 + (unit - 600) * 9.93
            return round(money,2)
        

def Commercial(unit):
    money = unit * 9.58 # flat rate for all the time
    return round(money,2)

def ResidentialConstruction(unit):
    money = unit * 19.16 # Flat rate for all the time    
    return round(money, 2)

def ResidentialFF(unit):
    if unit > 0 and unit <= 200:
        money = unit * 0 # first 200 unit is free for Freedom Fighter
        return round(money,2)
    elif unit > 200 and unit <= 300:
        money = (unit - 200) * 5.19
        return round(money,2) # step 3
    elif unit > 300 and unit <= 400:
        money = (300 - 200) * 5.19 + (unit - 300) * 5.42
        return round(money,2) # step 4
    elif unit > 400 and unit <= 600:
        money = (300 - 200) * 5.19 + (400 - 300) * 5.42 + (unit - 400) * 8.51
        return round(money,2) # step 5
    elif unit > 600 and unit <=99998:
        money = (300 - 200) * 5.19 + (400 - 300) * 5.42 + (600 - 400) * 8.51 + (unit - 600) * 9.93
        return round(money,2) # step 6

