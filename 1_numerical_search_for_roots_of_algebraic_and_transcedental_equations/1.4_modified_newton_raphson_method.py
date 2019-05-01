def func (x):
    return (x-3) * (x-1) * (x-1)
def func_prime(x):
    return 3*x**2 - 10*x + 7
def func_double_prime(x):
    return 6*x - 10



def modified_newton_raphson_method(x_i, f, fp, fpp, err):

    modified_newton_raphson_formula = lambda x_i: x_i - (f(x_i) * fp(x_i)) / (fp(x_i)**2 - f(x_i) * fpp(x_i))

    while abs(f(x_i)) > err:
        x_i = modified_newton_raphson_formula(x_i)
    
    return x_i


    
if __name__ == "__main__":
    print(modified_newton_raphson_method(0, func, func_prime, func_double_prime, 0.000001))
