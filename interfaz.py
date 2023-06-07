import tkinter 
import re
import os


def aceptar():
    regex1 = '^Perfil.*'
    regex2 = '^.*G1 Z0 F.*'
    regex3 = '^.*M3 S1000'

    newFile = ''
    directory = os.getcwd()

    nombreArchivoNuevo = nombredelcodigo_entry.get()
    tiempoDeBandeo = tiempodelay_entry.get()
    alturaRetraccion = alturaderetraccion_entry.get()

    with open(f'{directory}/entrada.gcode', 'r') as f:
        for line in f:
            result1 = re.search(regex1, line)
            result2 = re.search(regex2, line)
            result3 = re.search(regex3, line)

            if not result1:
                if result2:
                    newFile += ';z-probe\n'
                    newFile += 'G91\n'
                    newFile += 'G38.2 Z-100 F1500\n'
                    newFile += 'G90\n'
                    newFile += 'G10 L20 P1 Z0\n'
                    newFile += 'G91\n'
                    newFile += f'G0 Z{alturaRetraccion}\n'
                    newFile += 'G90\n'
                elif result3:
                    newFile += f'M3 S1000 G4 P{tiempoDeBandeo}\n'
                else:
                    newFile += line

    with open(f'{directory}/entrada.gcode', 'w') as f:
        f.write('')
    
    with open(f'{directory}/{nombreArchivoNuevo}.gcode', 'x') as f:
        f.write(newFile)

    quit()
    

window = tkinter.Tk()
window.title("Editor de gcodes para Plasma")


frame = tkinter.Frame(window)
frame.pack()

ingvariables_frame = tkinter.LabelFrame(frame, text= "Corte Plasma CNC")
ingvariables_frame.grid(row= 0,column= 0, padx=20, pady=20)




nombredelcodigo_label = tkinter.Label(ingvariables_frame, text= "Nombre del codigo nuevo")
nombredelcodigo_label.grid(row= 0, column= 0,padx=50, pady=20 )

nombredelcodigo_entry= tkinter.Entry(ingvariables_frame)
nombredelcodigo_entry.grid(row= 1, column= 0 )

tiempodelay_label = tkinter.Label(ingvariables_frame, text= "Tiempo de bandeo[seg]")
tiempodelay_label.grid(row= 0, column= 1,padx=50, pady=20)

tiempodelay_entry= tkinter.Entry(ingvariables_frame)
tiempodelay_entry.grid(row= 1, column= 1 )
tiempodelay_entry.insert(0, "1.5")

alturaderetraccion_label = tkinter.Label(ingvariables_frame, text= "Altura de retraccion[mm]")
alturaderetraccion_label.grid(row= 0, column= 2,padx=50, pady=20 )

alturaderetraccion_entry= tkinter.Entry(ingvariables_frame)
alturaderetraccion_entry.grid(row= 1, column= 2 )
alturaderetraccion_entry.insert(0, "8")

recordatorio_label = tkinter.Label(ingvariables_frame, text= "Generalmente 8mm")
recordatorio_label.grid(row= 3, column= 2 )

recordatorio2_label = tkinter.Label(ingvariables_frame, text= "1.5seg hasta 10mm")
recordatorio2_label.grid(row= 3, column= 1 )

recordatorio3_label = tkinter.Label(ingvariables_frame, text= ".gcode")
recordatorio3_label.grid(row= 3, column= 0 )

ingresar_valores= tkinter.Button(frame, text= "aceptar", command=aceptar)
ingresar_valores.grid(row=4, column=0, sticky="news", padx=10, pady=5,)


window.mainloop()