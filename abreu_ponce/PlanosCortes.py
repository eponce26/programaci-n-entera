import pulp
import numpy as np

class ProblemaMaximizacion:
    def __init__(self):
        # Crear el problema de maximización
        self.prob = pulp.LpProblem("Ejemplo_Cortes_Gomory", pulp.LpMaximize)
        self.variables = []

    def definir_funcion_objetivo(self):
        # Solicitar al usuario los coeficientes de la función objetivo
        print("Ingrese los coeficientes de la función objetivo:")
        coeficientes = list(map(float, input("Coeficientes (separados por espacios): ").split()))
        
        # Definir variables continuas para la relajación inicial
        self.variables = [pulp.LpVariable(f"x{i+1}", lowBound=0) for i in range(len(coeficientes))]
        
        # Definir la función objetivo
        self.prob += sum(coeficientes[i] * self.variables[i] for i in range(len(coeficientes))), "Función Objetivo"

    def definir_restricciones(self):
        # Solicitar al usuario el número de restricciones
        num_restricciones = int(input("Ingrese el número de restricciones: "))
        
        # Definir las restricciones
        for i in range(num_restricciones):
            print(f"Ingrese los coeficientes de la restricción {i + 1}:")
            coef_restriccion = list(map(float, input("Coeficientes (separados por espacios): ").split()))
            limite = float(input("Ingrese el límite de la restricción: "))
            self.prob += sum(coef_restriccion[j] * self.variables[j] for j in range(len(coef_restriccion))) <= limite, f"Restriccion_{i + 1}"

    def agregar_corte(self, tableau):
        filas, columnas = tableau.shape
        for i in range(filas):
            if not np.isclose(tableau[i, -1], np.floor(tableau[i, -1])):  # Verificar si la solución es entera
                corte = np.floor(tableau[i, -1]) - tableau[i, -1]
                for j in range(columnas - 1):
                    if not np.isclose(tableau[i, j], 0):
                        corte += (tableau[i, j] - np.floor(tableau[i, j])) * self.variables[j]
                self.prob += corte <= 0, f"Corte_Gomory_{i}"
                return True  # Corte añadido
        return False  # No se necesita corte

    def resolver(self):
        # Resolver el problema relajado inicialmente
        self.prob.solve()
        print(f"Estado de la solución: {pulp.LpStatus[self.prob.status]}")
        print(", ".join([f"{var.name} = {var.varValue}" for var in self.variables]))

        # Tabla simplex (esto es un ejemplo, debe ser adaptado)
        tableau = np.array([
            [6, 4, 0, 24],  # Restricción 1
            [1, 2, 0, 6],   # Restricción 2
            [-1, 1, 0, 1]   # Restricción 3
        ])

        # Aplicar el algoritmo de cortes iterativamente
        while True:
            if not self.agregar_corte(tableau):
                break
            self.prob.solve()
            print(f"Estado de la solución: {pulp.LpStatus[self.prob.status]}")
            print(", ".join([f"{var.name} = {var.varValue}" for var in self.variables]))

        # Mostrar la solución final
        print("Solución óptima entera:", ", ".join([f"{var.name} = {var.varValue}" for var in self.variables]))

# Uso de la clase
if __name__ == "__main__":
    problema = ProblemaMaximizacion()
    problema.definir_funcion_objetivo()
    problema.definir_restricciones()
    problema.resolver()
