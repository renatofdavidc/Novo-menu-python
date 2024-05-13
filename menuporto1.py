import time

def exibirMenu():
    print('====================== MEU CARRO PORTO ======================')
    print('Seja bem vindo ao app Meu Carro Porto!')
    print('====================== MENU PRINCIPAL ======================')
    print('[1] - Onde posso acessar o site da Porto?')
    print('[2] - Meu carro está com um problema')
    print('[3] - Chamar um mecânico')
    print('[4] - Calculadora de economia do Meu Carro Porto')
    print('[5] - O que é o app Meu Carro Porto')
    print('[6] - Sair do aplicativo')

def tela1():
    print('====================== ACESSO SITE DA PORTO ======================')
    print('Você pode acessar o site da porto pelo link: https://www.portoseguro.com.br/seguro-auto')
    print('Retornando ao menu principal em 10 segundos...')
    time.sleep(10)
    exibirMenu()

def tela2():
    print('====================== MEU CARRO ESTÁ COM UM PROBLEMA ======================')
    print('Qual problema o seu carro apresenta?')
    print('[1] - Problemas de motor')
    print('[2] - Problemas na transmissão')
    print('[3] - Problemas nas rodas/suspensão')
    print('[4] - Problemas com peças externas/estéticas')
    print('[5] - Retornar ao menu principal')
    problema = input('Escolha uma opção: ')

rua = []
numerocasa = []
bairro = []
i = 0

def tela3():
    print('====================== CHAMAR UM MECÂNICO ======================')
    print('[1] - Registrar um endereço para envio de mecânico (máximo de 5)')
    print('[2] - Escolher um endereço para ser enviado um mecânico')
    print('[3] - Visualizar endereços registrados')
    print('[4] - Retornar ao menu principal')
    escolhaOpcao = input('Digite uma opção: ')
    def definirEndereco():
        bairroinput = input('Por favor, digite seu bairro: ')
        bairro.append(bairroinput)
        ruainput = input('Por favor, digite sua rua: ')
        rua.append(ruainput)
        numerocasainput = input('Por favor, digite o número da sua casa:')
        numerocasa.append(numerocasainput)
        tela3()
    def escolherUmEndereco():
        i = int(input('Para qual endereço deve ser enviado o guincho? Escolha um número de 1 a 5: '))-1
        if (i < 0 or i >=len(rua)):
            print('Opção inválida! Em 5 segundos você será encaminhado ao menu anterior...')
            time.sleep(5)
            tela3()
        else:
            print(f'Um guincho será enviado para o seguinte endereço: Bairro: {bairro[i]}, Rua: {rua[i]}, Número: {numerocasa[i]}')
            time.sleep(5)
            exibirMenu()
    def visualizarEnderecos():
        print('Os endereços registrados são, respectivamente em cada lista:')
        print(f'Rua: {rua}')
        print(f'Bairro: {bairro}')
        print(f'Número da casa: {numerocasa}')
        print('Retornando ao menu anterior em 10 segundos...')
        time.sleep(10)
        tela3()

    match escolhaOpcao:
        case '1':
            definirEndereco()
        case '2':
            escolherUmEndereco()
        case '3':
            visualizarEnderecos()
        case '4':
            exibirMenu()
        case _:
            print('Opção inválida! Em 5 segundos você será enviado para o menu principal...')
            time.sleep(5)
            exibirMenu()

def tela4():
    print('====================== CALCULADORA DE ECONOMIA ======================')


    
def main():
    while True:
        exibirMenu()
        escolhaPrincipal = input('Escolha uma opção: ')

        match escolhaPrincipal:
            case '1':
                tela1()
            case '2': 
                tela2()
            case '3':
                tela3()
            case _:
                print('Opção inválida! Por favor, digite novamente.')
if __name__ == "__main__":
    main()
