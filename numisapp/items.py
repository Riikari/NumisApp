# -*- coding: utf-8 -*-

class Moneda:
    #Define una moneda en base a su valor, fecha de acuñacion y pais asociado

    def __init__(self, valor, pais, fecha):
        self.valor = valor
        self.pais = pais
        self.fecha = fecha

    def addDesc(self, str):
        self.desc = str

    def getValor(self):
        return self.valor

    def getPais(self):
        return self.pais
        
    def getFecha(self):
        return self.fecha