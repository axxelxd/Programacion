import tkinter as tk

# Variables para guardar usuario y contraseña
usuario_guardado = ""
password_guardado = ""

def evaluar_password(password):
    if len(password) < 8:
        return "débil"
    elif (any(c.islower() for c in password) and
          any(c.isupper() for c in password) and
          any(c.isdigit() for c in password)):
        return "fuerte"
    else:
        return "bueno"

def verificar_password(*args):
    password = entrada_password.get()
    nivel = evaluar_password(password)
    resultado.config(text=nivel)

def registrar():
    global usuario_guardado, password_guardado
    
    usuario_guardado = entrada_usuario.get()
    password_guardado = entrada_password.get()
    
    if len(password_guardado) >= 8:
        estado.config(text="Usuario creado correctamente ✅")
    else:
        estado.config(text="La contraseña debe tener al menos 8 caracteres ❌")

def login():
    usuario = entrada_usuario.get()
    password = entrada_password.get()
    
    if usuario == usuario_guardado and password == password_guardado:
        estado.config(text="Acceso aceptado ✅")
    else:
        estado.config(text="Datos incorrectos ❌")

# Ventana
ventana = tk.Tk()
ventana.title("Sistema de Autenticación")
ventana.geometry("400x300")

# Usuario
tk.Label(ventana, text="Usuario").pack(pady=5)
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()

# Contraseña
tk.Label(ventana, text="Contraseña").pack(pady=5)
entrada_password = tk.Entry(ventana, show="*")
entrada_password.pack()

# Mensaje ayuda
tk.Label(ventana, text="Crea con al menos 8 caracteres").pack()

# Nivel de seguridad
resultado = tk.Label(ventana, text="")
resultado.pack(pady=5)

# Detectar escritura
password_var = tk.StringVar()
entrada_password.config(textvariable=password_var)
password_var.trace("w", verificar_password)

# Botones
tk.Button(ventana, text="Crear usuario", command=registrar).pack(pady=5)
tk.Button(ventana, text="Entrar", command=login).pack(pady=5)

# Estado
estado = tk.Label(ventana, text="")
estado.pack(pady=10)

ventana.mainloop()