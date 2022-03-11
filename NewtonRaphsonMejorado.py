from math import isnan
from sympy import sympify, Symbol, SympifyError, Derivative

def validar(f: str, x_i: float): 
    try: 
        func = sympify(f)
    except SympifyError: 
        return ("Función inválida", "", "")
    var = Symbol("x")
    derivada = Derivative(func, var).doit()
    segunda_derivada = Derivative(derivada, var).doit()
    funciones = "f(x) = "+str(func)+"\nf'(x) = "+str(derivada)+"\nf''(x) = "+str(segunda_derivada)
    print(funciones)
    err = 100
    i = 1
    while err > 0.1:
        x = x_i - ( func.subs(var, x_i) * derivada.subs(var, x_i) )/( (derivada.subs(var, x_i))**2 - func.subs(var, x_i) * segunda_derivada.subs(var, x_i) )
        try:
            err = float( abs( ( x - x_i )/x )*100 )
        except: 
            return ("Función inválida", "", "")
        print("Iteración #"+str(i))
        print("x = "+str(x))
        print("Error = "+str(err)+"%")
        print("-"*20)
        x_i = x
        i+=1
    if isnan(err): 
        err = 0
    if isnan(x_i): 
        x_i = 0
    return (funciones, "x = "+str(round(x_i, 6)), "Error aproximado = "+str(round(err, 3))+"%")

if __name__=="__main__": 
    f = input("Ingrese una función: ")
    x_i = float(input("x_0 = "))
    funciones, x, err = validar(f, x_i)
    print(funciones)
    print(x)
    print(err)