import tkinter as tk
from transformers import pipeline
from tkinter import PhotoImage

# Definir funciones
# ----------------------------------------------------
def procesamiento(contexto, pregunta):
    pipe = pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2")
    respuesta = pipe(question=pregunta, context=contexto)
    return respuesta

def obtener_respuesta_y_mostrar_nota():
    global pregunta, respuesta, contenido

    # Mostrar nota seleccionada
    indice = lista.curselection()
    if indice:
        elemento_seleccionado.set(lista.get(indice))
        i = indice[0] + 1
        archivo_entrada = f"otas_clinicas_corpus_distemist/distemist_test_{i}.txt"
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        cuadro_texto.delete(1.0, tk.END)  # Limpiar el cuadro de texto
        cuadro_texto.insert(tk.END, contenido)  # Insertar el contenido en el cuadro de texto

    # Obtener respuesta
    pregunta = cuadro_pregunta.get("1.0", "end-1c")  # Obtener el contenido del cuadro_pregunta
    respuesta = procesamiento(contenido, pregunta)
    cuadro_texto.delete(1.0, tk.END)  # Limpiar el cuadro de texto
    cuadro_texto.insert(tk.END, contenido + "\n" + "La respuesta es: " + respuesta['answer'])  # Insertar la respuesta en el cuadro de texto

# Crear la ventana principal
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Interfaz PLN")
    ventana.geometry("600x600")
    imagen = PhotoImage(file="michophone.png")

    # Crear una Lista
    lista = tk.Listbox(ventana)
    lista.pack(padx=20, pady=20)

    elementos = ["nota_{}".format(i) for i in range(1, 3001)]
    for elemento in elementos:
        lista.insert(tk.END, elemento)

    elemento_seleccionado = tk.StringVar()
    etiqueta_elemento = tk.Label(ventana, textvariable=elemento_seleccionado)
    etiqueta_elemento.pack()

    contenedor_botones = tk.Frame(ventana)
    contenedor_botones.pack()

    boton_obtener_respuesta_y_mostrar_nota = tk.Button(contenedor_botones, text="Obtener Respuesta y Mostrar Nota", command=obtener_respuesta_y_mostrar_nota)
    boton_obtener_respuesta_y_mostrar_nota.pack(side=tk.LEFT, padx=10)

    boton = tk.Button(contenedor_botones, image=imagen, text=" ")  # Eliminamos la asociación con la función toggle_recording
    boton.pack(side=tk.LEFT)

    contenedor_texto = tk.Frame(ventana)
    contenedor_texto.pack(pady=10)

    cuadro_pregunta = tk.Text(contenedor_texto, width=40, height=1)
    cuadro_pregunta.pack(padx=20, pady=10)

    etiqueta_resultado = tk.Label(contenedor_texto, text="")
    etiqueta_resultado.pack()

    cuadro_texto = tk.Text(contenedor_texto, height=10, width=40)
    cuadro_texto.pack(pady=10)

    ventana.mainloop()
