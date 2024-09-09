# Función para calcular el área de un rectángulo
def rect_area(base, altura):
    result = base * altura
    return result

# Función para calcular el área de un triángulo
def tri_area(base, altura):
    resulta = 0.5 * base * altura
    return resulta

# Función principal
if __name__ == "__main__":
    baser = float(input("base del rectangulo:"))
    alturar = float(input("altura del rectangulo:"))
    rect_area = rect_area(baser, alturar)
    print("Área del rectángulo:", rect_area)

    baset = float(input("base del rectangulo:"))
    alturat = float(input("altura del rectangulo:"))
    tri_area = tri_area(baset, alturat)
    print("Área del triángulo:", tri_area)


