

try:
    a= 5
    b=1
    c = a/b
    print(c)
except ZeroDivisionError:
    print("division by zero exception")
finally:
    print("Finally executed")