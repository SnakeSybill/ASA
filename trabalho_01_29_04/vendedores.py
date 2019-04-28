import psycopg2
from psycopg2 import Error

class Vendedores:

	### Inicia Conexao com o banco
	def setConnection(self):
		self.__con = psycopg2.connect(
        	host = "localhost",
        	database = "teste_asa",
        	user = "postgres",
        	password = "hambotregga"
    	)
		self.__cur = self.__con.cursor()

	### Encerra Conexao com o banco
	def killConnection(self):
		self.__con.close()
		self.__cur.close()
	
	### Criacao da tabela tb_vendedores
	def createTable(self): 
		try:
			self.setConnection()
			create_table_query = '''CREATE TABLE tb_vendedores 
                (id_vendedor SERIAL PRIMARY KEY, 
                cpf VARCHAR(60),
                nome VARCHAR(200),
                telefone VARCHAR(60),
                carteiraTrabalho VARCHAR(60),
                dataAdmissao timestamp,
                fg_ativo INT default 1); '''
            # cursor, connection = connect()
			self.__cur.execute(create_table_query)
			self.__con.commit()
			self.killConnection()
			res = True
		except (Exception, psycopg2.Error) as error :
				if(self.__con):
					print("Failed to create table", error) 
					res = False
		return res

	### Inicio metodos CRUD
	def insertVendedor(self, cpf, nome, carteiraTrabalho, telefone):
		self.setConnection()
		self.__cur.execute('insert into tb_vendedores (cpf, nome, carteiraTrabalho, telefone, dataAdmissao) values (%s, %s, %s, %s, NOW())', (cpf, nome, carteiraTrabalho, telefone))
		self.__con.commit()
		count = self.__cur.rowcount
		print(count, "Record inserted successfully into table")
		self.killConnection()
		
	def deleteVendedor(self, id_vendedor):
		self.setConnection()
		self.__cur.execute("delete from tb_vendedores where id_vendedor = " + str(id_vendedor))
		print("Record deleted successfully from the table")
		self.__con.commit()
		self.killConnection()

	def updateVendedor(self, cpf, nome, telefone, carteiraTrabalho, dataAdmissao, fg_ativo, id_vendedor):
		self.setConnection()
		self.__cur.execute("update tb_vendedores set cpf = %s, nome = %s,  dataAdmissao = NOW() where id_vendedor = " + str(id_vendedor), (cpf, nome))
		print("Record updated successfully from the table")
		self.__con.commit()
		self.killConnection()

	def consultaVendedores(self):
		self.setConnection()
		self.__cur.execute("select * from tb_vendedores ")
		rows = self.__cur.fetchall()
		self.killConnection()
		return rows
		
	### Fim metodos CRUD
