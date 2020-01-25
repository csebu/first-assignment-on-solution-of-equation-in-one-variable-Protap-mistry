def bisection_method(x):
    return (x ** 3 - 2 * x ** 2 - 4)


a = 2
b = 3

print("Bisection Method: ")
for i in range(1, 20):
    x0 = (a + b) / 2
    print(x0);
    fx0 = bisection_method(x0)
    fa = bisection_method(a)
    fb = bisection_method(b)

    if fa * fx0 < 0:
        b = x0
    else:
        a = x0