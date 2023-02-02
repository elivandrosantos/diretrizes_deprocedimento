"""
Esse algoritmo basicamtente é uma diretriz de procedimento, o cliente irá responder algumas
perguntas pré pronta e de acordo com sua resposta, sendo sim ou não o programa irá retornar
uma condição para o cliente.

"""


def diretrizesdeProcedimento():

    print('****Diretrizes de procedimentos****\n')

    pergunta_1 = input('O cliente é proprietário do veículo? S/N ')

    if pergunta_1 == 's':
        pergunta_2 = input('O cliente tem acesso ao manual do proprietário? S/N ')
        if pergunta_2 == 's':
            print('Verifique as páginas 43 e 44 do manual. ')
            pergunta_4 = input('O problema do cliente foi resolvido? ')

            if pergunta_4 == 's':
                print('Encerre a chamada.')
                print('**** FIM DO PROGRAMA ****')
            else:
                print('Recomende uma visita ao revendedor para inspeções/esclarecimentos adicionais.')
                print('**** FIM DO PROGRAMA ****')

        elif pergunta_2 != 's':
            pergunta_3 = input('O Problema do cliente é nos recursos de rádio, navegação ou Bluetooth? S/N ')
            if pergunta_3 == 's':
                print('Transferindo para o suporte técnico.')
                print('****FIM DO PROGRAMA****')
            else:
                print('Recomende uma visita ao revendedor para inspeções/esclarecimentos adicionais.')
                print(' ****FIM DO PROGRAMA**** ')
    else:
        print('Transfira para o suporte de marketing.')
        print('**** FIM DO PROGRAMA ****')


diretrizesdeProcedimento()
