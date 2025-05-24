import os, time

consultas = [
            {'numero_consulta':'000001','nome_doutor':'Dr. Gabriel Azevedo','data':'25/07/25 - 13h00','especialidade':'Cardiologista'},
            {'numero_consulta':'000002','nome_doutor':'Dra. Isabella Azevedo','data':'20/08/25 - 17h30','especialidade':'Psiquiatra'}
            ]

historicos = [
            {'data':'01/01/25 - 10h00', 'nome_doutor':'Dr. Gabriel Azevedo','especialidade':'Cardiologista'},
            {'data':'02/02/25 - 20h00', 'nome_doutor':'Dr. Isabella Azevedo','especialidade':'Psiquiatra'}]

def limpar_tela():
    os.system('cls')

def lista_menu():
    limpar_tela()
    print("Bem-Vindo ao Agendador do hospital das clínicas".center(50))
    print("-"*50)
    print("1. 📅 Historico de Consultas")
    print("2. 🏥 Telemedicina")
    print("3. ❓ Dúvidas")
    print("4. 🚪 Sair\n")

    try:
        selecao = int(input("Digite qual opção deseja escolher: "))
    except ValueError:
        print("Valor inválido! Por favor, digite apenas números.\n")
        time.sleep(2)
        lista_menu()
        return

    match selecao:
        case 1:
            historico_consultas()
        case 2:
            telemedicina()
        case 3:
            duvidas()
        case 4:
            desligar()
        case _:
            print("Opção Inválida! Tente novamente... \n")
            time.sleep(2)
            lista_menu()


def historico_consultas():
    limpar_tela()
    print("HISTORICO DE CONSULTAS".center(50))
    print("-"*50)
    print("Veja abaixo as suas ultimas consultas\n")
    for historico in historicos:
        print(f"Data: {historico['data']}")
        print(f"Dr(a): {historico['nome_doutor']}")
        print(f"Especialidade: {historico['especialidade']}\n")
    
    input("Digite qualquer tecla para voltar: ")
    lista_menu()

def telemedicina():
    limpar_tela()
    print("TELEMEDICINA".center(50))
    print("-"*50)
    print("1. 📅 Meus agendamentos")
    print("2. 🔄 Reagendar consulta")
    print("3. ❌ Cancelar consulta")
    print("4. Voltar\n")

    try:
        selecao = int(input("Digite qual opção deseja escolher: "))
    except ValueError:
        print("Valor inválido! Por favor, digite apenas números.\n")
        time.sleep(2)
        telemedicina()
        return

    match selecao:
        case 1:
            meus_agendamentos()
        case 2:
            reagendar_consulta()
        case 3:
            cancelar_consulta()
        case 4:
            lista_menu()
        case _:
            print("Opção Inválida! Tente novamente... \n")
            time.sleep(3)
            os.system('cls')
            telemedicina()

def meus_agendamentos():
    limpar_tela()
    print("MEUS AGENDAMENTOS".center(50))
    print("-"*50)
    for consulta in consultas:
        print(f"Numero da Consulta: {consulta['numero_consulta']}")
        print(f"Dr(a): {consulta['nome_doutor']}")
        print(f"Data da Consulta: {consulta['data']}")
        print(f"Especialidade: {consulta['especialidade']}\n")

    input("Digite qualquer tecla para voltar: ")
    telemedicina()

def atualizar_data_consulta(numero, nova_data):
    for consulta in consultas:
        if consulta['numero_consulta'] == numero:
            consulta['data'] = nova_data
            return True
    return False

def reagendar_consulta():
    limpar_tela()
    print("REAGENDAMENTOS".center(50))
    print("-"*50)

    for consulta in consultas:
        print(f"Numero da Consulta: {consulta['numero_consulta']}")
        print(f"Dr(a): {consulta['nome_doutor']}")
        print(f"Data da Consulta: {consulta['data']}")
        print(f"Especialidade: {consulta['especialidade']}\n")

    selecao_consulta = input('Digite o número da consulta que você deseja reagendar: ')
    nova_data = input('Digite a nova data (formato: 01/01/25 - 00h30): ')

    if atualizar_data_consulta(selecao_consulta, nova_data):
        limpar_tela()
        print("Consulta reagendada com sucesso!\n")
    else:
        print("Número da consulta não encontrado.\n")
    input("Digite qualquer tecla para voltar: ")
    telemedicina()

def cancelar_consulta():
    print("CANCELAMENTOS\n".center(50))
    print("-"*50)

    for consulta in consultas:
        print(f"Número da consulta: {consulta['numero_consulta']}")
        print(f"Dr(a).: {consulta['nome_doutor']}")
        print(f"Data da consulta: {consulta['data']}")
        print(f"Especialidade: {consulta['especialidade']}\n")

    selecao_consulta = input('Digite o numero da consulta que você deseja cancelar: ')

    consulta_encontrada = None
    for consulta in consultas:
        if selecao_consulta == consulta['numero_consulta']:
            consulta_encontrada = consulta
            break

    if consulta_encontrada:
        limpar_tela()
        print('Consulta encontrada!\n')
        print('Tem certeza que deseja sair?\n')
        selecao = input("[S]im ou [N]ão: ").upper()

        match selecao:
            case 'S':
                limpar_tela()
                consultas.remove(consulta)
                print("Consulta Cancelada com Sucesso!\n")

                input("Digite qualquer tecla para voltar: ")
                telemedicina()
            case 'N':
                limpar_tela()
                print('Retornando...')
                time.sleep(2)
                telemedicina()
    else:
        print('Consulta não encontrada')
        input("Digite qualquer tecla para voltar: ")
        telemedicina()

def duvidas():
    limpar_tela()
    print("MENU DE TÓPICOS".center(50))
    print("-"*50)
    print("1. 📌 Sobre o Programa")
    print("2. 📱 Acesso ao Portal")
    print("3. 🏥 Teleconsultas")
    print("4. 🔄 Gerenciamento de Consultas")
    print("5. ❓ Dúvidas Técnicas")
    print("6. 📊 Dados e Estatísticas")
    print("7. ⏹️ Sair do FAQ\n")

    selecao = int(input("Digite qual opção deseja escolher: "))

    match selecao:
        case 1:
            sobre_programa()
        case 2:
            acesse_portal()
        case 3:
            duvidas_tele()
        case 4:
            gerenciar_consulta()
        case 5:
            duvidas_tecnicas()
        case 6:
            dados_estatisticas()
        case 7:
            lista_menu()

def sobre_programa():
    limpar_tela()
    print("📌 SOBRE O PROGRAMA".center(50))
    print("\nO que é Saúde Digital?")
    print("A Saúde Digital é uma iniciativa que utiliza tecnologia para proporcionar")
    print("atendimentos virtuais (teleconsultas), melhorando o acesso aos serviços")
    print("de saúde, especialmente para pacientes com dificuldade de locomoção ou")
    print("que residem em áreas remotas.\n")
    
    print("Quais são os benefícios da Saúde Digital?")
    print("- Maior comodidade e praticidade para os pacientes")
    print("- Redução de barreiras geográficas")
    print("- Diminuição do absenteísmo nas consultas")
    print("- Acesso mais fácil a especialistas")
    print("- Economia de tempo e recursos\n")
    
    input("Digite qualquer tecla para voltar: ")
    duvidas()

def acesse_portal():
    limpar_tela()
    print("📱 ACESSO AO PORTAL".center(50))
    print("\nComo faço meu primeiro acesso ao Portal do Paciente?")
    print("1. Baixe o aplicativo 'Portal do Paciente HC' na Play Store (Android) ou App Store (iPhone)")
    print("2. Clique em 'Cadastrar Senha'")
    print("3. Insira seu CPF e clique em 'Localizar Paciente'")
    print("4. Confirme seus dados pessoais e cadastre uma senha")
    print("5. Acesse com CPF e senha cadastrados\n")
    
    print("Esqueci minha senha, o que fazer?")
    print("No login do aplicativo, clique em 'Esqueci minha senha' e siga as")
    print("instruções para redefinição.\n")
    
    input("Digite qualquer tecla para voltar: ")
    duvidas()

def duvidas_tele():
    limpar_tela()
    print("🏥 TELECONSULTAS".center(50))
    print("\nComo agendar uma teleconsulta?")
    print("1. Converse com seu médico para verificar a possibilidade de atendimento virtual")
    print("2. Se elegível, dirija-se ao setor de Saúde Digital para agendamento")
    print("3. No dia marcado, acesse o Portal do Paciente e entre na sala de teleconsulta\n")
    
    print("Quais equipamentos preciso para uma teleconsulta?")
    print("- Celular ou computador com internet")
    print("- Câmera e microfone funcionais")
    print("- Aplicativo 'Portal do Paciente HC' instalado\n")
    
    print("O que fazer se não consigo ver minha consulta agendada?")
    print("No menu do aplicativo, clique em 'Teleconsulta' para visualizar seus")
    print("agendamentos. Se ainda não aparecer, entre em contato com o setor de Saúde Digital.\n")
    
    input("Digite qualquer tecla para voltar: ")
    duvidas()
    
def gerenciar_consulta():
    limpar_tela()
    print("🔄 GERENCIAMENTO DE CONSULTAS".center(50))
    print("\nComo reagendar uma consulta?")
    print("1. Acesse a seção 'Telemedicina' no aplicativo")
    print("2. Selecione 'Meus agendamentos'")
    print("3. Escolha a consulta e a opção 'Reagendar'")
    print("4. Informe a nova data desejada\n")
    
    print("Posso cancelar uma consulta pelo aplicativo?")
    print("Sim, acesse 'Telemedicina' > 'Meus agendamentos' e selecione a opção")
    print("'Cancelar consulta'.\n")

    input("Digite qualquer tecla para voltar: ")
    duvidas()

def duvidas_tecnicas():
    limpar_tela()
    print("❓ DÚVIDAS TÉCNICAS".center(50))
    print("\nO que fazer se o aplicativo não funciona corretamente?")
    print("- Verifique sua conexão com a internet")
    print("- Atualize o aplicativo na loja de aplicativos")
    print("- Reinicie seu dispositivo")
    print("- Caso persista, procure o setor de Saúde Digital para suporte\n")
    
    print("Onde encontro mais informações sobre o programa?")
    print("Visite o site www.redelucymontoro.org.br ou dirija-se ao setor de")
    print("Saúde Digital no endereço: Rua Domingo de Soto, 100 - Jardim Vila Mariana.\n")

    input("Digite qualquer tecla para voltar: ")
    duvidas()

def dados_estatisticas():
    limpar_tela()
    print("📊 DADOS E ESTATÍSTICAS".center(50))
    print("\nQual a taxa atual de absenteísmo nas teleconsultas?")
    print("O programa tem como meta reduzir a taxa de absenteísmo de 20% para")
    print("menos de 10% através de melhorias na usabilidade e orientação aos pacientes.\n")
    
    print("A teleconsulta tem a mesma qualidade que o atendimento presencial?")
    print("Sim, as teleconsultas são realizadas com a mesma equipe médica e")
    print("multidisciplinar, mantendo os padrões de qualidade do atendimento presencial.\n")

    input("Digite qualquer tecla para voltar: ")
    duvidas()

def desligar():
    limpar_tela()
    print("\nTem certeza que deseja sair?")
    selecao = input("[S]im ou [N]ão: ").upper()

    if selecao == "S":
        limpar_tela()
        print("FINALIZANDO O PROGRAMA... ATÉ BREVE!".center(50))
        print("-"*50)
        time.sleep(3)
        limpar_tela()
        exit()
    else:
        lista_menu()

lista_menu()
