from time import sleep

def func (x):
    return x**2 - 9


def method_of_false_position(x_l, x_u, f, err):
    
    if f(x_l) * f(x_u) >= 0.:
        raise Exception("Function must change sign over the interval.")
    
    x_r_estimate = lambda x_l, x_u: x_u - (f(x_u)*(x_l - x_u)) / (f(x_l) - f(x_u))
    
    x_r = x_r_estimate(x_l, x_u)
    
    while abs(f(x_r)) > err:
        print(x_r)
        # sleep(1)
        if f(x_l) * f(x_r) < 0:
            x_u = x_r
        elif f(x_l) * f(x_r) > 0:
            x_l = x_r
        else:
            break
        x_r = x_r_estimate(x_l, x_u)
    return x_r


if __name__ == "__main__":
    print(method_of_false_position(0, 1000, func, 0.0000001))
