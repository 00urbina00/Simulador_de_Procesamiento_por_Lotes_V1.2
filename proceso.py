class Proceso:
    def __init__(self, operador, operando_a, operando_b, tiempo, numero_proceso) -> None:
        self.__operacion_realizar = operador
        self.__operando_a = operando_a
        self.__operando_b = operando_b
        self.__tiempo_medio_estimado = int(tiempo)
        self.__tiempo_transcurrido = 0
        self.__tiempo_restante = int(tiempo)
        self.__resultado = 0.0
        self.__id = numero_proceso
        self.__terminado = False

    def set_operacion(self, operacion):
        self.__operacion_realizar = operacion

    def set_operando_a(self, operando_a):
        self.__operando_a = operando_a

    def set_operando_b(self, operando_b):
        self.__operando_b = operando_b

    def set_tiempo_max(self, tiempo):
        self.__tiempo_medio_estimado = tiempo

    def set_id(self, numero_proceso):
        self.__id = numero_proceso

    def terminado(self):
        return self.__terminado

    def set_terminado(self):
        self.__terminado = True

    def set_resultado(self, res):
        self.__resultado = res

    def set_tiempo_transcurrido(self, tiempo):
        self.__tiempo_transcurrido = tiempo

    def get_operacion(self) -> str:
        return self.__operacion_realizar

    def get_operando_a(self):
        return self.__operando_a

    def get_operando_b(self):
        return self.__operando_b

    def get_tiempo(self) -> int:
        return int(self.__tiempo_medio_estimado)

    def get_id(self) -> int:
        return self.__id

    def get_resultado(self):
        return self.__resultado

    def get_tiempo_transcurrido(self):
        return self.__tiempo_transcurrido

    def segundo_transcurrido(self):
        self.__tiempo_transcurrido += 1
        if self.__tiempo_restante > 0:
            self.__tiempo_restante -= 1

    def get_tiempo_restante(self) -> str:
        return str(self.__tiempo_restante)

    def ejecutar(self):
        if self.__operacion_realizar == '+':
            self.__resultado = self.__operando_a + self.__operando_b
        elif self.__operacion_realizar == '-':
            self.__resultado = self.__operando_a - self.__operando_b
        elif self.__operacion_realizar == '*':
            self.__resultado = self.__operando_a * self.__operando_b
        elif self.__operacion_realizar == '/':
            if self.__operando_b != 0:
                self.__resultado = round(self.__operando_a / self.__operando_b)
            else:
                print("Error: DIV0")
                self.__resultado = 0
        elif self.__operacion_realizar == '%':
            self.__resultado = round(((self.__operando_a / 100) * self.__operando_b), 2)
        elif self.__operacion_realizar == '%%':
            self.__resultado = self.__operando_a % self.__operando_b
