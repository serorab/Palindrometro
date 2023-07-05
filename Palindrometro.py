#Se importa la biblioteca Tkinter
import tkinter as tk

#Se crea la ventana Principal
ventana = tk.Tk()
ventana.geometry("300x200")
ventana.title('Palindrómetro')
mensaje = tk.Label(ventana, text='Pon una frase y te diré si es o no Palíndromo')
mensaje.pack()

#Se crea el cuádro o espacio en donde el usuario ingresará la frase
entrada = tk.Entry(ventana)
entrada.pack(pady=20)

#Función que determinará cuál frase es palíndromo y cuál no.
def juego():
	frase = entrada.get()
	if frase == '':
		mensajeSalida.config(text='El campo está vacío')
		mensajeFinal.config(text='')

	elif esPalindromo(frase):
		mensajeSalida.config(text=f'La frase "{frase}", Es palíndromo')
		entrada.delete(0, tk.END)
		mensajeFinal.config(text='¡Gracias por jugar!')

	else:
		mensajeSalida.config(text=f'La frase "{frase}", No es palíndromo')
		entrada.delete(0, tk.END)
		mensajeFinal.config(text='¡Gracias por jugar!')

#Función que invierte la frase ingresada y la compara consigo misma.
def esPalindromo (texto):
	fInv = texto[:: -1]

	if texto == fInv:
		return True

	else: 
		return False

#Botón que inicia la tarea
botonFrase = tk.Button(ventana, text='¡Haz click acá!', bg='#71d772', command=juego)
botonFrase.pack(pady=5)

#Mensaje de salida dentro de la ventana.
mensajeSalida = tk.Label(ventana, text='')
mensajeSalida.pack(pady= 10)

mensajeFinal = tk.Label(ventana, text='')
mensajeFinal.pack(pady=10)

ventana.mainloop()
