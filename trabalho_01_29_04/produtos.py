import psycopg2
from psycopg2 import Error


class Produtos:

	### Inicia Conexao com o banco
    def setConnection(self):
        self.__con = psycopg2.connect(
            host="localhost",
            database="teste_asa",
            user="postgres",
            password="hambotregga"
        )
        self.__cur = self.__con.cursor()

    ### Encerra Conexao com o banco
    def killConnection(self):
        self.__con.close()
        self.__cur.close()
		
    def createTable(self):
        try:
            self.setConnection()
            create_table_query = '''CREATE TABLE tb_produtos 
                (id_produto SERIAL PRIMARY KEY, 
                id_fornecedor INT references tb_fornecedores(id_fornecedor) NOT NULL, 
                id_categoria INT references tb_categorias(id_categoria) NOT NULL, 
                nomeProduto VARCHAR(60),
                descricaoProduto VARCHAR(200),
                valorUnitario NUMERIC,
                quantidade INT,
                quantidadeMinima INT,
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

    def insertProduto(self, id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima):
        try:
            self.setConnection()
            insert_query = '''INSERT INTO tb_produtos (id_fornecedor, id_categoria, 
			nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            values = (id_fornecedor, id_categoria, nomeProduto,
                      descricaoProduto, valorUnitario, quantidade, quantidadeMinima)
            self.__cur.execute(insert_query, values)
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

    def getprecoByIdProduto(self, where):
        self.setConnection()
        select_query = "select valorUnitario from tb_produtos " + where
        self.__cur.execute(select_query)
        preco = self.__cur.fetchone()
        self.killConnection()
        return preco

    def consultaProdutos(self):
        self.setConnection()
        select_query = 'select * from tb_produtos'
        self.__cur.execute(select_query)
        produtos = self.__cur.fetchall()
        self.killConnection()
        return produtos
