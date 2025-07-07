# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        # Verifica linhas
        for i in range(3):
            if self.matriz[i][0] == self.matriz[i][1] == self.matriz[i][2] != Tabuleiro.DESCONHECIDO:
                return self.matriz[i][0]
            
        # Verifica colunas
        for j in range(3):
            if self.matriz[0][j] == self.matriz[1][j] == self.matriz[2][j] != Tabuleiro.DESCONHECIDO:
                return self.matriz[0][j]
            
        # Verifica diagonais
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] != Tabuleiro.DESCONHECIDO:
            return self.matriz[0][0]
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] != Tabuleiro.DESCONHECIDO:
            return self.matriz[0][2]
        
        # Se não houver campeão, retorna DESCONHECIDO
        return Tabuleiro.DESCONHECIDO