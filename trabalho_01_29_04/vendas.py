import psycopg2
from psycopg2 import Error


class Vendas:

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

    # Inicio metodos CRUD
    def insertVenda(self, id_vendedor, id_produto, id_categoria, valorTotal, quantidade):
        try:
            self.setConnection()
            insert_table_query = '''INSERT INTO tb_vendas (id_vendedor, id_produto, id_categoria, 
            dataVenda, valorTotal, quantidade) VALUES (%s, %s, %s, NOW(), %s, %s)'''
            values = (id_vendedor, id_produto, id_categoria, valorTotal, quantidade)
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

    def deleteVenda(self, id_venda):
        self.setConnection()
        self.__cur.execute(
            "delete from tb_vendas where id_venda = " + str(id_venda))
        print("Record deleted successfully from the table")
        self.__con.commit()
        self.killConnection()

    def updateVenda(self, dataVenda, valorTotal, quantidade, id_venda):
        self.setConnection()
        self.__cur.execute("update tb_vendas set dataVenda = %s, valorTotal = %s,  quantidade = NOW() where id_venda = " +
                           str(id_venda), (dataVenda, valorTotal, quantidade))
        print("Record updated successfully from the table")
        self.__con.commit()
        self.killConnection()

    def consultaVendas(self):
        self.setConnection()
        self.__cur.execute("select * from tb_vendas")
        rows = self.__cur.fetchall()        
        self.killConnection()
        return rows

        # Fim metodos CRUD

    # Criacao da tabela tb_vendas
    def createTable(self):
        try:
            self.setConnection()
            create_table_query = '''CREATE TABLE tb_vendas 
                (id_venda SERIAL PRIMARY KEY, 
                id_produto INT references tb_produtos(id_produto) NOT NULL,
                id_vendedor INT references tb_vendedores(id_vendedor) NOT NULL, 
                id_categoria INT references tb_categorias(id_categoria) NOT NULL, 
                dataVenda timestamp,
                valorTotal NUMERIC,
                quantidade INT,
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
