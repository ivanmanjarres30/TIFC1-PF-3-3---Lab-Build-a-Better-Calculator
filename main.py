def addmultiplenumbers(numbers):

    total = 0
    for num in numbers:
        total += num
    return total


def multiplymultiplenumbers(numbers):
    if not numbers:
        return 0
    
    result = numbers[0]
    for num in numbers[1:]:
        result *= num
    return result


def isiteven(num):
    if isitaninteger(num):
        return int(num) % 2 == 0
    return False


def isitaninteger(num):
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return num.is_integer()
    return False


def main():
    print("Hello learners!")
    
    lista_pruebas = [2, 3, 4]
    
    print("\n--- Pruebas de las funciones ---")
    print("\n--- Prueba SUMA ---")
    print(f"Suma de {lista_pruebas}: {addmultiplenumbers(lista_pruebas)}") 
    
    print("\n--- Prueba MULTIPLICACIÓN ---")
    print(f"Multiplicación de {lista_pruebas}: {multiplymultiplenumbers(lista_pruebas)}") 
    
    print("\n--- Prueba NÚMERO ENTERO ---")
    print(f"¿Es 4 un número entero? {isitaninteger(4)}") 
    print(f"¿Es 4.5 un número entero? {isitaninteger(4.5)}") 
    
    print("\n--- Prueba NÚMERO PAR ---")
    print(f"¿Es 4 un número par? {isiteven(4)}") 
    print(f"¿Es 5 un número par? {isiteven(5)}")  
    


if __name__ == "__main__":
    main()