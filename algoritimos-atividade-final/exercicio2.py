import enum
from os import system

class DiasSemana(enum.Enum):
    Segunda = 1
    Terça = 2
    Quarta = 3
    Quinta = 4
    Sexta = 5

horarios = {
    0: '8-9',
    1: '9-10',
    2: '10-11',
    3: '11-12',
    4: '12-13',
    5: '13-14',
    6: '14-15',
    7: '15-16',
    8: '16-17',
    9: '17-18'
}

def maior_sequencia(lista, valor):
    max_seq = 0
    atual = 0
    inicio_max = -1
    inicio_atual = 0
    for i, item in enumerate(lista):
        if item == valor:
            if atual == 0:
                inicio_atual = i
            atual += 1
            if atual > max_seq:
                max_seq = atual
                inicio_max = inicio_atual
        else:
            atual = 0
    return max_seq, inicio_max

def input_agenda():
    agenda = []
    for i in range(1,6):
        dia = DiasSemana(i).name
        lista_atividades = input(f'{i}. {dia}: ').split()
        agenda.append(lista_atividades)
    return agenda

def input_acoes():
    n = int(input('Número de alterações: '))
    print('Formato para adicionar: Adicionar <Atividade> <Tempo>')
    print('Formato para remover: Remover <Dia> <Horário Inicial> <Horário Final>')
    acoes = []
    while n:
        acao = input('> ').split()
        if len(acao) > 4 or len(acao) < 3:
            raise ValueError('Comando de alteração no formato errado!')
        acoes.append(acao)
        n -= 1
    return acoes

def aplicar_acoes(agenda, acoes):
    for acao in acoes:
        comando = acao[0].lower()
        if comando == 'adicionar':
            atividade = acao[1]
            tempo = int(acao[2])
            adicionado = False
            for dia, atividades in enumerate(agenda):
                maior_seq, indice_inicial = maior_sequencia(atividades, 'Livre')
                if maior_seq < tempo:
                    continue
                else:
                    for i in range(tempo):
                        agenda[dia][i+indice_inicial] = atividade
                    adicionado = True
                    break
            if not adicionado:
                print(f'Não foi possível alocar a atividade {atividade}')
        elif comando == 'remover':
            dia = acao[1]
            if dia not in DiasSemana._member_names_:
                raise ValueError(f'Dia {dia} não existe, não consta na agenda ou está escrito errado!')
                continue
            indice_dia = DiasSemana[dia].value - 1
            horario_inicial = int(acao[2]) - 8
            horario_final = int(acao[3]) - 8
            for i in range(horario_inicial, horario_final):
                agenda[indice_dia][i] = 'Livre'
        else:
            raise ValueError(f'Ação {acao[0]} não existe!')

def imprimir_agenda(agenda):
    agenda_transposta = list(map(list, zip(*agenda))) #unpacking
    print(f'{'\x1b[33mHorário':<7}', end=' ')
    for dia in DiasSemana._member_names_:
        print(f'{dia:<12}', end=' ')
    print('\x1b[0m')
    for horario, atividades in enumerate(agenda_transposta):
        print(f'{horarios[horario]:<7}', end=' ')
        for atividade in atividades:
            print(f'{atividade:<12}', end=' ')
        print()

if __name__ == "__main__":
    system('')
    agenda = input_agenda()
    acoes = input_acoes()
    aplicar_acoes(agenda, acoes)
    imprimir_agenda(agenda)