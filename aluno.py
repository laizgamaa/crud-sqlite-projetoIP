import sqlite3
import subprocess as sp

"""
Código do banco de dados.
"""

def create_table():
	conn = sqlite3.connect('alunos.sqlite')
	cursor = conn.cursor()
	query = '''
	    CREATE TABLE IF NOT EXISTS aluno(
	    	id INTEGER PRIMARY KEY, 
	    	roll INTEGER, 
	    	name TEXT
	    )
	'''
	cursor.execute(query)

	conn.commit()
	conn.close()

### Cria o banco de dados ###

def adiciona_aluno(roll,name):
	conn = sqlite3.connect('alunos.sqlite')
	cursor = conn.cursor()
	query = '''
	    INSERT INTO aluno( roll, name )
	    	        VALUES ( ?,? )
	'''

	cursor.execute(query,(roll,name))

	conn.commit()
	conn.close()

def obtem_alunos():
	conn = sqlite3.connect('alunos.sqlite')
	cursor = conn.cursor()
	query = '''
	    SELECT roll, name
	    FROM aluno
	'''

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def obtem_aluno_by_roll(roll):
	conn = sqlite3.connect('alunos.sqlite')
	cursor = conn.cursor()
	query = '''
	    SELECT roll, name
	    FROM aluno
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def atualiza_aluno(roll,name):
	conn = sqlite3.connect('alunos.sqlite')
	cursor = conn.cursor()
	query = '''
	    UPDATE aluno
	    SET name = ?
	    WHERE roll = ?
	'''

	cursor.execute(query,(name,roll))

	conn.commit()
	conn.close()


def apaga_aluno(roll):
	conn = sqlite3.connect('alunos.sqlite')
	cursor = conn.cursor()
	query = '''
	    DELETE
	    FROM aluno
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows



create_table()



def adiciona_dados(id_,name):
	adiciona_aluno(id_,name)
def obtem_dados():
	return obtem_alunos()

def exibe_dados():
	alunos = obtem_dados()
	for aluno in alunos:
		print(aluno)

def exibe_dados_by_id(id_):
	alunos = obtem_aluno_by_roll(id_)
	if not alunos:
		print("Nenhum dado encontrado",id_)
	else:
		print (alunos)

def select():

	sel = input("1.Adicionar aluno\n 2.Exibir alunos cadastrados\n 3.Atualizar aluno\n 4.Apagar aluno do sistema\n 5.Sair\n\n")
	
	if sel=='1':
		id_ = int(input('CPF: '))
		name = input('Nome: ')
		adiciona_dados(id_,name)
	elif sel=='2':
		sp.call('clear',shell=True)
		exibe_dados()
		input("\n\n Digite enter para retornar")
	
	elif sel=='3':
		id__ = int(input('Informar CPF: '))
		exibe_dados_by_id(id__)
		print()
		name = input('Nome: ')
		atualiza_aluno(id__,name)
		input("\n\n Aluno devidamente atualizado \nDigite enter para retornar")
	elif sel=='4':
		id__ = int(input('Informar CPF: '))
		exibe_dados_by_id(id__)
		apaga_aluno(id__)
		input("\n\nO aluno foi apagado do sistema \nDigite enter para retornar")
	else:
		return 0;
	return 1;

while(select()):
	pass
