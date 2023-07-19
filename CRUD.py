import mysql.connector
conexao = mysql.connector.connect(
	host='localhost',
	user='root',
	password='123456789',
	database='db_1',
	)

n = input('nome produto: ')
v = input('valor: ')
#quando for adcionar por uso de variaveis, colocar as variaveis que tem input antes do cursor=conexao.cursor()

cursor = conexao.cursor()

#CRUD

nome_produto = n
valor = v

#CREATE
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}",{valor})' 
cursor.execute(comando)
conexao.commit()#quando editar algo no DB precisa dessa linha de cód
#resultado = cursor.fetchall() #ler algo no DB

#READ
comando_leitura = f'SELECT * FROM vendas' 
cursor.execute(comando_leitura)
resultado=cursor.fetchall()
print(resultado)

#UPDATE
nome_produto = 'toddy'
valor_produto = 8
comando_update = f'UPDATE vendas SET valor = {valor_produto} WHERE nome_produto = "{nome_produto}"'  
cursor.execute(comando_update)
conexao.commit()#quando editar algo no DB precisa dessa linha de cód

#READ
comando_leitura = f'SELECT * FROM vendas' 
cursor.execute(comando_leitura)
resultado=cursor.fetchall()
print(resultado)

#DELETE

nome_produto = 'docinho'
comando_update = f'DELETE FROM vendas  WHERE nome_produto = "{nome_produto}"'  
cursor.execute(comando_update)
conexao.commit()#quando editar algo no DB precisa dessa linha de cód





cursor.close()
conexao.close()
