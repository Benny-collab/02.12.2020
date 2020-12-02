def my_div(a, n):
    if a == 0:
        return "∞"
    elif a == 1:
        return "Число простое, наибольший делитель равен 1"
    elif a < 0:
        return "Введите положительное число!"
    elif a % n != 0:
        return my_div(a, n-1)
    return n
a=int(input("Введите число: "))
n=a-1
res = my_div(a,n)
if res == 1:
    print("Число простое, наибольший делитель равен:", a)
else:
    print("Наибольший делитель ревен: ", my_div(a,n))