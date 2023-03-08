"""
Esse algoritmo basicamtente é uma diretriz de procedimento, o cliente irá responder algumas
perguntas pré pronta e de acordo com sua resposta, sendo sim ou não o programa irá retornar
uma condição para o cliente.
"""

print('****Diretrizes de procedimentos****\n')


def diretrizProcedimento():
    per_um = input(f'O cliente é proprietário do veículo? S/N ')
    resposta = per_um

    while resposta not in ['s', 'n']:
        print('Digite um caractere Sim(S) ou Não(N)')
        resposta = input(f'O cliente é proprietário do veículo? S/N ')

    if resposta == 's':
        pass

        def pergunta_dois():
            perg_dois = input('O cliente tem acesso ao manual do proprietário? ')
            resp_dois = perg_dois

            while resp_dois not in ['s', 'n']:
                print('Digite um caractere Sim(S) ou Não(N) ')
                resp_dois = input('O cliente tem acesso ao manual do proprietário? ')

            if resp_dois == 's':

                def pergunta_quatro():
                    perg_quatro = str(input('O problema do cliente foi resolvido? '))
                    resp_quatro = perg_quatro

                    while resp_quatro not in ['s', 'n']:
                        print('Digite um caractere Sim(S) ou Não(N) ')
                        resp_quatro = input('O problema do cliente foi resolvido? ')

                    if resp_quatro == 's':
                        print('Encerre a chamada.')
                    else:
                        print('Recomende uma visita ao revendedor para inspeções/esclarecimentos adicionais')

                pergunta_quatro()

            else:
                def pergunta_tres():
                    perg_tres = str(input('O problema é nos recursos de rádio, navegação ou Bluetooth? '))
                    resp_tres = perg_tres

                    while resp_tres not in ['s', 'n']:
                        print('Digite um caractere Sim(S) ou Não(N) ')
                        resp_tres = input('O problema é nos recursos de rádio, navegação ou Bluetooth? ')

                    if resp_tres == 's':
                        print('Transfira para o suporte técnico.')
                    else:
                        print('Recomende uma visita ao revendedor para inspeções/esclarecimentos adicionais.')

                pergunta_tres()
        pergunta_dois()

    else:
        print('Transfira para o suporte de marketing.')


diretrizProcedimento()

print('**** Fim do Programa ****')

