import sqlite3
import subprocess as sp


def create_table_prof():
	conn = sqlite3.connect('professor.sqlite')
	cursor = conn.cursor()
	query = '''
	    CREATE TABLE IF NOT EXISTS professor(
	    	id INTEGER PRIMARY KEY, 
	    	roll INTEGER, 
	    	name TEXT,
	        departamento TEXT
	    )
	'''

	cursor.execute(query)

	conn.commit()
	conn.close()


def adiciona_prof(roll,name,departamento):
	conn = sqlite3.connect('professor.sqlite')
	cursor = conn.cursor()
	query = '''
	    INSERT INTO professor( roll, name, departamento )
	    	        VALUES ( ?,?,? )
	'''

	cursor.execute(query,(roll,name,departamento))

	conn.commit()
	conn.close()


def obtem_prof():
	conn = sqlite3.connect('professor.sqlite')
	cursor = conn.cursor()
	query = '''
	    SELECT roll, name, departamento
	    FROM professor
	'''

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def obtem_prof_by_roll(roll):
	conn = sqlite3.connect('professor.sqlite')
	cursor = conn.cursor()
	query = '''
	    SELECT roll, name, departamento
	    FROM professor
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def atualiza_prof(roll,name,departamento):
	conn = sqlite3.connect('professor.sqlite')
	cursor = conn.cursor()
	query = '''
	    UPDATE professor
	    SET name = ?, departamento = ?
	    WHERE roll = ?
	'''

	cursor.execute(query,(name,departamento,roll))

	conn.commit()
	conn.close()

def apaga_prof(roll):
	conn = sqlite3.connect('professor.sqlite')
	cursor = conn.cursor()
	query = '''
	    DELETE
	    FROM professor
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows



create_table_prof()



def adiciona_dados_prof(id_,name,departamento):
	adiciona_prof(id_,name,departamento)
def obtem_dados_prof():
	return obtem_prof()

def exibe_dados_prof():
	professores = obtem_dados_prof()
	for professor in professores:
		print(professor)

def exibe_dados_by_id_prof(id_):
	professor = obtem_prof_by_roll(id_)
	if not professor:
		print("Nenhum dado encontrado",id_)
	else:
		print (professor)

def select():
	sp.call('clear',shell=True)
	sel = input("1.Adicionar professor\n 2.Exibir professores cadastrados\n 3.Atualizar informação de professor\n 4.Apagar professor do sistema\n\n")

	
	if sel=='1':
		sp.call('clear',shell=True)
		id_ = int(input('CPF: '))
		name = input('Nome: ')
		departamento = input('Departamento: ')
		adiciona_dados_prof(id_,name,departamento)
	elif sel=='2':
		sp.call('clear',shell=True)
		exibe_dados_prof()
		input("\n\nDigite enter para retornar")
	elif sel=='3':
		sp.call('clear',shell=True)
		id__ = int(input('Inserir cpf: '))
		exibe_dados_by_id_prof(id__)
		print()
		name = input('Nome: ')
		departamento = input('Departamento: ')
		atualiza_prof(id__,name,departamento)
		input("\n\nProfessor devidamente atualizado \nDigite enter para retornar")
	elif sel=='4':
		sp.call('clear',shell=True)
		id__ = int(input('CPF: '))
		exibe_dados_by_id_prof(id__)
		apaga_prof(id__)
		input("\n\nO professor foi apagado do sistema \nDigite enter para retornar")
	else:
		return 0;
	return 1;


while(select()):
	pass