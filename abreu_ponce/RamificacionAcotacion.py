from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, PULP_CBC_CMD

class ProblemaProgramacionEntera:
    def __init__(self):
        # Crear el problema de maximización
        self.problema = LpProblem("Ejemplo_Programacion_Entera", LpMaximize)
        # Inicializar las variables de decisión
        self.x = LpVariable('x', lowBound=0, cat='Integer')
        self.y = LpVariable('y', lowBound=0, cat='Integer')
        # Almacenar restricciones
        self.restricciones = []
        # Solicitar y configurar los datos del usuario
        self.obtener_datos_usuario()
        self.configurar_problema()

    def obtener_datos_usuario(self):
        # Pedir coeficientes de la función objetivo
        self.coef_x = float(input("Ingrese el coeficiente de x en la función objetivo: "))
        self.coef_y = float(input("Ingrese el coeficiente de y en la función objetivo: "))
        
        # Pedir el número de restricciones
        num_restricciones = int(input("Ingrese el número de restricciones: "))
        
        # Pedir los valores para cada restricción
        print("\nIngrese los valores para cada restricción (coeficientes de x y y, y el límite):")
        for i in range(1, num_restricciones + 1):
            coef_x = float(input(f"Ingrese el coeficiente de x para la restricción {i}: "))
            coef_y = float(input(f"Ingrese el coeficiente de y para la restricción {i}: "))
            limite = float(input(f"Ingrese el valor límite para la restricción {i}: "))
            signo = input("Ingrese '<=' para menor o igual, '>=' para mayor o igual: ")
            
            # Agregar cada restricción como una tupla (coef_x, coef_y, limite, signo)
            self.restricciones.append((coef_x, coef_y, limite, signo))

    def configurar_problema(self):
        # Definir la función objetivo
        self.problema += self.coef_x * self.x + self.coef_y * self.y, "Función Objetivo"
        
        # Definir las restricciones basadas en la entrada del usuario
        for i, (coef_x, coef_y, limite, signo) in enumerate(self.restricciones, start=1):
            if signo == "<=":
                self.problema += coef_x * self.x + coef_y * self.y <= limite, f"Restriccion_{i}"
            elif signo == ">=":
                self.problema += coef_x * self.x + coef_y * self.y >= limite, f"Restriccion_{i}"
            else:
                print(f"Signo no válido en la restricción {i}. Se omite esta restricción.")

    def resolver(self):
        # Resolver el problema usando el solucionador CBC
        self.problema.solve(PULP_CBC_CMD(msg=True))

    def mostrar_resultados(self):
        # Mostrar el estado de la solución
        print(f"Estado de la solución: {LpStatus[self.problema.status]}")
        # Mostrar los valores óptimos de las variables
        print(f"x = {self.x.varValue}")
        print(f"y = {self.y.varValue}")
        # Mostrar el valor óptimo de la función objetivo
        print(f"Valor óptimo de Z = {self.problema.objective.value()}")

# Crear una instancia del problema, resolverlo y mostrar resultados
problema = ProblemaProgramacionEntera()
problema.resolver()
problema.mostrar_resultados()
