import json


ARCHIVO = "persistencia.json"


def pedir_datos():
    """Solicita y valida los datos del usuario."""

    nombre = input("¿Cuál es su nombre? ").strip()
    carro = input("¿Qué carro usó? ").strip()

    while True:
        try:
            kilometros = float(input("¿Cuántos kilómetros recorrió? "))

            if kilometros < 0:
                print(" Los kilómetros no pueden ser negativos.")
                continue

            break

        except ValueError:
            print(" Por favor, ingrese un número válido.")

    return {
        "nombre": nombre,
        "carro": carro,
        "kilometros": kilometros
    }


def guardar_datos(datos):
    """Guarda los datos en un archivo JSON."""

    try:
        with open(ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        print(f"\n Datos guardados correctamente en '{ARCHIVO}'.")

    except OSError as error:
        print(f" No se pudieron guardar los datos: {error}")


def registrar_y_guardar():
    """Registra los datos y los guarda en el archivo."""

    print("=== REGISTRO DE RECORRIDO ===\n")

    datos = pedir_datos()
    guardar_datos(datos)


if __name__ == "__main__":
    registrar_y_guardar()
