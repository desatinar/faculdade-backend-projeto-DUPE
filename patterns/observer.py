from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self, duplicata):
        """Método que será chamado quando houver notificação"""
        pass

class Notificador:
    def __init__(self):
        self._observadores = []

    def inscrever(self, observador: Observador):
        self._observadores.append(observador)
    
    def notificar_todos(self, duplicata):
        for obs in self._observadores:
            obs.atualizar(duplicata)
