def conv(c):
    c2 = c * 9 / 5 + 32
    return c2


celsius = int(input("Enter celsius: "))
fahrenheit = conv(celsius)
print(fahrenheit)
