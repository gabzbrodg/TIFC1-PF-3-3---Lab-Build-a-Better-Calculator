def main():
  print("Hello learners!")
  
def addmultiplenumbers(numbers):
    # Suma todos los números de la lista
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    # Multiplica todos los números de la lista
    if not numbers:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    # Verifica si es par y entero (divisible por 2 con residuo 0)
    return num % 2 == 0

def isitaninteger(num):
    # Verifica si el tipo de dato es un entero
    return isinstance(num, int)

def main():
    print("--- Calculadora Mejorada ---")
    # Ejemplo de uso interactivo
    nums = [2, 4, 6]
    print(f"Suma de {nums}: {addmultiplenumbers(nums)}")
    print(f"¿Es 10 un entero?: {isitaninteger(10)}")

if __name__ == "__main__":
    main()

if __name__=="__main__":
  main()