'''
Primeiro trabalho de IA

Guilherme de Lacerda Gomes - 1421134
Leonardo Grosso Moraes     - XXXXXXX   
'''

import sys

##### Variaveis globais #####

# Quantidade de clientes
clientes = None

# Capacidade de carga dos veiculos
capacidade = None

# Posicao x dos clientes
coordenada_x = []

# Posicao y dos clientes
coordenada_y = []

# Demanda dos clientes
demanda_clientes = []



def dados_do_arquivo():
    '''
    Funcao que, dado o arquivo .txt passado como parametro,
    salva as informacoes dele (supondo que esteja em um formato padronizado Uchoa et al).
    A funcao salva as linhas do arquivo em uma lista e, a partir dessa lista,
    obtem as informacoes do problema.
    '''

    with open(sys.argv[1], 'r') as arquivo:
       
        palavras = [linha.split() for linha in arquivo]
        iterador = iter(palavras)
        global clientes
        global capacidade

        for i in range(len(palavras)):

            if palavras[i][0] == 'DEMAND_SECTION':
                valor = i
                break

        
        for i in range(len(palavras)):

            elemento = next(iterador)

            if i < valor:
                if i < 7:
                    for x in range(len(elemento)):
                        if elemento[x] == 'DIMENSION':
                            clientes = elemento[x+2]
                        if elemento[x] == 'CAPACITY':
                            capacidade = elemento[x+2]
                    
                else: 
                    for x in range(len(elemento)):
                        if x == 1:
                            coordenada_x.append(int(elemento[x]))
                        if x == 2:
                            coordenada_y.append(int(elemento[x]))
            else:
                for x in range(len(elemento)):

                    if x == 1:
                        demanda_clientes.append(int(elemento[x]))


def verifica_dados():
    '''
    Funcao auxiliar usada para verificar se os dados
    obtidos pela dados_do_arquivo() estao corretos.
    '''
    print "Numero de clientes: {}\n".format(clientes)
    print "Capacidade dos veiculos: {}\n".format(capacidade)

    print "Cliente\t\tX\t\tY"
    for i in range(len(coordenada_x)):
        print "{}\t\t{}\t\t{}".format(i,coordenada_x[i],coordenada_y[i])

    print "\nCliente\t\tDemanda"
    for x in range(len(demanda_clientes)):
        print "{}\t\t{}".format(x, demanda_clientes[x])


if __name__ == "__main__":
    dados_do_arquivo()
    verifica_dados()
