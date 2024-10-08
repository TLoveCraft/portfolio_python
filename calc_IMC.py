import tkinter as tk
# Thierry Araujo Mendes

def calcular_imc():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso / (altura ** 2)

    # Aqui temos um conjunto de If para verificarmos a saude do usuario
    if imc < 18.5:
        classificacao["text"] = "Abaixo do peso. Consulte um nutricionista."
    elif 18.5 <= imc < 25:
        classificacao["text"] = "Peso normal. Parabéns!"
    elif 25 <= imc < 30:
        classificacao["text"] = "Sobrepeso. Consulte um profissional de saúde."
    else:
        classificacao["text"] = "Obesidade. Procure um médico."

   
    resultado["text"] = f"Seu IMC é: {imc:.2f}"

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.state("zoomed")

label_peso = tk.Label(janela, text="Peso (kg):")
entry_peso = tk.Entry(janela)

label_altura = tk.Label(janela, text="Altura (m):")
entry_altura = tk.Entry(janela)

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)

resultado = tk.Label(janela, text="")
classificacao = tk.Label(janela, text="")

label_peso.pack()
entry_peso.pack()
label_altura.pack()
entry_altura.pack()
botao_calcular.pack()
resultado.pack()
classificacao.pack()

janela.mainloop()