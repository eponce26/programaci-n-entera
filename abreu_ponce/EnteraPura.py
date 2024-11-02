from pulp import LpMaximize, LpProblem, LpVariable, LpStatus

class IntegerProgramming:
    def __init__(self):
        # Crear un problema de maximización
        self.prob = LpProblem("Programacion_Entera_Pura", LpMaximize)
        self.decision_vars = {}
        self.create_decision_variables()

    def create_decision_variables(self):
        # Definir las variables de decisión (enteras)
        self.decision_vars['x'] = LpVariable('x', lowBound=0, cat='Integer')
        self.decision_vars['y'] = LpVariable('y', lowBound=0, cat='Integer')

    def solicitar_flotante(self, mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: ingrese un número válido.")

    def set_objective(self):
        coef_x = self.solicitar_flotante("Ingrese el coeficiente de x en la función objetivo: ")
        coef_y = self.solicitar_flotante("Ingrese el coeficiente de y en la función objetivo: ")
        # Definir la función objetivo
        self.prob += coef_x * self.decision_vars['x'] + coef_y * self.decision_vars['y'], "Función Objetivo"

    def add_constraints(self):
        for i in range(1, 3):  # Para dos restricciones
            print(f"Ingrese los coeficientes para la restricción {i} (formato: a*x + b*y <= c):")
            a = self.solicitar_flotante(f"Coeficiente de x en la restricción {i}: ")
            b = self.solicitar_flotante(f"Coeficiente de y en la restricción {i}: ")
            rhs = self.solicitar_flotante(f"Lado derecho (c) de la restricción {i}: ")
            # Definir la restricción
            self.prob += a * self.decision_vars['x'] + b * self.decision_vars['y'] <= rhs, f"Restriccion_{i}"

    def solve(self):
        # Resolver el problema
        self.prob.solve()
        self.display_results()

    def display_results(self):
        # Mostrar el estado de la solución
        print(f"Estado de la solución: {LpStatus[self.prob.status]}")
        # Mostrar los valores óptimos de las variables
        for var_name, var in self.decision_vars.items():
            print(f"{var_name} = {var.varValue:.2f}")  # Formato a dos decimales
        # Mostrar el valor óptimo de la función objetivo
        print(f"Valor óptimo de Z = {self.prob.objective.value():.2f}")  # Formato a dos decimales

if __name__ == "__main__":
    ip = IntegerProgramming()
    ip.set_objective()
    ip.add_constraints()
    ip.solve()
