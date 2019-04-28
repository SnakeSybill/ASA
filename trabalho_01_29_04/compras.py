import psycopg2
from psycopg2 import Error

class Compras:
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
            create_table_query = '''CREATE TABLE tb_compras 
                (id_compra SERIAL PRIMARY KEY, 
                id_produto INT references tb_produtos(id_produto) NOT NULL,
                id_fornecedor INT references tb_fornecedores(id_fornecedor) NOT NULL, 
                id_categoria INT references tb_categorias(id_categoria) NOT NULL, 
                dataCompra timestamp,
                valorTotal NUMERIC,
                quantidade INT,
                fg_ativo INT default 1); '''
            self.__cur.execute(create_table_query)
            self.__con.commit()
            self.killConnection()
            res = True
        except (Exception, psycopg2.Error) as error :
            if(self.__con):
                print("Failed to create table", error) 
            res = False
        return res
    
    def insertCompra(self, id_fornecedor, id_produto, id_categoria, valorTotal, quantidade):
        try:
            self.setConnection()
            insert_table_query = '''INSERT INTO tb_Compras (id_fornecedor, id_produto, id_categoria, 
            dataCompra, valorTotal, quantidade) VALUES (%s, %s, %s, NOW(), %s, %s)'''
            values = (id_fornecedor, id_produto, id_categoria, valorTotal, quantidade)
            self.__cur.execute(insert_table_query, values)
            self.__con.commit()
            count = self.__cur.rowcount
            print (count, "Record inserted successfully into table")
            self.killConnection()
            res = True
        except (Exception, psycopg2.Error) as error :
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

    def consultaCompras(self):
        self.setConnection()
        select_query = 'select * from tb_compras'
        self.__cur.execute(select_query)
        compras = self.__cur.fetchall() 
        self.killConnection()
        return compras
