from pulp import LpMinimize, LpProblem, LpVariable, LpStatus

class ProblemaProgramacionBinaria:
    def __init__(self):
        self.prob = LpProblem("Programacion_Binaria", LpMinimize)
        self.decision_variables = {}
    
    def definir_variables(self):
        # Definir las variables de decisión (binarias)
        self.decision_variables['x'] = LpVariable('x', cat='Binary')
        self.decision_variables['y'] = LpVariable('y', cat='Binary')
        self.decision_variables['z'] = LpVariable('z', cat='Binary')

    def ingresar_coeficientes_objetivo(self):
        self.coef_x = self.get_integer_input("Ingrese el coeficiente de x en la función objetivo: ")
        self.coef_y = self.get_integer_input("Ingrese el coeficiente de y en la función objetivo: ")
        self.coef_z = self.get_integer_input("Ingrese el coeficiente de z en la función objetivo: ")

        # Definir la función objetivo
        self.prob += (self.coef_x * self.decision_variables['x'] + 
                       self.coef_y * self.decision_variables['y'] + 
                       self.coef_z * self.decision_variables['z']), "Función Objetivo"

    def ingresar_restricciones(self):
        print("Ingrese los coeficientes para la primera restricción (formato: a*x + b*y >= c):")
        a1 = self.get_integer_input("Coeficiente de x en la primera restricción: ")
        b1 = self.get_integer_input("Coeficiente de y en la primera restricción: ")
        rhs1 = self.get_integer_input("Lado derecho (c) de la primera restricción: ")

        print("Ingrese los coeficientes para la segunda restricción (formato: a*y + b*z >= c):")
        a2 = self.get_integer_input("Coeficiente de y en la segunda restricción: ")
        b2 = self.get_integer_input("Coeficiente de z en la segunda restricción: ")
        rhs2 = self.get_integer_input("Lado derecho (c) de la segunda restricción: ")

        # Definir las restricciones
        self.prob += a1 * self.decision_variables['x'] + b1 * self.decision_variables['y'] >= rhs1, "Restriccion_1"
        self.prob += a2 * self.decision_variables['y'] + b2 * self.decision_variables['z'] >= rhs2, "Restriccion_2"

    def resolver(self):
        self.prob.solve()
        self.mostrar_resultados()

    def mostrar_resultados(self):
        # Mostrar el estado de la solución
        print(f"Estado de la solución: {LpStatus[self.prob.status]}")

        # Mostrar los valores óptimos de las variables
        for var in self.decision_variables.values():
            print(f"{var.name} = {var.varValue}")

        # Mostrar el valor óptimo de la función objetivo
        print(f"Valor óptimo de Z = {self.prob.objective.value()}")

    @staticmethod
    def get_integer_input(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    problema = ProblemaProgramacionBinaria()
    problema.definir_variables()
    problema.ingresar_coeficientes_objetivo()
    problema.ingresar_restricciones()
    problema.resolver()
