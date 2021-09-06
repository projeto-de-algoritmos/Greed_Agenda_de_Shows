atividade = {}
lista_atividades = []

while True:
    print("\nO que você deseja fazer?\n\n");
    print("1) Adicionar shows\n2) Visulizar agenda do dia\n3) Sair\n");
    entrada = input()
    entrada = int(entrada)
    if (entrada == 1):
        dia = str (input('Desejar escolher a agenda para qual dia?(dd/mm) '))
        c = 's'
        while c == 's' or c == 'S':    
            atividade['nome'] = str (input('Nome do evento: '))
            horaInicio = int(input('Horario de inicio do show: '))
            atividade['inicio'] = int (horaInicio)
            tempo = input('Horario de termino do show: ')
            temp = tempo
            tempo = int(tempo)
            atividade['fim'] = int(tempo)
            lista_atividades.append(atividade.copy())
            atividade.clear()
            c = str(input ('Deseja adicionar mais shows?(s/n) '))    
        lista_atividades = sorted(lista_atividades, key=lambda row:row['fim'])
        j = -1
        agenda = []
        cont = 0
        for i in lista_atividades:
            if j <= lista_atividades[cont]['inicio']:
                agenda.append(lista_atividades[cont])
                j = lista_atividades[cont]['fim']
            cont = cont + 1
        arquivo = open('agenda.txt', 'a')
        arquivo.write("Agenda (" + dia + ")")
        arquivo.write("\n")
        cont = 0
        for i in agenda:
            arquivo.write("Evento: " + agenda[cont]['nome'])
            arquivo.write("\n")
            arquivo.write("Inicio: ")
            hora_inicio = str (agenda[cont]['inicio'])
            arquivo.write(hora_inicio)
            arquivo.write("\n")
            arquivo.write("Termino: ")
            hora_fim = str(agenda[cont]['fim'])
            arquivo.write(hora_fim)
            arquivo.write("\n\n")
            cont = cont + 1
        arquivo.write("------------------------------------")
        arquivo.close()
    elif entrada == 2:
        cont = 0
        print("------------------------------------")
        print("-           Agenda (" + dia + ")         -")
        print("------------------------------------")
        for i in agenda:
            print("- Evento: " + agenda[cont]['nome'])
            print("- Inicio:", end=" ")
            print(agenda[cont]['inicio'])
            print("- Termino:", end=" ")
            print(agenda[cont]['fim'])
            print("------------------------------------")
            cont = cont + 1
    else:
        break