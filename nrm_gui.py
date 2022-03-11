from tkinter import Button, Entry, Frame, Label, StringVar, Tk
import NewtonRaphsonMejorado as nrm

def oprimirBoton(f_entry: Entry, x_entry: Entry, f_txt: StringVar, r_txt: StringVar): 
    func = f_entry.get()
    if func != "": 
        try: 
            x_i = float(x_entry.get())
        except ValueError: 
            f_txt.set("")
            r_txt.set("Por favor ingresa un valor real para la x inicial")
        else: 
            f, x, err = nrm.validar(func, x_i)
            f_txt.set(f)
            r_txt.set(x+"\n"+err)
    else: 
        r_txt.set("Ingrese una función válida")

if __name__=="__main__": 
    root = Tk()
    fnt = ('', 30, 'bold')
    root.title("Newton-Raphson Mejorado")
    primer_frame = Frame(root, width=200, height=200, padx=10, pady=10)
    Label(primer_frame, text="Newton-Raphson Mejorado", padx=40, pady=50, font=fnt).grid(columnspan=2)
    Label(primer_frame, text="Ingrese una ecuacion: ", font=fnt).grid(columnspan=2)
    Label(primer_frame, text="Ejemplo: \n\nx³-11x²+3x+135   --->   x**3-11*x**2+3*x+135", font=fnt, padx=15).grid(columnspan=2)
    Label(primer_frame, text="f(x) = ", pady=20, font=fnt).grid(column=0, row=3)
    funciones_entry = Entry(primer_frame, font=fnt)
    funciones_entry.grid(column=1, row=3)
    Label(primer_frame, text="Valor inicial de x: ", pady=20, font=fnt).grid(column=0, row=4)
    x_inicial = Entry(primer_frame, font=fnt)
    x_inicial.grid(column=1, row=4)

    func_txt = StringVar()
    func_txt.set("")

    resp_txt = StringVar()
    resp_txt.set("")

    funciones_label = Label(primer_frame, textvariable=func_txt, font=fnt)
    respuesta_label = Label(primer_frame, textvariable=resp_txt, font=fnt)
    
    boton = Button(primer_frame, text="Obtener Raíz", font=fnt, command=lambda: oprimirBoton(funciones_entry, x_inicial, func_txt, resp_txt)).grid(columnspan=2)

    funciones_label.grid(columnspan=2)
    respuesta_label.grid(columnspan=2)
    primer_frame.pack()
    root.mainloop()