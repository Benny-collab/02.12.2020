def my_power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * my_power(a, n-1)
    elif n % 2 == 0:
        return my_power(a*a, n/2)
a=int(input("Введите число: "))
n=int(input("В какую степень будем возводить? "))
print("Число", a, "в степени", n, "=", my_power(a,n))