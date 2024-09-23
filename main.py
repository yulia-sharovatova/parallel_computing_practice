
def calculate_ch (a,b,c,d):
    ch = ((a+b)**2)-((c+d)**2)
    return ch

def calculate_z (a,b,c,d):
    z = ((c+a)**2)*((b+d)**2)
    return z



a = float(input("введите значение а"))
b = float(input("введите значение b"))
c = float(input("введите значение c"))
d = float(input("введите значение d"))

ch = calculate_ch(a,b,c,d)
z = calculate_z(a,b,c,d)

if z == 0:
    print ("ошибка деления на 0")
else:
    y=ch/z    
    print("результат вычисления:", y)

