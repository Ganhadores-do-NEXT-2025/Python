import os, time

consultas = [
            {'NumeroConsulta':'000001','NomeDoutor':'Dr. Gabriel Azevedo','Data':'25/07/25 - 13h00','Especialidade':'Cardiologista'},
            {'NumeroConsulta':'000002','NomeDoutor':'Dra. Isabella Azevedo','Data':'20/08/25 - 17h30','Especialidade':'Psiquiatra'}
            ]

historicos = [
            {'Data':'01/01/25 - 10h00', 'NomeDoutor':'Dr. Gabriel Azevedo','Especialidade':'Cardiologista'},
            {'Data':'02/02/25 - 20h00', 'NomeDoutor':'Dr. Isabella Azevedo','Especialidade':'Psiquiatra'}]

def limparTela():
    os.system('cls')

def listaMenu():
    limparTela()
    print("Bem-Vindo ao Agendador do hospital das clínicas".center(50))
    print("-"*50)
    print("1. 📅 Historico de Consultas")
    print("2. 🏥 Telemedicina")
    print("3. ❓ Dúvidas")
    print("4. 🚪 Sair\n")

    selecao = int(input("Digite qual opção deseja escolher: "))

    match selecao:
        case 1:
            historicoConsultas()
        case 2:
            telemedicina()
        case 3:
            duvidas()
        case 4:
            desligar()
        case _:
            print("Opção Inválida! Tente novamente... \n")
            time.sleep(3)
            os.system('cls')
            listaMenu()


def historicoConsultas():
    limparTela()
    print("HISTORICO DE CONSULTAS".center(50))
    print("-"*50)
    print("Veja abaixo as suas ultimas consultas\n")
    for historico in historicos:
        print(f'Data: {historico['Data']}')
        print(f'Dr(a): {historico['NomeDoutor']}')
        print(f'Especialidade: {historico['Especialidade']}\n')
    
    input("Digite qualquer tecla para voltar: ")
    listaMenu()

def telemedicina():
    limparTela()
    print("TELEMEDICINA".center(50))
    print("-"*50)
    print("1. 📅 Meus agendamentos")
    print("2. 🔄 Reagendar consulta")
    print("3. ❌ Cancelar consulta")
    print("4. Voltar\n")

    selecao = int(input("Digite qual opção deseja escolher: "))

    match selecao:
        case 1:
            meusAgendamentos()
        case 2:
            reagendarConsulta()
        case 3:
            cancelarConsulta()
        case 4:
            listaMenu()
        case _:
            print("Opção Inválida! Tente novamente... \n")
            time.sleep(3)
            os.system('cls')
            telemedicina()

def meusAgendamentos():
    limparTela()
    print("MEUS AGENDAMENTOS".center(50))
    print("-"*50)
    for consulta in consultas:
        print(f"Numero da Consulta: {consulta['NumeroConsulta']}")
        print(f"Dr(a): {consulta['NomeDoutor']}")
        print(f"Data da Consulta: {consulta['Data']}")
        print(f"Especialidade: {consulta['Especialidade']}\n")

    input("Digite qualquer tecla para voltar: ")
    telemedicina()

def reagendarConsulta():
    limparTela()
    print("REAGENDAMENTOS".center(50))
    print("-"*50)

    for consulta in consultas:
        print(f"Numero da Consulta: {consulta['NumeroConsulta']}")
        print(f"Dr(a): {consulta['NomeDoutor']}")
        print(f"Data da Consulta: {consulta['Data']}")
        print(f"Especialidade: {consulta['Especialidade']}\n")

    selecaoConsulta = input('Digite o numero da consulta que você deseja reagendar: ')

    consultaEncontrada = None
    for consulta in consultas:
        if consulta['NumeroConsulta'] == selecaoConsulta:
            consultaEncontrada = consulta
            break
    
    if consultaEncontrada:
        print(f'Consulta de numero {consulta["NumeroConsulta"]} encontrada!')
        nova_data = input('\nDigite qual a data desejada(Siga o padrão "01/01/25 - 00h30"): ')

        consulta['Data'] = nova_data
        limparTela()
        print("Data alterada com sucesso!\n")
        input("Digite qualquer tecla para voltar: ")
        telemedicina()
    else: 
        limparTela
        print("\nNumero de consulta não encontrado")
        time.sleep(2)
        telemedicina()

def cancelarConsulta():
    print("CANCELAMENTOS\n".center(50))
    print("-"*50)

    for consulta in consultas:
        print(f"Número da consulta: {consulta['NumeroConsulta']}")
        print(f"Dr(a).: {consulta['NomeDoutor']}")
        print(f"Data da consulta: {consulta['Data']}")
        print(f"Especialidade: {consulta['Especialidade']}\n")

    selecaoConsulta = input('Digite o numero da consulta que você deseja cancelar: ')

    consultaEncontrada = None
    for consulta in consultas:
        if selecaoConsulta == consulta['NumeroConsulta']:
            consultaEncontrada = consulta
            break

    if consultaEncontrada:
        limparTela()
        print('Consulta encontrada!\n')
        print('Tem certeza que deseja sair?\n')
        selecao = input("[S]im ou [N]ão: ").upper()

        match selecao:
            case 'S':
                limparTela()
                consultas.remove(consulta)
                print("Consulta Cancelada com Sucesso!\n")

                input("Digite qualquer tecla para voltar: ")
                telemedicina()
            case 'N':
                limparTela()
                print('Retornando...')
                time.sleep(2)
                telemedicina()
    else:
        print('Consulta não encontrada')
        input("Digite qualquer tecla para voltar: ")
        telemedicina()

def duvidas():
    limparTela()
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
            sobrePrograma()
        case 2:
            acessePortal()
        case 3:
            duvidasTele()
        case 4:
            gerenciarConsulta()
        case 5:
            duvidasTecnicas()
        case 6:
            dadosEstatisticas()
        case 7:
            listaMenu()

def sobrePrograma():
    limparTela()
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

def acessePortal():
    limparTela()
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

def duvidasTele():
    limparTela()
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
    
def gerenciarConsulta():
    limparTela()
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

def duvidasTecnicas():
    limparTela()
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

def dadosEstatisticas():
    limparTela()
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
    limparTela()
    print("\nTem certeza que deseja sair?")
    selecao = input("[S]im ou [N]ão: ").upper()

    if selecao == "S":
        limparTela()
        print("FINALIZANDO O PROGRAMA... ATÉ BREVE!".center(50))
        print("-"*50)
        time.sleep(3)
        limparTela()
        exit()
    else:
        listaMenu()

listaMenu()
