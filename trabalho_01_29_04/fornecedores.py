import psycopg2
from psycopg2 import Error


class Fornecedores:
    # Inicia Conexao com o banco
    def setConnection(self):
        self.__con = psycopg2.connect(
            host="localhost",
            database="teste_asa",
            user="postgres",
            password="hambotregga"
        )
        self.__cur = self.__con.cursor()

    # Encerra Conexao com o banco
    def killConnection(self):
        self.__con.close()
        self.__cur.close()


    def createTable(self):
        try:
            self.setConnection()
            create_table_query = '''CREATE TABLE tb_fornecedores 
                    (id_fornecedor SERIAL PRIMARY KEY, 
                    cnpj VARCHAR(60),
                    razaoSocial VARCHAR(200),
                    telefone VARCHAR(60),
                    contato VARCHAR(60),
                    endereco varchar(100),
                    fg_ativo INT default 1); '''
            self.__cur.execute(create_table_query)
            self.__con.commit()
            self.killConnection()
            res = True
        except (Exception, psycopg2.Error) as error:
            if(self.__con):
                print("Failed to create table", error)
            res = False
        return res


    def insertFornecedor(self, cnpj, razaoSocial, telefone, endereco, contato):
        try:
            self.setConnection()
            insert_table_query = '''INSERT INTO tb_fornecedores (cnpj, razaoSocial, 
                telefone, endereco, contato) VALUES (%s, %s, %s, %s, %s)'''
            values = (cnpj, razaoSocial, telefone, endereco, contato)
            self.__cur.execute(insert_table_query, values)
            self.__con.commit()
            count = self.__cur.rowcount
            print(count, "Record inserted successfully into table")
            self.killConnection()
            res = True
        except (Exception, psycopg2.Error) as error:
            if(self.__con):
                print("Failed to insert record into table", error)
            res = False
        return res


    def consultaFornecedores(self):
        self.setConnection()
        select_query = 'select * from tb_fornecedores'
        self.__cur.execute(select_query)
        fornecedores = self.__cur.fetchall()
        self.killConnection()
        return fornecedores
