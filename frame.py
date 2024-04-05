import tkinter as tk
from tkinter import scrolledtext
import chatbot
def enviar_mensaje(event=None):
    global chatbot
    mensaje_usuario = entrada_usuario.get()
    respuesta_chatbot = chatbot.chatbot(mensaje_usuario)
    conversacion.config(state=tk.NORMAL)
    conversacion.insert(tk.END, "TÚ: " + mensaje_usuario + "\n")
    conversacion.insert(tk.END, "CHATBOT: " + respuesta_chatbot + "\n")
    conversacion.config(state=tk.DISABLED)
    
    entrada_usuario.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Chatbot 2024")

# Crear menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de")

# Crear frame para la conversación
conversacion = scrolledtext.ScrolledText(ventana, width=60, height=30, wrap=tk.WORD,font=("Arial", 12))
conversacion.grid(row=0, column=0, padx=20, pady=20, columnspan=3)
conversacion.insert(tk.END, "Welcome \U0001F60A\nHi! I'm ChatBot \U0001F916\n")
conversacion.config(state=tk.DISABLED)

# Crear frame para la entrada del usuario
entrada_usuario = tk.Entry(ventana, width=50, font=("Arial", 12),)
entrada_usuario.grid(row=1, column=0, padx=20, pady=10)
entrada_usuario.bind("<Return>", enviar_mensaje)

# Crear botón de enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.grid(row=1, column=1, padx=10, pady=10)

# Botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.grid(row=1, column=2, padx=10, pady=10)

# Ejecutar la ventana principal
ventana.mainloop()