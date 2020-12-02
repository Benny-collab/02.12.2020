def my_sum(a, b):
    if a == 0:
        return b;
    elif b == 0:
        return a;
    elif a == 0 and b == 0:
        return a;
    elif a < 0:
        return my_sum(a+1, b-1)
    elif a<0 and b <0:
        return my_sum(a+1, b+1)
    return my_sum(a-1, b+1)
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
print("Сумма числел равна:", my_sum(a, b))