import sqlite3
import subprocess as sp

"""
Código do banco de dados.
"""

def create_table_discip():
	conn = sqlite3.connect('disciplinas.sqlite')
	cursor = conn.cursor()
	query = '''
	    CREATE TABLE IF NOT EXISTS disciplina(
	    	codigo INTEGER PRIMARY KEY, 
	    	roll INTEGER, 
	    	name TEXT
	    )
	'''

	cursor.execute(query)

	conn.commit()
	conn.close()


def adiciona_discip(roll,name):
	conn = sqlite3.connect('disciplinas.sqlite')
	cursor = conn.cursor()
	query = '''
	    INSERT INTO disciplina( roll, name )
	    	        VALUES ( ?,?)
	'''

	cursor.execute(query,(roll,name))

	conn.commit()
	conn.close()


def obtem_discip():
	conn = sqlite3.connect('disciplinas.sqlite')
	cursor = conn.cursor()
	query = '''
	    SELECT roll, name
	    FROM disciplina
	'''

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def obtem_discip_by_roll(roll):
	conn = sqlite3.connect('disciplinas.sqlite')
	cursor = conn.cursor()
	query = '''
	    SELECT roll, name
	    FROM disciplina
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def atualiza_discip(roll,name):
	conn = sqlite3.connect('disciplinas.sqlite')
	cursor = conn.cursor()
	query = '''
	    UPDATE disciplina
	    SET name = ?
	    WHERE roll = ?
	'''

	cursor.execute(query,(name,roll))

	conn.commit()
	conn.close()


def apaga_disciplina(roll):
	conn = sqlite3.connect('disciplinas.sqlite')
	cursor = conn.cursor()
	query = '''
	    DELETE
	    FROM disciplina
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows


create_table_discip()



def adiciona_dados_discip(id_,name):
	adiciona_discip(id_,name)
def obtem_dados_discip():
	return obtem_discip()

def exibe_dados_discip():
	disciplinas = obtem_dados_discip()
	for disciplina in disciplinas:
		print(disciplina)

def exibe_dados_by_id_discip(id_):
	disciplinas = obtem_discip_by_roll(id_)
	if not disciplinas:
		print("Dado não encontrado",id_)
	else:
		print (disciplinas)

def select():
	sp.call('clear',shell=True)
	sel = input("1.Adicionar disciplina\n 2.Exibir disciplinas do sistema\n 3.Atualizar disciplina\n 4.Apagar disciplina do sistema\n 5.Sair\n\n")
	
	if sel=='1':
		sp.call('clear',shell=True)
		id_ = int(input('Código da disciplina: '))
		name = input('Nome da disciplina: ')
		adiciona_dados_discip(id_,name)
	elif sel=='2':
		sp.call('clear',shell=True)
		exibe_dados_discip()
		input("\n\nDigite enter para retornar")

	elif sel=='3':
		sp.call('clear',shell=True)
		id__ = int(input('Informar código da disciplina: '))
		exibe_dados_by_id_discip(id__)
		print()
		name = input('Nome da disciplina: ')
		atualiza_discip(id__,name)
		input("\n\nDisciplina devidamente alterada \nDigite enter para retornar")
	elif sel=='4':
		sp.call('clear',shell=True)
		id__ = int(input('Informar código da disciplina: '))
		exibe_dados_by_id_discip(id__)
		apaga_disciplina(id__)
		input("\n\nA disciplina foi apagada do sistema \nDigite enter para retornar")
	else:
		return 0;
	return 1;


while(select()):
	pass