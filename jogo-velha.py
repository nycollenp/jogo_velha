def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|". join(linha))
        print("_" * 5)

def verificar_vencedor(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return tabuleiro[0][i]
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
            return tabuleiro[0][0]
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
            return tabuleiro[0][2]
        return None

def jogo_velha():
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]
    jogador_atual = "X"

    for rodada in range(9):
        exibir_tabuleiro(tabuleiro)
        print("vez do jogador", jogador_atual)

        while True:
            linha = int(input("escolha a linha 0,1,2: "))
            coluna = int(input("escolha a coluna 0,1,2: "))

            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("entrada inválida! escolha entre 0 e 2.")
            else:
                if tabuleiro[linha][coluna] != " ":
                    print("posição ja ocupada! tente novamente.")
                else:
                    tabuleiro[linha][coluna] = jogador_atual
                    break

        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print("jogador", vencedor, "venceu!")
            return

        if jogador_atual == "X":
            jogador_atual = "0"
        else:
            jogador_atual = "X"

        exibir_tabuleiro(tabuleiro)
        print("empate!")

jogo_velha()










