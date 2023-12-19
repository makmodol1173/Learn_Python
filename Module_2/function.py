# define 
def func(num):
    result = num * 2
    print('inside the function.py file', result)
    return result

func(8)
func(88)

def sum(num1, num2):
    result = num1 + num2
    return result

total = sum(44, 39)
print('total value', total)

final = func(total)
print('final value', final)