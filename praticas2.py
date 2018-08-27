##############################
#   Projeto de Práticas 2    #
#    João Otávio Ukstin      #
#    Letícia Alves Chijo     #
#    Nikolas Athanasopoulos  #
#    Pedro Afonso Jaloto     #
##############################


def main():

  
    #decide o tamanho do tabuleiro
    ver1 = 0
    size_list = ["3","4","5"]
    print("Vamos jogar?")
    while ver1 == 0:
        size = input("Qual o tamanho do tabuleiro (3x3, 4x4, 5x5)? ")
        if size in size_list:
            size = int(size)
            print("Você escolheu um tabuleiro de tamanho ", size, "x", size)
            ver1 = 1
        else:
            print("Esse não é um valor válido")

    #imprime a matriz para verificação
    print(set_board(size))
            
    ver2 = 0
    player_list = ["2","3"]
    while ver2 == 0:
        playernum = input("Quantos jogadores vão jogar (2, 3)? ")
        if playernum in player_list:
            playernum = int(playernum)
            print(playernum, " jogadores vão jogar.")
            ver2 = 1
        else:
            print("Esse não é um valor válido")


    #aqui começa o jogo
    player = 1
    end_game = 0
    point = [0,0,0]
    board = set_board(size)
    end_board = ver_board(size)
    cont = 0
    
    while end_game == 0:
        print("Player ", player)
        button = input("Botão: ")
        board = botao_apertado(button, board)
        end_board = ver_point(board, end_board, player)
        if cont_1(end_board) != cont:
            point[player-1] += 1
            cont = cont_1(end_board)
        else:
            player = change_player(player, playernum)
            
        print("Traços: ", board)
        print("Centros: ", end_board)
        print("Pontuação: ", point)

        if cont == size*size:
            end_game = 1

    j = 0
    win = 0
    for i in range(len(point)):
        if point[i] > j:
            j = point[i]
            win = i+1

    print("O vencedor é o player ", win, "!")
    print("Obrigado por jogar")
            
    return


def set_board(size):

    if size == 5:

        board = [[["v11","v12","h11","h21"],["v12","v13","h21","h31"],["v13","v14","h31","h41"],["v14","v15","h41","h51"],["v15","v16","h51","h61"]],[["v21","v22","h12","h22"],["v22","v23","h22","h32"],["v23","v24","h32","h42"],["v24","v25","h42","h52"],["v25","v26","h52","h62"]],[["v31","v32","h13","h23"],["v32","v33","h23","h33"],["v33","v34","h33","h43"],["v34","v35","h43","h53"],["v35","v36","h53","h63"]],[["v41","v41","h14","h24"],["v42","v43","h24","h34"],["v43","v44","h34","h44"],["v44","v45","h44","h54"],["v45","v46","h54","h64"]],[["v51","v52","h15","h25"],["v52","v53","h25","h35"],["v53","v54","h35","h45"],["v54","v55","h45","h55"],["v55","v56","h55","h65"]]]

    elif size == 4:

        board = [[["v11","v12","h11","h21"],["v12","v13","h21","h31"],["v13","v14","h31","h41"],["v14","v15","h41","h51"]],[["v21","v22","h12","h22"],["v22","v23","h22","h32"],["v23","v24","h32","h42"],["v24","v25","h42","h52"]],[["v31","v32","h13","h23"],["v32","v33","h23","h33"],["v33","v34","h33","h43"],["v34","v35","h43","h53"]],[["v41","v41","h14","h24"],["v42","v43","h24","h34"],["v43","v44","h34","h44"],["v44","v45","h44","h54"]]]

    elif size == 3:

        board = [[["v11","v12","h11","h21"],["v12","v13","h21","h31"],["v13","v14","h31","h41"]],[["v21","v22","h12","h22"],["v22","v23","h22","h32"],["v23","v24","h32","h42"]],[["v31","v32","h13","h23"],["v32","v33","h23","h33"],["v33","v34","h33","h43"]]]

        
    return board


def ver_board(size):

    if size == 5:

        board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    elif size == 4:

        board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    elif size == 3:

        board = [[0,0,0],[0,0,0],[0,0,0]]

        
    return board


def botao_apertado(button, board):

    lin = 0
    cont = 0
    while lin < len(board) and cont < 2:
        col = 0
        while col < len(board) and cont < 2:
            el = 0
            while el < len(board[lin][col]) and cont < 2:
                if board[lin][col][el] == button:
                    board[lin][col][el] = 1
                    cont += 1
                el += 1
            col += 1    
        lin += 1
    
    return board

def ver_point(board, end_board, player):

    for lin in range(len(board)):
        for col in range(len(board)):
            if all((el==1 for el in board[lin][col])) and end_board[lin][col] == 0:
                end_board[lin][col] = player
                
    return end_board

def change_player(player, playernum):

    if player == 1:
        player = 2
    elif player == 2 and playernum == 3:
        player = 3
    elif player == 2 and playernum == 2:
        player = 1
    elif player == 3:
        player = 1

    return player
    

def cont_1(board):

    cont = 0
    for lin in range(len(board)):
        for col in range(len(board)):
            if board[lin][col] != 0:
                cont += 1
    return cont

main()
