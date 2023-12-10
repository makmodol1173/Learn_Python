# in, not, not in, is, is not 
# >, <, >=, <=, ==, !==
# and, or

a = 1
boss = False
if a > 5:
    print( 'Greater than 5')
elif a > 3:
    print('Greater than 3')
elif a == 2:
    print('Equals to 2')
else:
    print('Nothing')

if boss is not True:
    print('Lazy and Angry')
else: 
    print('Thats good!')

coin = 'head'
# nested conditions
if boss == True:
    print('boss you are joss')
    if coin == 'tail':
        print('batting')
    else:
        print('bowling')
        if 5 > 2 or boss != True:
            print('do  something')
            if 8%2 == 0 and 5%2==1:
                print('even 8 is an even number')
else:
    print('you are loss not a boss')