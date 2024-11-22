import tkinter as tk
from tkinter import messagebox
import requests

def on_button_click_Mostrar_Nazionalida():
    nombre = txtNombre.get()
    url = f"https://api.nationalize.io?name={nombre}" 
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            mostrar_resultados(data)
        else:
            messagebox.showerror("Error", "Conexión no establecida!")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def mostrar_resultados(data):
    # Limpiar resultados anteriores
    for widget in resultado_frame.winfo_children():
        widget.destroy()
    
    # Mostrar el nombre y el conteo
    nombre_label = tk.Label(resultado_frame, text=f"Nombre: {data['name']} ({data['count']})", font=("Helvetica", 14))
    nombre_label.pack(pady=5)
    
    # Mostrar los países y sus probabilidades
    for pais in data['country']:
        pais_label = tk.Label(resultado_frame, text=f"{pais['country_id']}: {pais['probability']:.2%}", font=("Helvetica", 12))
        pais_label.pack(pady=2)

# Crear la ventana principal
root = tk.Tk()
root.title("App de Nacionalidad")
root.geometry("500x500")

# Crear panel 
panel = tk.Frame(root, bg="gray")
panel.pack(expand=True, fill='both')

# Header label
header_label = tk.Label(panel, text="Mostrar Nacionalidad", bg="lightblue", font=("Helvetica", 16, "bold"))
header_label.pack(side=tk.TOP, fill='x', padx=20, pady=10)

# Textbox para buscar nombres
txtNombre = tk.Entry(panel, width=50)
txtNombre.pack(pady=20)

# Crear un botón y asignarle la función on_button_click
button = tk.Button(panel, text="Buscar", command=on_button_click_Mostrar_Nazionalida)
button.pack(pady=20)

# Crear un frame para mostrar los resultados
resultado_frame = tk.Frame(panel, bg="white")
resultado_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Iniciar el bucle principal
root.mainloop()
