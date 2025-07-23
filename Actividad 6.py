import tkinter as tk
from tkinter import messagebox, ttk
import os

# Ruta del archivo
file_path = os.path.join(os.path.expanduser("~"), "Downloads", "friendsContact.txt")

# Configuración de estilo
BG_COLOR = "#f0f0f0"
FONT = ("Arial", 10)

# Función para crear un nuevo contacto
def create_contact():
    name = entry_name.get()
    number = entry_number.get()
    
    if name and number:
        if contact_exists(name):
            messagebox.showwarning("Advertencia", "El contacto ya existe.")
            return
        
        with open(file_path, 'a') as file:
            file.write(f"{name}!{number}\n")
        messagebox.showinfo("Éxito", "Contacto agregado.")
        entry_name.delete(0, tk.END)
        entry_number.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa ambos campos.")

# Función para verificar si un contacto ya existe
def contact_exists(name):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            contacts = file.readlines()
            for line in contacts:
                contact_name, _ = line.strip().split("!")
                if contact_name == name:
                    return True
    return False

# Función para leer todos los contactos
def read_contacts():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            contacts = file.readlines()
        if contacts:
            contacts_list = "\n".join([c.replace("!", " - ") for c in contacts])
            # Crear ventana secundaria para mostrar contactos
            contacts_window = tk.Toplevel(root)
            contacts_window.title("Lista de Contactos")
            contacts_window.geometry("300x400")
            
            text_area = tk.Text(contacts_window, wrap=tk.WORD, font=FONT)
            scrollbar = ttk.Scrollbar(contacts_window, command=text_area.yview)
            text_area.configure(yscrollcommand=scrollbar.set)
            
            text_area.insert(tk.END, contacts_list)
            text_area.config(state=tk.DISABLED)
            
            text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        else:
            messagebox.showinfo("Contactos", "No hay contactos guardados.")
    else:
        messagebox.showwarning("Advertencia", "No hay contactos guardados.")

# Función para actualizar un contacto
def update_contact():
    name = entry_name.get()
    new_number = entry_number.get()
    
    if name and new_number:
        updated = False
        lines = []
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
        
        with open(file_path, 'w') as file:
            for line in lines:
                contact_name, contact_number = line.strip().split("!")
                if contact_name == name:
                    file.write(f"{contact_name}!{new_number}\n")
                    updated = True
                else:
                    file.write(line)
        
        if updated:
            messagebox.showinfo("Éxito", "Contacto actualizado.")
        else:
            messagebox.showwarning("Advertencia", "El contacto no existe.")
        
        entry_name.delete(0, tk.END)
        entry_number.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa ambos campos.")

# Función para eliminar un contacto
def delete_contact():
    name = entry_name.get()
    
    if name:
        deleted = False
        lines = []
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
        
        with open(file_path, 'w') as file:
            for line in lines:
                contact_name, contact_number = line.strip().split("!")
                if contact_name != name:
                    file.write(line)
                else:
                    deleted = True
        
        if deleted:
            messagebox.showinfo("Éxito", "Contacto eliminado.")
        else:
            messagebox.showwarning("Advertencia", "El contacto no existe.")
        
        entry_name.delete(0, tk.END)
        entry_number.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un nombre.")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Contactos")
root.geometry("400x300")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Frame principal
main_frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

# Campos de entrada
input_frame = tk.Frame(main_frame, bg=BG_COLOR)
input_frame.pack(pady=(0, 15))

tk.Label(input_frame, text="Nombre:", bg=BG_COLOR, font=FONT).grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = ttk.Entry(input_frame, font=FONT, width=25)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Número:", bg=BG_COLOR, font=FONT).grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_number = ttk.Entry(input_frame, font=FONT, width=25)
entry_number.grid(row=1, column=1, padx=5, pady=5)

# Frame para los botones
button_frame = tk.Frame(main_frame, bg=BG_COLOR)
button_frame.pack(pady=10)

# Botones
style = ttk.Style()
style.configure('TButton', padding=6, font=FONT)

ttk.Button(button_frame, text="Create", command=create_contact).grid(row=0, column=0, padx=10, pady=10, ipadx=10)
ttk.Button(button_frame, text="Read", command=read_contacts).grid(row=0, column=1, padx=10, pady=10, ipadx=10)
ttk.Button(button_frame, text="Update", command=update_contact).grid(row=1, column=0, padx=10, pady=10)
ttk.Button(button_frame, text="Delete", command=delete_contact).grid(row=1, column=1, padx=10, pady=10)

# Iniciar el bucle principal
root.mainloop()


