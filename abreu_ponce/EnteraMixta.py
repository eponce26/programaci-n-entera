from pulp import LpMaximize, LpProblem, LpVariable, LpStatus

class ProgramacionEnteraMixta:
    def __init__(self):
        # Crear un problema de maximización
        self.prob = LpProblem("Programacion_Entera_Mixta", LpMaximize)

        # Definir las variables de decisión
        self.x = LpVariable('x', lowBound=0, cat='Integer')  # Entera
        self.y = LpVariable('y', lowBound=0, cat='Continuous')  # Continua

    def solicitar_flotante(self, mensaje):
        """Solicita un número flotante al usuario."""
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: ingrese un número válido.")

    def definir_funcion_objetivo(self):
        """Define la función objetivo a partir de la entrada del usuario."""
        coef_x = self.solicitar_flotante("Ingrese el coeficiente de x en la función objetivo: ")
        coef_y = self.solicitar_flotante("Ingrese el coeficiente de y en la función objetivo: ")
        self.prob += coef_x * self.x + coef_y * self.y, "Función Objetivo"

    def definir_restricciones(self):
        """Permite al usuario definir las restricciones."""
        num_restricciones = int(self.solicitar_flotante("Ingrese el número de restricciones: "))
        for i in range(num_restricciones):
            print(f"Ingresando restricción {i + 1}:")
            a = self.solicitar_flotante("Coeficiente de x en la restricción: ")
            b = self.solicitar_flotante("Coeficiente de y en la restricción: ")
            rhs = self.solicitar_flotante("Lado derecho (c) de la restricción: ")
            self.prob += a * self.x + b * self.y <= rhs, f"Restriccion_{i + 1}"

    def resolver(self):
        """Resuelve el problema y muestra los resultados."""
        self.prob.solve()
        print(f"Estado de la solución: {LpStatus[self.prob.status]}")
        print(f"x = {self.x.varValue}")
        print(f"y = {self.y.varValue}")
        print(f"Valor óptimo de Z = {self.prob.objective.value()}")

# Uso de la clase
if __name__ == "__main__":
    modelo = ProgramacionEnteraMixta()
    modelo.definir_funcion_objetivo()
    modelo.definir_restricciones()
    modelo.resolver()
