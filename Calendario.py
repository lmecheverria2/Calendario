# Importando el módulo tkinter
from tkinter import *
# Importando el módulo calendar
import calendar

# Función para mostrar el calendario del año ingresado
def showCalendar():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendario del año")
    gui.geometry("550x600")
    try:
        year = int(year_field.get())
        gui_content = calendar.calendar(year)
        calYear = Label(gui, text=gui_content, font="Consolas 10 bold", bg='white', justify=LEFT)
        calYear.grid(row=0, column=0, padx=20, pady=20)
    except ValueError:
        error_label = Label(gui, text="Por favor ingrese un año válido", font="Arial 12", fg="red")
        error_label.grid(row=1, column=0)
    gui.mainloop()

# Código principal
if __name__ == '__main__':
    # Creando ventana principal
    new = Tk()
    new.config(background='grey')
    new.title("Calendario")
    new.geometry("300x200")

    # Widgets principales
    cal = Label(new, text="Calendario", bg='grey', font=("Times", 28, "bold"))
    year = Label(new, text="Ingrese el año", bg='dark grey')
    year_field = Entry(new)
    button = Button(new, text='Mostrar Calendario', fg='Black', bg='Blue', command=showCalendar)
    exit_button = Button(new, text="Salir", fg='Black', bg='Red', command=new.destroy)

    # Posicionando los widgets
    cal.grid(row=0, column=1, pady=10)
    year.grid(row=1, column=1, pady=5)
    year_field.grid(row=2, column=1, pady=5)
    button.grid(row=3, column=1, pady=10)
    exit_button.grid(row=4, column=1, pady=10)

    # Ejecutando la ventana principal
    new.mainloop()
