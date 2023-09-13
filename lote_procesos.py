from proceso import Proceso


class Lote:
    def __init__(self, num_lote):
        self.__procesos = []
        self.__numero_de_lote = num_lote
        self.__tiempo_maximo = 0
        self.__tiempo_transcurrido = 0

    def agregar_proceso(self, proceso) -> bool:
        if len(self.__procesos) < 5:
            self.__procesos.append(proceso)
            self.__tiempo_maximo += int(proceso.get_tiempo())
            return True
        return False

    def __str__(self) -> str:
        return "\nNumero de lote " + str(self.__numero_de_lote)

    def isvoid(self) -> bool:
        return len(self.__procesos) == 0

    def saca_proceso(self) -> Proceso:
        if self.__procesos:
            return self.__procesos.pop(0)
        else:
            return None

    def get_num_lote(self):
        return self.__numero_de_lote

    def get_tiempo_maximo(self):
        return self.__tiempo_maximo

    def get_tiempo_transcurrido(self):
        return self.__tiempo_transcurrido

    def transcurre_tiempo(self):
        self.__tiempo_transcurrido += 1

    def get_procesos(self):
        return self.__procesos
