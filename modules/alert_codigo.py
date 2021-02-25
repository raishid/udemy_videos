from tkinter import *

def Solicitar_codigo():
    win = Tk()
    win.title('Introduce url del curso')
    win.geometry('300x300')
    win.resizable(0, 0)

    texto = Label(win, text='Introduce url del curso')
    texto.config(pady=5)
    texto.pack(anchor=CENTER)
    codigo_entry = StringVar()
    input_codigo = Entry(win, textvariable=codigo_entry).pack(anchor=CENTER)

    text2 = Label(win, text="introduce bien la url...")
    text2.config(fg="red")

    def Cerrar_aplicacion():
        if len(codigo_entry.get()) > 10:
            win.destroy()
        else:
            text2.pack(anchor=CENTER)

    Button(win, text="Enviar", command=Cerrar_aplicacion).pack(anchor=CENTER)

    win.attributes("-topmost", True)
    win.mainloop()

    return codigo_entry.get()