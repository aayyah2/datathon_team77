d = {'accent': 1, 'hongkong': 2611, 'us': 309260, 'england': 105160, 'african': 7379, 'indian': 54655, 'other': 10512, 'canada': 36851, 'australia': 42098, 'scotland': 11131, 'philippines': 3413, 'singapore': 2579, 'bermuda': 596, 'newzealand': 10763, 'malaysia': 1359, 'ireland': 7205, 'wales': 1448, 'southatlandtic': 209}
us_val = 0
india_val = 0
african_val = 0
philippines_val = 0
uk_val = 0
other_val = 0
for key in d:
    if (key == 'us'):
        us_val = d[key]
    elif(key == 'indian'):
        india_val = d[key]
    elif(key == 'african'):
        african_val = d[key]
    elif(key == 'philippines'):
        philippines_val = d[key]
    elif(key == 'england'):
        uk_val = d[key]
    elif(key == 'scotland'):
        uk_val = d[key]
    elif(key == 'wales'):
        uk_val = d[key]
    else:
        other_val = other_val + 1
        
        
print(us_val, india_val, african_val, philippines_val, uk_val, other_val)
