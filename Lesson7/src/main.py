from time import time

def timer(func):
    # stampa il tempo di esecuzione di una funzione
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__} executed in {(t2 - t1):.4f}s')
        return result
    return wrap_func

@timer
def somma(n):
    res = 0
    for i in range(n):
        res += i
    return res

somma(10)
somma(10000000)
