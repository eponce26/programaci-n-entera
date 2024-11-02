from pulp import LpMaximize, LpProblem, LpVariable, LpStatus

class ProblemaMochila:
    def __init__(self):
        self.n = 0
        self.pesos = []
        self.valores = []
        self.capacidad = 0
        self.x = []

    def solicitar_numero(self, mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: por favor ingrese un número válido.")

    def ingresar_datos(self):
        print("\n--- Paso 1: Ingreso de datos ---")
        self.n = int(self.solicitar_numero("Ingrese el número de objetos: "))
        
        for i in range(self.n):
            peso = self.solicitar_numero(f"Ingrese el peso del objeto {i + 1}: ")
            valor = self.solicitar_numero(f"Ingrese el valor del objeto {i + 1}: ")
            self.pesos.append(peso)
            self.valores.append(valor)
        
        self.capacidad = self.solicitar_numero("Ingrese la capacidad máxima de la mochila: ")
        
        if self.capacidad <= 0:
            print("Error: La capacidad de la mochila debe ser un número positivo.")
            return False
        return True

    def resolver(self):
        # Crear el problema de maximización
        problema_mochila = LpProblem("Problema_de_la_Mochila", LpMaximize)
        
        # Definir las variables de decisión
        self.x = [LpVariable(f"x_{i+1}", cat='Binary') for i in range(self.n)]

        # Definir la función objetivo
        problema_mochila += sum(self.valores[i] * self.x[i] for i in range(self.n)), "Valor_total"

        # Definir la restricción de capacidad de la mochila
        problema_mochila += sum(self.pesos[i] * self.x[i] for i in range(self.n)) <= self.capacidad, "Capacidad_mochila"

        # Resolver el problema
        problema_mochila.solve()

        # Mostrar estado de la solución
        print(f"\nEstado de la solución: {LpStatus[problema_mochila.status]}")

        if LpStatus[problema_mochila.status] != "Optimal":
            print("No se encontró una solución óptima. Revise los datos ingresados.")
            return

        # Mostrar los objetos seleccionados
        print("\n--- Objetos seleccionados ---")
        for i in range(self.n):
            if self.x[i].varValue == 1:
                print(f"Objeto {i+1}: Seleccionado (Peso: {self.pesos[i]}, Valor: {self.valores[i]})")

        # Calcular y mostrar el valor total y el peso total
        valor_total = sum(self.valores[i] * self.x[i].varValue for i in range(self.n))
        peso_total = sum(self.pesos[i] * self.x[i].varValue for i in range(self.n))
        print(f"\nValor total en la mochila: {valor_total}")
        print(f"Peso total en la mochila: {peso_total}")

# Llamar a la función para resolver el problema
if __name__ == "__main__":
    problema = ProblemaMochila()
    if problema.ingresar_datos():
        problema.resolver()