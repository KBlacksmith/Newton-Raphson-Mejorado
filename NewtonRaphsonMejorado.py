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
    err = 1
    while err > 0:
        x = x_i - ( func.subs(var, x_i) * derivada.subs(var, x_i) )/( (derivada.subs(var, x_i))**2 - func.subs(var, x_i) * segunda_derivada.subs(var, x_i) )
        err = float( abs( ( x - x_i )/x ) )
        x_i = x
    return (funciones, "x = "+str(x_i), "Error aproximado = "+str(err*100)+"%")

if __name__=="__main__": 
    f = input("Ingrese una función: ")
    x_i = float(input("x_0 = "))
    #x_i = input("x_i = ")
    #if x_i != "": 
      #  x_i = float(x_i)
    #else: 
     #   x_i = 0
    funciones, x, err = validar(f, x_i)
    print(funciones)
    print(x)
    print(err)
