import os
    
def cadastro_usuario():
    print('Cadastro Usuário - HP Pedrada\n')
    nome = input('Qual o seu nome? ')
    idade = int(input('Qual a sua idade? '))
    
    # Solicita ao usuário que digite o código para o gênero
    print('Digite o código para o gênero:')
    print('1 - Masculino')
    print('2 - Feminino')

    genero_codigo = input('Digite o código correspondente: ')

    # Validação simples para garantir que o usuário insira 1 ou 2
    while genero_codigo not in ('1', '2'):
        print('Opção inválida. Por favor, digite 1 para masculino e 2 para feminino.')
        genero_codigo = input('Digite 1 para masculino e 2 para feminino: ')

    # Mapeia o código do gênero para a string correspondente
    genero = 'Masculino' if genero_codigo == '1' else 'Feminino'
    
    endereco = input('Qual o seu endereço? ')
    
    print('Digite o código para o estado civil:')
    print('1 - Solteiro(a)')
    print('2 - Casado(a)')
    print('3 - Divorciado(a)')
    print('4 - Viúvo(a)')

    estado_civil_codigo = input('Digite o código correspondente: ')

    # Validação simples para garantir que o usuário insira um código válido
    while estado_civil_codigo not in ('1', '2', '3', '4'):
        print('Opção inválida. Por favor, digite um código válido.')
        estado_civil_codigo = input('Digite o código correspondente: ')

    # Mapeia o código do estado civil para a string correspondente
    estado_civil_map = {
        '1': 'Solteiro(a)',
        '2': 'Casado(a)',
        '3': 'Divorciado(a)',
        '4': 'Viúvo(a)'
    }
    estado_civil = estado_civil_map[estado_civil_codigo]
    cpf = int(input('Qual seu CPF? '))
    nome_pai_mae = input('Qual o nome da sua mãe ou do seu pai? (Digite "N/A" se não aplicável): ')
    
    usuario = {
        'nome': nome,
        'idade': idade,
        'genero': genero,
        'endereco': endereco,
        'estado_civil': estado_civil,
        'cpf': cpf,
        'nome_pai_mae': nome_pai_mae if nome_pai_mae.lower() != 'n/a' else None,  # Trata o caso "N/A"
    }
    
    voltar_ao_menu_principal()
    return usuario

def exibir_informacoes_usuario(usuario):
    print("\nInformações do Usuário:")
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']} anos")
    print(f"Gênero: {usuario['genero']}")
    print(f"Endereço: {usuario['endereco']}")
    print(f"Estado Civil: {usuario['estado_civil']}")
    print(f"CPF: {usuario['cpf']}")
       

def alterar_informacoes_usuario(usuario):
    print('Alteração de Informações do Usuário\n')
    estado_civil_map = {
        '1': 'Solteiro(a)',
        '2': 'Casado(a)',
        '3': 'Divorciado(a)',
        '4': 'Viúvo(a)'
    }

    # Solicitar ao usuário as informações que ele deseja atualizar
    opcao = input('Digite o número correspondente ao dado que deseja alterar:\n'
                  '1 - Nome\n'
                  '2 - Idade\n'
                  '3 - Gênero\n'
                  '4 - Endereço\n'
                  '5 - Estado Civil\n'
                  '6 - CPF\n'
                  '7 - Nome da Mãe ou Pai\n'
                  '0 - Sair\n'
                  'Opção: ')

    while opcao != '0':
        if opcao == '1':
            usuario['nome'] = input('Novo nome: ')
        elif opcao == '2':
            usuario['idade'] = int(input('Nova idade: '))
        elif opcao == '3':
            print('Digite o código para o novo gênero:')
            print('1 - Masculino')
            print('2 - Feminino')
            novo_genero_codigo = input('Digite o código correspondente: ')
            while novo_genero_codigo not in ('1', '2'):
                print('Opção inválida. Por favor, digite 1 para masculino e 2 para feminino.')
                novo_genero_codigo = input('Digite 1 para masculino e 2 para feminino: ')
            usuario['genero'] = 'Masculino' if novo_genero_codigo == '1' else 'Feminino'
        elif opcao == '4':
            usuario['endereco'] = input('Novo endereço: ')
        elif opcao == '5':
            print('Digite o código para o novo estado civil:')
            print('1 - Solteiro(a)')
            print('2 - Casado(a)')
            print('3 - Divorciado(a)')
            print('4 - Viúvo(a)')
            novo_estado_civil_codigo = input('Digite o código correspondente: ')
            while novo_estado_civil_codigo not in ('1', '2', '3', '4'):
                print('Opção inválida. Por favor, digite um código válido.')
                novo_estado_civil_codigo = input('Digite o código correspondente: ')
            usuario['estado_civil'] = estado_civil_map[novo_estado_civil_codigo]
        elif opcao == '6':
            usuario['cpf'] = int(input('Novo CPF: '))
        elif opcao == '7':
            novo_nome_pai_mae = input('Novo nome da mãe ou do pai (Digite "N/A" se não aplicável): ')
            usuario['nome_pai_mae'] = novo_nome_pai_mae if novo_nome_pai_mae.lower() != 'n/a' else None
        else:
            print('Opção inválida. Tente novamente.')

        # Exibir informações atualizadas
        exibir_informacoes_usuario(usuario)

        # Solicitar ao usuário a próxima ação
        opcao = input('Digite o número correspondente ao dado que deseja alterar (ou 0 para sair): ')

    print('Alteração de informações concluída.')

    voltar_ao_menu_principal()
    

  
def obter_identidade_genero():
    opcoes = {
        1: 'Masculino',
        2: 'Feminino',
        3: 'Prefiro não dizer'
    }

    print('Identidade de gênero:')
    for key, value in opcoes.items():
        print(f'{key} - {value}')

    while True:
        try:
            opcao = int(input('Selecione uma das opções acima: '))
            if opcao in opcoes:
                return opcoes[opcao]
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Digite um número.')


def obter_estado_civil():
    opcoes = {
        1: 'Casado',
        2: 'Solteiro',
        3: 'Viúvo'
    }

    print('Estado civil:')
    for key, value in opcoes.items():
        print(f'{key} - {value}')

    while True:
        try:
            opcao = int(input('Selecione uma das opções acima: '))
            if opcao in opcoes:
                return opcoes[opcao]
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Digite um número.')

def listar_medicos(medicos):
    print('Lista dos médicos')
    for indice, medico in enumerate(medicos, start=1):
        nome_med = medico['nome']
        crm = medico['crm']
        print(f'{indice}. Nome: {nome_med.ljust(5)} | CRM: {crm}')
    voltar_ao_menu_principal()

def cadastrar_medico():
    print('Cadastro Médico - HP Pedrada\n')
    nome = input('Qual o seu nome? ')
    idade = int(input('Qual a sua idade? '))
    
    # Solicita ao médico que digite o código para o gênero
    print('Digite o código para o gênero:')
    print('1 - Masculino')
    print('2 - Feminino')

    genero_codigo = input('Digite o código correspondente: ')

    # Validação simples para garantir que o usuário insira 1 ou 2
    while genero_codigo not in ('1', '2'):
        print('Opção inválida. Por favor, digite 1 para masculino e 2 para feminino.')
        genero_codigo = input('Digite 1 para masculino e 2 para feminino: ')

    # Mapeia o código do gênero para a string correspondente
    genero = 'Masculino' if genero_codigo == '1' else 'Feminino'
    
    endereco = input('Qual o seu endereço? ')
    
    print('Digite o código para o estado civil:')
    print('1 - Solteiro(a)')
    print('2 - Casado(a)')
    print('3 - Divorciado(a)')
    print('4 - Viúvo(a)')

    estado_civil_codigo = input('Digite o código correspondente: ')

    # Validação simples para garantir que o usuário insira um código válido
    while estado_civil_codigo not in ('1', '2', '3', '4'):
        print('Opção inválida. Por favor, digite um código válido.')
        estado_civil_codigo = input('Digite o código correspondente: ')

    # Mapeia o código do estado civil para a string correspondente
    estado_civil_map = {
        '1': 'Solteiro(a)',
        '2': 'Casado(a)',
        '3': 'Divorciado(a)',
        '4': 'Viúvo(a)'
    }
    estado_civil = estado_civil_map[estado_civil_codigo]
    cpf = int(input('Qual seu CPF? '))
    nome_pai_mae = input('Qual o nome da sua mãe ou do seu pai? (Digite "N/A" se não aplicável): ')
    crm = int(input('Digite o seu CRM: '))
    
    medico = {
        'nome': nome,
        'idade': idade,
        'genero': genero,
        'endereco': endereco,
        'estado_civil': estado_civil,
        'cpf': cpf,
        'nome_pai_mae': nome_pai_mae if nome_pai_mae.lower() != 'n/a' else None,  # Trata o caso "N/A"
        'crm': crm
    }
    
    voltar_ao_menu_principal()
    return medico

def exibir_informacoes_medico(medico):
    print('\nInformações do Médico:')
    print(f'Nome: {medico["nome"]}')
    print(f'Idade: {medico["idade"]}')
    print(f'Gênero: {medico["genero"]}')
    print(f'Endereço: {medico["endereco"]}')
    print(f'Estado Civil: {medico["estado_civil"]}')
    print(f'CPF: {medico["cpf"]}')
    print(f'Nome da Mãe ou Pai: {medico["nome_pai_mae"]}')
    print(f'CRM: {medico["crm"]}')

def alterar_dados_medico(lista_medicos):
    print('Alteração de Dados do Médico:')
    
    while True:
        # Exibe a lista de médicos disponíveis
        print('Escolha o número do médico que deseja alterar:')
        for i, medico in enumerate(lista_medicos):
            print(f'{i + 1} - {medico["nome"]}')

        try:
            indice_medico = int(input('Digite o número correspondente ao médico: ')) - 1
            if 0 <= indice_medico < len(lista_medicos):
                medico = lista_medicos[indice_medico]
                exibir_informacoes_medico(medico)

                # Chama a função para alterar os dados do médico
                print('\nEscolha a informação que deseja alterar:')
                print('1 - Nome')
                print('2 - Idade')
                print('3 - Gênero')
                print('4 - Endereço')
                print('5 - Estado Civil')
                print('6 - CPF')
                print('7 - Nome da Mãe ou Pai')
                print('8 - CRM')

                opcao = input('Digite o número da opção: ')

                if opcao == '1':
                    medico['nome'] = input('Novo nome: ')
                elif opcao == '2':
                    medico['idade'] = int(input('Nova idade: '))
                elif opcao == '3':
                    medico['genero'] = obter_identidade_genero()
                elif opcao == '4':
                    medico['endereco'] = input('Novo endereço: ')
                elif opcao == '5':
                    medico['estado_civil'] = obter_estado_civil()
                elif opcao == '6':
                    medico['cpf'] = int(input('Novo CPF: '))
                elif opcao == '7':
                    medico['nome_pai_mae'] = input('Novo nome da mãe ou pai: ')
                elif opcao == '8':
                    medico['crm'] = int(input('Novo CRM: '))
                else:
                    print('Opção inválida. Tente novamente.')

                print('Alterações concluídas. Informações atualizadas:')
                exibir_informacoes_medico(medico)

            else:
                print('Médico não encontrado.')

        except ValueError:
            print('Entrada inválida. Digite um número.')
        
        voltar_ao_menu_principal()




def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main() 


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def inicio():
    print(F' Seja bem vindo ao Hp Pedrada 2025')


def retorno():
    print(f'Voce Entrou no menu')


def finalizar_app():
    print('Finalizando o app')


def exibir_opcoes():
    print('1. Cadastrar Usuario')
    print('2. Cadastrar Medico')
    print('3. alterar dados Usuario')
    print('4. alterar dados Medico')
    print('5. Listar medico')
    print('6. exibir dados do Usuario')
    print('7. Agenda Medico')
    print('8. Marcar consulta')
    print('9. Excluir medico')
    print('10. Sair\n')


def escolher_opcao(usuario, lista_medicos):
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            usuario = cadastro_usuario()
        elif opcao_escolhida == 2:
            medico = cadastrar_medico()
        elif opcao_escolhida == 3: 
            alterar_informacoes_usuario(usuario)
        elif opcao_escolhida == 4: 
            alterar_dados_medico(lista_medicos)
        elif opcao_escolhida == 5:
            listar_medicos(lista_medicos)
        elif opcao_escolhida == 6:
            exibir_informacoes_usuario(usuario)
        elif opcao_escolhida == 7:
            pass
        elif opcao_escolhida == 8:
            pass
        elif opcao_escolhida == 9:
            pass
        elif opcao_escolhida == 10:
            finalizar_app()
        else: 
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    os.system('cls')
    inicio()
    usuario = None
    lista_medicos = []

    while True:
        exibir_opcoes()
        escolher_opcao(usuario, lista_medicos)


if __name__ == '__main__':  
    main()  

# Exemplo para exibir as informações do médico cadastrado.
#lista_medicos = []
#cadastrar_medico(lista_medicos)


# Exemplo para exibir as informações do usuário cadastrado. 
#novo_usuario = cadastro_usuario()
#exibir_informacoes_usuario(novo_usuario)
#alterar_informacoes_usuario(novo_usuario)

