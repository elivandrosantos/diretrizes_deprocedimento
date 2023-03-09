def validar_resposta(pergunta):
    resposta = input(f'{pergunta} S/N ').lower()
    while resposta not in ['s', 'n']:
        print('Digite um caractere Sim(S) ou Não(N)')
        resposta = input(f'{pergunta} S/N ').lower()
    return resposta == 's'


def pergunta_um():
    return validar_resposta('O cliente é proprietário do veículo?')


def pergunta_dois():
    return validar_resposta('O cliente tem acesso ao manual do proprietário?')


def pergunta_tres():
    return validar_resposta('O problema é nos recursos de rádio, navegação ou Bluetooth?')


def pergunta_quatro():
    return validar_resposta('O problema do cliente foi resolvido?')


def diretrizProcedimento():
    if pergunta_um():
        if pergunta_dois():
            if pergunta_quatro():
                print('Encerre a chamada.')
            else:
                print('Recomende uma visita ao revendedor para inspeções/esclarecimentos adicionais.')
        else:
            if pergunta_tres():
                print('Transfira para o suporte técnico.')
            else:
                print('Recomende uma visita ao revendedor para inspeções/esclarecimentos adicionais.')
    else:
        print('Transfira para o suporte de marketing.')


print('****Diretrizes de procedimentos****\n')

diretrizProcedimento()
print('**** Fim do Programa ****')
