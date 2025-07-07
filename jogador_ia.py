# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):

        # R1. Se você ou seu oponente tiver duas marcações em sequência, marque o quadrado restante.
        for tipo in [self.tipo, Tabuleiro.JOGADOR_X]:
            # Verifica linhas
            for l in range(0,3):
                if sum(self.tabuleiro.matriz[l]) == tipo * 2:
                    print("Usando regra R1: linha (" + ('vencer' if tipo == self.tipo else 'bloquear') + ")")
                    return (l, self.tabuleiro.matriz[l].index(Tabuleiro.DESCONHECIDO))
            # Verifica colunas
            for c in range(0,3):
                if sum(self.tabuleiro.matriz[l][c] for l in range(3)) == tipo * 2:
                    print("Usando regra R1: coluna (" + ('vencer' if tipo == self.tipo else 'bloquear') + ")")
                    return (self.tabuleiro.matriz[c].index(Tabuleiro.DESCONHECIDO), c)
            # Verifica diagonais
            if (self.tabuleiro.matriz[0][0] + self.tabuleiro.matriz[1][1] + self.tabuleiro.matriz[2][2]) == tipo * 2:
                for i in range(3):
                    if self.tabuleiro.matriz[i][i] == Tabuleiro.DESCONHECIDO:
                        print("Usando regra R1: diagonal principal (" + ('vencer' if tipo == self.tipo else 'bloquear') + ")")
                        return (i, i)
            if (self.tabuleiro.matriz[0][2] + self.tabuleiro.matriz[1][1] + self.tabuleiro.matriz[2][0]) == tipo * 2:
                for i in range(3):
                    if self.tabuleiro.matriz[i][2-i] == Tabuleiro.DESCONHECIDO:
                        print("Usando regra R1: diagonal secundária (" + ('vencer' if tipo == self.tipo else 'bloquear') + ")")
                        return (i, 2-i)

        # R2. Se houver uma jogada que crie duas sequências de duas marcações, use-a.
        for l in range(0,3):
            for c in range(0,3):
                if self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    # Simula a jogada
                    self.tabuleiro.matriz[l][c] = self.tipo
                    count = 0
                    # Checa linhas
                    for li in range(3):
                        if sum(self.tabuleiro.matriz[li]) == self.tipo * 2:
                            count += 1
                    # Checa colunas
                    for ci in range(3):
                        col = [self.tabuleiro.matriz[li][ci] for li in range(3)]
                        if sum(col) == self.tipo * 2:
                            count += 1
                    # Checa diagonal principal
                    diag1 = [self.tabuleiro.matriz[i][i] for i in range(3)]
                    if sum(diag1) == self.tipo * 2:
                        count += 1
                    # Checa diagonal secundária
                    diag2 = [self.tabuleiro.matriz[i][2-i] for i in range(3)]
                    if sum(diag2) == self.tipo * 2:
                        count += 1
                    # Se cria duas ou mais sequências de vitória
                    if count >= 2:
                        print("Usando regra R2: cria duas sequências de duas marcações (fork)")
                        self.tabuleiro.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)
                    # Reverte a jogada
                    self.tabuleiro.matriz[l][c] = Tabuleiro.DESCONHECIDO

        # R3. Se o quadrado central estiver livre, marque-o.
        if self.tabuleiro.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            print("Usando regra R3: centro livre")
            return (1, 1)

        # R4. Se seu oponente tiver marcado um dos cantos, marque o canto oposto.
        # Verifica se o oponente marcou um canto
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for (l, c) in cantos:
            if self.tabuleiro.matriz[l][c] == Tabuleiro.JOGADOR_X:
                l_oposto = 2 - l
                c_oposto = 2 - c
                if self.tabuleiro.matriz[l_oposto][c_oposto] == Tabuleiro.DESCONHECIDO:
                    print("Usando regra R4: canto oposto")
                    return (l_oposto, c_oposto)

        # R5. Se houver um canto vazio, marque-o.
        for (l, c) in cantos:
            if self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                print("Usando regra R5: canto vazio")
                return (l, c)

        # R6. Marque arbitrariamente um quadrado vazio.
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            print("Usando regra R6: jogada aleatória")
            return lista[p]
        else:
            print("Nenhuma jogada possível")
            return None