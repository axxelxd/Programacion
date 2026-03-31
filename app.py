import tkinter as tk

# Función para calcular el IMC
def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())

        imc = peso / (altura ** 2)

        resultado.config(text=f"IMC: {imc:.2f}")

        # Clasificación
        if imc < 18.5:
            estado.config(text="Bajo peso")
        elif imc < 25:
            estado.config(text="Peso normal")
        elif imc < 30:
            estado.config(text="Sobrepeso")
        else:
            estado.config(text="Obesidad")

    except:
        resultado.config(text="Error: datos inválidos")
        estado.config(text="")

ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("300x250")

tk.Label(ventana, text="Peso (kg):").pack()
entrada_peso = tk.Entry(ventana)
entrada_peso.pack()

tk.Label(ventana, text="Altura (m):").pack()
entrada_altura = tk.Entry(ventana)
entrada_altura.pack()

tk.Button(ventana, text="Calcular IMC", command=calcular_imc).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

estado = tk.Label(ventana, text="")
estado.pack()

ventana.mainloop()