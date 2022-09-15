#TODO: Demuestre por inducción que, para todo n mayor o igual que 4, n!>2^n
def primer_paso (n):
    factorial = 1
    while (n > 1):
        factorial *= n
        n -= 1
    p_01 = factorial
    p_02= 2** n
    if p_01 >p_02:
        return True
    else:
        return False
    k=primer_paso(n+1)
assert primer_paso(5)==True


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#TODO: Un granjero ha comprado una pareja de conejos para criarlos y luego venderlos.
#   Si la pareja de conejos produce una nueva pareja cada mes y la nueva pareja
#   tarda un mes más en ser también productiva, ¿cuántos pares de conejos podrá
#   poner a la venta el granjero al cabo de un año?

def f_fibonacci(n):
    a = 1
    b = 0
    for i in range(0, n + 1):
        b = b + a
        a = b - a
        print(a, end=',')


f_fibonacci(12)

