from time import sleep

def func (x):
    return x**2 - 9
def func_prime(x):
    return 2 * x



def newton_raphson_method(x_i, f, fp, err):

    newton_raphson_formula = lambda x_i: x_i - f(x_i) / fp(x_i)

    while abs(f(x_i)) > err:
        x_i = newton_raphson_formula(x_i)
    
    return x_i


    
if __name__ == "__main__":
    print(newton_raphson_method(100, func, func_prime, 0.01))
