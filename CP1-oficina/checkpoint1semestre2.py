#FUNÇÕES
def mostarInscricoesOficina(oficina):
    print("Foram realizadas {} inscrições nessa oficina.".format(len(oficina)))
def percorrerOficinas(rm, oficina):
    for i in range(len(oficina)):
        if oficina[i] == rm:
            print("O Aluno não pode se inscrever em mais de uma mesma oficina")
            return 0
    return 1
def menuInscricao(listarm):
    print("\nMenu de Opções")
    if len(listarm) == 0:
        print("1 - Cadastrar alunos")
    print("2 - Fazer inscrições\n3 - Listar inscrições\n"
                "4 - Sair")

    menu = int(input("Digite a opção desejada: "))


    return menu

def localizaOficina(todasOficinas,rm):
    temp = []
    for i in range(len(todasOficinas)):
       for j in range(len(todasOficinas[i])):
            if todasOficinas[i][j] == rm:
                temp.append(i)
    return(temp)

def funcaoPrintNome(rm, todasOficinas, listaGrande, tuplaOficinas):
    index = 0
    for i in range(len(listaGrande)):
        if listaGrande[i][0] == rm:
            index = i
    print("\nrm: {0} - aluno: {1} - serie: {2}".format(listaGrande[index][0], listaGrande[index][1], listaGrande[index][2]))
    print("\nOficinas:")
    temp = localizaOficina(todasOficinas, rm)
    for i in range(len(temp)):
        print(tuplaOficinas[i])

def encherLista (listarm, listaNome, listaSerie, listaGrande):
  listaTemp = []
  for i in range(len(listarm)):
       listaTemp.append(listarm[i])
       listaTemp.append(listaNome[i])
       listaTemp.append(listaSerie[i])
       listaGrande.append(listaTemp)
       listaTemp = []


listaGrande = []

def ordenaNome(listaGrande):
    listaGrande.sort(key=lambda e: e[1])

def funcaoPrintOficina(rm, todasOficinas, tuplaOficinas):
    for n in range(len(todasOficinas)):
       for p in range(len(todasOficinas[n])):
            if todasOficinas[n][p] == rm:
                print(tuplaOficinas[n])

def funcaoPrintNomeOficina(rm, listaGrande):
    index = 0
    for i in range(len(listaGrande)):
        if listaGrande[i][0] == rm:
           index = i
        print("rm: {0} - aluno: {1} - serie: {2}".format(listaGrande[index][0], listaGrande[index][1], listaGrande[index][2]))


# OFICINAS LISTAS
lista_oficinaA = []  # A língua de sinais                 - quarta-feira     - séries liberadas: (2,3,4,5)
lista_oficinaB = []  # Criando e recriando com emojis     - sexta-feira      - série liberada: (2)
lista_oficinaC = []  # Criar e contar histórias           - segunda-feira    - séries liberadas: (2,3)
lista_oficinaD = []  # Expressão Artística                - quinta-feira     - séries liberadas: (4,5)
lista_oficinaE = []  # Leitura dinâmica                   - quinta-feira     - série liberada: (5)
lista_oficinaF = []  # Leitura Dramática                  - segunda-feira    - série liberada: (4)
lista_oficinaG = []  # O corpo fala                       - terça-feira      - série liberada: (3)
lista_oficinaH = []  # O mundo da imaginação              - quarta-feira     - série liberada: (2)
lista_oficinaI = []  # Soletrando                         - sexta-feira      - série liberada: (5)
lista_oficinaJ = []  # Teatro: Luz, Câmera e Ação         - terça-feira      - séries liberadas: (3,4)

lista_todasoficinas = [lista_oficinaA, lista_oficinaB, lista_oficinaC, lista_oficinaD, lista_oficinaE, lista_oficinaF,
                       lista_oficinaG, lista_oficinaH, lista_oficinaI, lista_oficinaJ]

tupla_oficinas = ("A língua de sinais - Quarta-Feira", "Criando e recriando com emojis - Sexta-Feira",
"Criar e contar histórias - Segunda-Feira", "Expressão Artística - Quinta-Feira", "Leitura dinâmica - Quinta-Feira",
"Leitura Dramática - Segunda-Feira", "O corpo fala - Terça-Feira", "O mundo da imaginação - Quarta-Feira",
"Soletrando - Sexta-Feira", "Teatro: Luz, Câmera e Ação - Terça-Feira")

# OUTRAS LISTAS
lista_rm = []
lista_nome = []
lista_serie = []
lista_21 = []
lista_22 = []
lista_23 = []
lista_31 = []
lista_32 = []
lista_33 = []
lista_41 = []
lista_42 = []
lista_43 = []
lista_51 = []
lista_52 = []
lista_53 = []

#---------------------------------------------------------------------------------------------------------------

#CODIGO

menu = int(input("Menu de Opções\n1 - Cadastrar alunos\n2 - Fazer inscrições\n3 - Listar inscrições\n"
                 "4 - Sair\nDigite a opção desejada: "))

while menu != 4:

    if menu == 1:
        while True:
            rm = int(input("Digite o RM do aluno: "))
            for i in range (len(lista_rm)):
                if lista_rm[i] == rm:
                     print("rm invalido")
                     rm = int(input("Digite o RM do aluno: "))
            if rm == 0:
                break
            lista_rm.append(rm)
            nome = str(input("Digite o nome do aluno: "))
            lista_nome.append(nome)

            serie = int(input("Digite a série do aluno: "))

            if serie < 2 or serie > 5:
                print("Série invalida, aluno deve pertencer a 2ª, 3ª, 4ª ou 5ª série")
                serie = int(input("Digite a série do aluno: "))


            lista_serie.append(serie)



    if menu == 2:
        procura_rm = int(input("Digite o RM do aluno: "))
        if procura_rm in lista_rm:
            print("Aqui está a relação de oficinas disponíveis para a série do aluno cadastrado: ")
        else:
            print("Aluno  não  cadastrado. Favor procurar a coordenação do Fundamental I.")
            break

        serieAluno = 0
        for i in range(len(lista_rm)):
            if procura_rm == lista_rm[i]:
                serieAluno = i

        if lista_serie[serieAluno] == 2:

                    print("2 série matutino: "     
                    "\nOpção A - A língua de sinais - Quarta-Feira"
                    "\nOpção C - Criar e contar histórias - Segunda-Feira"
                    "\n--------------------------------------------"
                    "\n2 série vespertino:"
                    "\nOpção H - O mundo da imaginação - Quarta-Feira"
                    "\nOpção J - Teatro: Luz, Câmera e Ação - Terça-Feira"
                    "\n--------------------------------------------"
                    "\nÉ possivel escolher até 3 oficinas, caso não queira mais de 1 ou 2, digite N nas demais opções")

                    serie_21 = input("Digite a primeira opcão desejada: ")

                    if serie_21 == "A" and len(lista_oficinaA) < 2:
                            lista_oficinaA.append(procura_rm)
                            mostarInscricoesOficina(lista_oficinaA)
                    elif serie_21 == "C" and len(lista_oficinaC) < 2:
                            lista_oficinaC.append(procura_rm)
                            mostarInscricoesOficina(lista_oficinaC)
                    elif serie_21 == "H" and len(lista_oficinaH) < 2:
                            lista_oficinaH.append(procura_rm)
                            mostarInscricoesOficina(lista_oficinaH)
                    elif serie_21 == "J" and len(lista_oficinaJ) < 2:
                            lista_oficinaJ.append(procura_rm)
                            mostarInscricoesOficina(lista_oficinaJ)
                    else:
                            print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_21.append(serie_21)

                    serie_22 = input("Digite a segunda opcão desejada: ")

                    if serie_22 != "N":

                        if serie_22 == "A" and len(lista_oficinaA) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaA) == 1:
                                lista_oficinaA.append(procura_rm)
                                mostarInscricoesOficina(lista_oficinaA)
                        elif serie_22 == "C" and len(lista_oficinaC) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaC) == 1:
                                lista_oficinaC.append(procura_rm)
                                mostarInscricoesOficina(lista_oficinaC)
                        elif serie_22 == "H" and len(lista_oficinaH) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaH) == 1:
                                lista_oficinaH.append(procura_rm)
                                mostarInscricoesOficina(lista_oficinaH)
                        elif serie_22 == "J" and len(lista_oficinaJ) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaJ) == 1:
                                lista_oficinaJ.append(procura_rm)
                                mostarInscricoesOficina(lista_oficinaJ)
                        else:
                            print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_22.append(serie_22)

                    serie_23 = input("Digite a terceira opcão desejada: ")

                    if serie_23 != "N":

                        if serie_23 == "A" and len(lista_oficinaA) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaA) == 1:
                                lista_oficinaA.append(procura_rm)
                                mostarInscricoesOficina(lista_oficinaA)
                        elif serie_23 == "C" and len(lista_oficinaC) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaC) == 1:
                                lista_oficinaC.append(procura_rm)
                                mostarInscricoesOficina(lista_oficinaC)
                        elif serie_23 == "H" and len(lista_oficinaH) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaH) == 1:
                                lista_oficinaH.append(procura_rm)
                                mostarInscricoesOficina(lista_oficinaH)
                        elif serie_23 == "J" and len(lista_oficinaJ) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaJ) == 1:
                                lista_oficinaJ.append(procura_rm)
                                mostarInscricoesOficina(lista_oficinaJ)
                        else:
                            print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_23.append(serie_23)



        if lista_serie[serieAluno] == 3:

                    print("3 série matutino: "
                    "\nOpção A - A língua de sinais - Quarta-Feira"
                    "\nOpção B - Criando e recriando com emojis - Sexta-Feira"
                    "\nOpção C - Criar e contar histórias - Segunda-Feira"
                    "\n--------------------------------------------"
                    "\n3 série vespertino:"
                    "\nOpção G - O corpo fala - Terça-Feira"
                    "\n--------------------------------------------"
                    "\nÉ possivel escolher até 3 oficinas, caso não queira mais de 1 ou 2, digite N nas demais opções")

                    serie_31 = input("Digite a primeira opcão desejada: ")

                    if serie_31 == "A" and len(lista_oficinaA) < 2:
                        lista_oficinaA.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaA)
                    elif serie_31 == "B" and len(lista_oficinaB) < 2:
                        lista_oficinaB.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaB)
                    elif serie_31 == "C" and len(lista_oficinaC) < 2:
                        lista_oficinaC.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaC)
                    elif serie_31 == "G" and len(lista_oficinaG) < 2:
                        lista_oficinaG.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaG)
                    else:
                        print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_31.append(serie_31)

                    serie_32 = input("Digite a segunda opcão desejada: ")

                    if serie_32 != "N":
                        if serie_32 == "A" and len(lista_oficinaA) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaA) == 1:
                               lista_oficinaA.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaA)
                        elif serie_32 == "B" and len(lista_oficinaB) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaB) == 1:
                               lista_oficinaB.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaB)
                        elif serie_32 == "C" and len(lista_oficinaC) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaC) == 1:
                               lista_oficinaC.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaC)
                        elif serie_32 == "G" and len(lista_oficinaG) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaG) == 1:
                               lista_oficinaG.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaG)
                        else:
                            print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_32.append(serie_32)

                    serie_33 = input("Digite a terceira opcão desejada: ")

                    if serie_33 != "N":

                        if serie_33 == "A" and len(lista_oficinaA) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaA) == 1:
                               lista_oficinaA.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaA)
                        elif serie_33 == "B" and len(lista_oficinaB) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaB) == 1:
                               lista_oficinaB.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaB)
                        elif serie_33 == "C" and len(lista_oficinaC) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaC) == 1:
                               lista_oficinaC.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaC)
                        elif serie_33 == "G" and len(lista_oficinaG) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaG) == 1:
                               lista_oficinaG.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaG)
                        else:
                            print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_33.append(serie_33)

        if lista_serie[serieAluno] == 4 :

                    print("4 série matutino: \n"
                    "\nOpção B - Criando e recriando com emojis - Sexta-Feira"
                    "\nOpção C - Criar e contar histórias - Segunda-Feira"
                    "\nOpção D - Expressão Artística - Quinta-Feira"
                    "\n--------------------------------------------"
                    "\n4 série vespertino: \n"
                    "\nOpção F - Leitura Dramática - Segunda-Feira"
                    "\n--------------------------------------------"
                    "\nÉ possivel escolher até 3 oficinas, caso não queira mais de 1 ou 2, digite 0 nas demais opções")

                    serie_41 = input("Digite a primeira opcão desejada: ")

                    if serie_41 == "B" and len(lista_oficinaB) < 2:
                        lista_oficinaB.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaB)
                    elif serie_41 == "C" and len(lista_oficinaC) < 2:
                        lista_oficinaC.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaC)
                    elif serie_41 == "D" and len(lista_oficinaD) < 2:
                        lista_oficinaD.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaD)
                    elif serie_41 == "F" and len(lista_oficinaF) < 2:
                        lista_oficinaF.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaF)
                    else:
                        print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_41.append(serie_41)

                    serie_42 = input("Digite a segunda opcão desejada: ")

                    if serie_42 != "N":

                        if serie_42 == "B" and len(lista_oficinaB) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaB) == 1:
                               lista_oficinaB.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaB)
                        elif serie_42 == "C" and len(lista_oficinaC) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaC) == 1:
                               lista_oficinaC.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaC)
                        elif serie_42 == "D" and len(lista_oficinaD) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaD) == 1:
                               lista_oficinaD.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaD)
                        elif serie_42 == "F" and len(lista_oficinaF) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaF) == 1:
                               lista_oficinaF.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaF)
                        else:
                            print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_42.append(serie_42)

                    serie_43 = input("Digite a terceira opcão desejada: ")

                    if serie_43 != "N":

                        if serie_43 == "B" and len(lista_oficinaB) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaB) == 1:
                               lista_oficinaB.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaB)
                        elif serie_43 == "C" and len(lista_oficinaC) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaC) == 1:
                               lista_oficinaC.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaC)
                        elif serie_43 == "D" and len(lista_oficinaD) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaD) == 1:
                               lista_oficinaD.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaD)
                        elif serie_43 == "F" and len(lista_oficinaF) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaF) == 1:
                               lista_oficinaF.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaF)
                        else:
                            print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_43.append(serie_43)

        if lista_serie[serieAluno] == 5:

                    print("5 série matutino: \n"
                    "\nOpção C - Criar e contar histórias - Segunda-Feira"
                    "\nOpção D - Expressão Artística - Quinta-Feira"
                    "\nOpção E - Leitura dinâmica - Quinta-Feira"
                    "\n--------------------------------------------"
                    "\n5 série vespertino: "
                    "\nOpção I - Soletrando - Sexta-Feira"
                    "\n--------------------------------------------"
                    "\nÉ possivel escolher até 3 oficinas, caso não queira mais de 1 ou 2, digite 0 nas demais opções")

                    serie_51 = input("Digite a primeira opcão desejada: ")

                    if serie_51 == "C" and len(lista_oficinaC) < 2:
                        lista_oficinaC.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaC)
                    elif serie_51 == "D" and len(lista_oficinaD) < 2:
                        lista_oficinaD.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaD)
                    elif serie_51 == "E" and len(lista_oficinaE) < 2:
                        lista_oficinaE.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaE)
                    elif serie_51 == "I" and len(lista_oficinaI) < 2:
                        lista_oficinaI.append(procura_rm)
                        mostarInscricoesOficina(lista_oficinaI)
                    else:
                        print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_51.append(serie_51)

                    serie_52 = input("Digite a segunda opcão desejada: ")

                    if serie_52 != "N":

                        if serie_52 == "C" and len(lista_oficinaC) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaC) == 1:
                               lista_oficinaC.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaC)
                        elif serie_52 == "D" and len(lista_oficinaD) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaD) == 1:
                               lista_oficinaD.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaD)
                        elif serie_52 == "E" and len(lista_oficinaE) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaE) == 1:
                               lista_oficinaE.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaE)
                        elif serie_52 == "I" and len(lista_oficinaI) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaI) == 1:
                               lista_oficinaI.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaI)
                        else:
                            print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_52.append(serie_52)

                    serie_53 = input("Digite a terceira opcão desejada: ")

                    if serie_53 != "N":

                        if serie_53 == "C" and len(lista_oficinaC) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaC) == 1:
                               lista_oficinaC.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaC)
                        elif serie_53 == "D" and len(lista_oficinaD) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaD) == 1:
                               lista_oficinaD.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaD)
                        elif serie_53 == "E" and len(lista_oficinaE) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaE) == 1:
                               lista_oficinaE.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaE)
                        elif serie_53 == "I" and len(lista_oficinaI) < 2:
                            if percorrerOficinas(procura_rm, lista_oficinaI) == 1:
                               lista_oficinaI.append(procura_rm)
                               mostarInscricoesOficina(lista_oficinaI)
                        else:
                            print("Essa Oficina chegou ao número máximo de inscrições")

                    lista_53.append(serie_53)

    if menu == 3:
        menu_alfabetico = int(input("Menu Listar Inscrições"
                                    "\n1 - Listar por aluno(ordem alfabética de nome)"
                                    "\n2 - Listar por oficina(ordem alfabética)"
                                    "\nDigite a opção desejada: "))
        if menu_alfabetico == 1:
            encherLista(lista_rm, lista_nome, lista_serie, listaGrande)
            ordenaNome(listaGrande)
            for i in range(len(listaGrande)):
                funcaoPrintNome(listaGrande[i][0], lista_todasoficinas, listaGrande, tupla_oficinas)

        if menu_alfabetico == 2:
            encherLista(lista_rm, lista_nome, lista_serie, listaGrande)
            for i in range(len(listaGrande)):
                funcaoPrintOficina(listaGrande[i][0], lista_todasoficinas, tupla_oficinas)
                funcaoPrintNomeOficina(listaGrande[i][0], listaGrande)

    if menu == 4:
        print("Você saiu do Menu.")
    menu = menuInscricao(lista_rm)




