import pickle
import os

#cria o arquivo binário
arquivo = open('file.db', 'wb')
for i in range(10):
    pickle.dump(i, arquivo)
arquivo.close()
print('Arquivo criado com sucesso.')

db = {}

def linha():
    l = input('---*---' * 5)
    return l

def mostrarMenu():
    os.system('cls')
    print('Existe(m)' + str(len(db))+' candidato (s) registrado(s).\n\n')
    print('Escolha uma opção')
    print('1 - Incluir candidato')
    print('2 - Consultar candidato')
    print('3 - Modificar candidato')
    print('4 - Excluir Candidato')
    print('5 - Listar todos os dados dos candidatos')
    print('6 - Listar votos por candidatos')
    print('7 - Listar votos por região')
    print('8 - Sair')
    return int(input(''))

#verifica se tem dados duplicados
def existeRegistro(codigo):
    duplicated = False
    if codigo in db.keys():
        duplicated = True
    return duplicated
    
#inserir candidato
def inserir():
    candidato = {}
    codigo = input('Digite o código do candidato\n')
    if existeRegistro(codigo):
        print('Já existe um candidato cadastrado com este código, digite outro')
        frase = print('\033[31mpressione para voltar ao menu\033[m')
        principal()
    else:
        candidato['cod_candidato'] = codigo
        candidato['nome'] =input('Digite o nome do candidato\n')
        candidato['cargo'] = input('Digite o cargo do candidato\n')
        candidato['regiao'] = input('Digite a região do candidato\n')
        candidato['num_votos'] = int(input('Digite a quantidade de votos do candidato\n'))
        db[codigo] = candidato
        principal()

def  mostrar(codigo):
    print('Código: ' + db[codigo]['cod_candidato'])
    print('Nome: ' + db[codigo]['nome'])  
    print('Cargo: ' + db[codigo]['cargo'])
    print('Região: ' + db[codigo]['regiao'])
    print('Número de votos: ' + str(db[codigo]['num_votos']))

def mostrarVotosCandidatos(codigo):
    print('Nome: ' + db[codigo]['nome'])
    print('Numero de votos: ' + str(db[codigo]['num_votos']))

def mostrarVotosRegiao(codigo):
    print('Nome: ' + db[codigo]['regiao'])
    print('Numero de votos: ' + str(db[codigo]['num_votos']))

#lista todos os candidatos pelo código
def listar():
    codigo = input('Digite o código do candidato\n')
    if existeRegistro(codigo):
        mostrar(codigo)
        frase = print('\033[31mpressione para voltar ao menu\033[m')
        principal()
    else:
        print('Registro não encontrado')
        frase = print('\033[31mpressione para voltar ao menu\033[m')
        principal()

#modifica o arquivo
def modificar():
    candidato = {}
    codigo = input('Digite o código do candidato\n')
#confirma que existe o candidato pelo código
    if existeRegistro(codigo):
        candidato['codigo'] = codigo
        candidato['nome'] = input('Digite o nome do candidato: ')
        candidato['cargo'] = input('Digite o cargo do candidato: ')
        candidato['região'] = input('Digite a região do candidato: ')
        candidato['num_votos'] = int(input('Digite a quantidade de votos: '))
        db[codigo] = candidato
        principal()
    else:
        print('\033[31mRegistro não encontrado.\033[m')
        frase = print('\033[31mpressione para voltar ao menu\033[m')
    principal()

#deletar do arquivo
def remover():
    codigo = input('Digite o código do candidato:\n')
#confirma se o arquivo existe
    if existeRegistro(codigo):
        del(db[codigo])
        print('Registro excluído com sucesso')
        frase = print('\033[31mpressione para voltar ao menu\033[m')
        principal()
    else:
        print('\033[31mRegistro não encontrado.\033[m')
        frase = print('\033[31mpressione para voltar ao menu\033[m')
    principal()

def list():
    if len(db) > 0:
        for codigo in db.keys():
            mostrar(codigo)
            linha()
        frase = print('\033[31mpressione para voltar ao menu\033[m')
        principal()
    else:
        print('\033[31mNão há registro a serem exibidos.\033[m')
        frase = print('\033[31mpressione para voltar ao menu\033[m')
        principal()

def votosCandidatos():
    if len(db) > 0:
        for codigo in db.keys():
            mostrarVotosCandidatos(codigo)
            linha()
        frase = print('\033[31mpressione para voltar ao menu\033[m')
        principal()
    else:
        print('Não há registros a serem exibidos')
        frase = print('\033[31mpressione para voltar ao menu\033[m')
        principal()

def votosRegiao():
    regioes = dict()
    for candidato in db.values():
        regioes[candidato['regiao']] = regioes.get(candidato['regiao'], 0) + candidato['num_votos']
    print('Total de votos por região: '+ str(regioes))
    frase = print('\033[31mpressione para voltar ao menu\033[m')
    principal()

def principal():
    while True:
        try:
            option = mostrarMenu()
            if(option ==1):
                inserir()
            elif(option == 2):
                listar()
            elif(option == 3):
                modificar()
            elif(option == 4):
                remover()
            elif(option == 5):
                list()
            elif(option == 6):
                votosCandidatos()
            elif(option == 7):
                votosRegiao()
            elif(option == 8):
                print('\033[31mSaindo do programa\033[m')
                exit()
            else:
                print('\033[31mPor favor selecione uma opção válida.\033[m')
        except (ValueError):
            print('\033[31mDigite uma opção válida.\033[m')
        principal()

principal()    