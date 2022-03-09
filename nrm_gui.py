from tkinter import Button, Entry, Frame, Label, Tk
import NewtonRaphsonMejorado as nrm

def oprimirBoton(f_entry: Entry, x_entry: Entry, f_label: Label, r_label: Label): 
    func = f_entry.get()
    if func != "": 
        try: 
            x_i = float(x_entry.get())
        except ValueError: 
            r_label.configure(text="Por favor ingresa un valor real para la x inicial")
        else: 
            f, x, err = nrm.validar(func, x_i)
            f_label.configure(text=f)
            r_label.configure(text=x+"\n"+err)
    else: 
        r_label.configure(text="Ingrese una función válida")

if __name__=="__main__": 
    root = Tk()
    root.title("Newton-Raphson Mejorado")
    primer_frame = Frame(root, width=200, height=200)
    Label(primer_frame, text="Newton-Raphson Mejorado", padx=40, pady=50).grid(columnspan=2)
    Label(primer_frame, text="Ingrese una ecuacion: ").grid(columnspan=2)
    Label(primer_frame, text="Ejemplo: \n\nx³-3x²+8x-20   --->   x**3-3*x**2+8*x-20").grid(columnspan=2)
    Label(primer_frame, text="f(x) = ", pady=20).grid(column=0, row=3)
    funciones_entry = Entry(primer_frame)
    funciones_entry.grid(column=1, row=3)
    Label(primer_frame, text="Valor inicial de x: ", pady=20).grid(column=0, row=4)
    x_inicial = Entry(primer_frame)
    x_inicial.grid(column=1, row=4)
    funciones_label = Label(primer_frame)
    respuesta = Label(primer_frame, text="")
    boton = Button(primer_frame, text="Ingresar ecuación", command=lambda: oprimirBoton(funciones_entry, x_inicial, funciones_label, respuesta)).grid(columnspan=2)
    funciones_label.grid(columnspan=2)
    respuesta.grid(columnspan=2)
    primer_frame.pack()
    root.mainloop()
