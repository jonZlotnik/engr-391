def func (x):
    return x**2 - 9


def secant_method(x_i, x_h, f, err):

    secant_formula = lambda x_i, x_h: (f(x_i)*(x_h - x_i)) / (f(x_h) - f(x_i))

    while abs(f(x_i)) > err:
        next_x_i = secant_formula(x_i, x_h)
        x_h = x_i
        x_i = next_x_i
    return x_i


    
if __name__ == "__main__":
    print(secant_method(100, 101, func, 0.01))
