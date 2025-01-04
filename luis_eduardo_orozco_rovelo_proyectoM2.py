import random

def obtener_palabra(mensaje):
    while True:
        palabra = input(mensaje)
        if len(palabra) >= 4 and len(palabra) <= 8:
            return palabra
        elif len(palabra) < 4:
            print("Hacen falta letras. Solo tiene", len(palabra), "letras.")
        else:
            print("Sobran letras. Tiene", len(palabra), "letras.")

def generar_contraseña(palabras):
    contraseña = ""
    for palabra in palabras:
        letra1 = random.choice(palabra)
        letra2 = random.choice(palabra)
        contraseña += letra1 + letra2
    return contraseña

def main():
    palabras = []
    for i in range(3):
        palabra = obtener_palabra(f"Introduce la palabra {i+1}: ")
        palabras.append(palabra)
    
    contraseña = generar_contraseña(palabras)
    
    print("La contraseña es:", contraseña)
    
    while True:
        contraseña_usuario = input("Introduce la contraseña: ")
        if len(contraseña_usuario) < len(contraseña):
            print("Faltan", len(contraseña) - len(contraseña_usuario), "caracteres")
        elif len(contraseña_usuario) > len(contraseña):
            print("Sobran", len(contraseña_usuario) - len(contraseña), "caracteres")
        elif contraseña_usuario == contraseña:
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorrecta")

if __name__ == "__main__":
    main()