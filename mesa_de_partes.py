def validar_dni(dni):
    """Valida que el DNI tenga exactamente 8 dígitos numéricos."""
    if len(dni) == 8 and dni.isdigit():
        return True
    return False


def registrar_expediente():
    print("\n--- REGISTRO DE NUEVO EXPEDIENTE ---")
    # 1. Ingreso y validación del DNI del ciudadano
    dni = input("Ingrese el DNI del ciudadano (8 dígitos): ")
    while not validar_dni(dni):
        print("DNI inválido. Debe contener exactamente 8 números.")
        dni = input("Ingrese el DNI del ciudadano (8 dígitos): ")

    # 2. Ingreso del código de trámite
    codigo_tramite = input("Ingrese el código de trámite (ej. TR-001): ")
    # 3. Ingreso del nombre del solicitante
    nombre = input("Ingrese el nombre completo del solicitante: ")
    # 4. Ingreso de la descripción del expediente
    descripcion = input("Ingrese la descripción breve del documento: ")

    # Estructuramos los datos en una lista temporal para este registro
    expediente = [codigo_tramite, dni, nombre, descripcion]
    print("\n¡Expediente registrado exitosamente en memoria!")
    return expediente

#Agregado-----------------------------------------------------------------

def buscar_expediente(lista_general):
        # Busca un expediente comparando su código con el ingresado por el usuario.
    codigo = input("Ingrese el codigo del expediente: ")

    encontrado = False

    for expediente in lista_general:
        if expediente[0] == codigo:
            print("Expediente encontrado")
            print("Codigo:", expediente[0])
            print("DNI:", expediente[1])
            print("Nombre:", expediente[2])
            print("Descripcion:", expediente[3])

            encontrado = True

    if encontrado == False:
        print("No se encontro el expediente")


def ordenar_expedientes(lista_general):
    lista_general.sort(key=lambda expediente: expediente[0])

    print("\n- EXPEDIENTES ORDENADOS POR CÓDIGO -")
    for expediente in lista_general:
        print(
            f"Código: {expediente[0]} | DNI: {expediente[1]} | "
            f"Nombre: {expediente[2]} | Descripción: {expediente[3]}"
        )

#--------------------------------------------------------------------------
# Menú principal interactivo básico con estructura repetitiva y condicional

def main():
    lista_general = []
    opcion = ""

    while opcion != "5":
        print("\n========================================")
        print(" MUNICIPALIDAD - MESA DE PARTES ")
        print("========================================")
        print("1. Registrar nuevo expediente")
        print("2. Mostrar expedientes registrados")
        print("3. Buscar expediente por codigo")
        print("4. Ordenar expedientes por código")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            nuevo = registrar_expediente()
            lista_general.append(nuevo)
        elif opcion == "2":
            if len(lista_general) == 0:
                print("\nNo hay expedientes registrados todavía.")
            else:
                print("\n--- LISTA DE EXPEDIENTES ---")
                # Bucle simple para recorrer la lista de expedientes
                for i in range(len(lista_general)):
                    print(
                        f"Expediente {i+1}: Código: {lista_general[i][0]} | DNI: {lista_general[i][1]} | "
                        f"Nombre: {lista_general[i][2]}"
                    )
        elif opcion == "3":
            if len(lista_general) == 0:
                print("\nNo hay expedientes registrados todavía.")
            else:
                buscar_expediente(lista_general)
        elif opcion == "4":
            if len(lista_general) == 0:
                print("\nNo hay expedientes registrados todavía.")
            else:
                ordenar_expedientes(lista_general)
        elif opcion == "5":
            print("\nSaliendo del sistema de mesa de partes. ¡Hasta luego!")
        else:
            print("\nOpción no válida. Por favor, elija entre 1 y 5.")


# Ejecución del programa
if __name__ == "__main__":
    main()