from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from base import Base, db_session

class Categorias(Base):

    __tablename__ = 'tb_categorias'
    
    id_categoria = Column("id_categoria", Integer, primary_key=True)
    titulocategoria = Column("titulocategoria", String)
    descricaocategoria = Column("descricaocategoria", String)
    fg_ativo = Column("fg_ativo", Integer)

    # FKs
    produtos = relationship("Produtos")

    def insertCategoria(self):
        
        session = db_session()
        session.add(self)
        session.commit()
        session.close()
        res = True
        
        return res
    
    def consultaCategorias(self):
        session = db_session()
        categorias = session.query(Categorias).filter(Categorias.titulocategoria.like("%"+ self.titulocategoria +"%"))
        session.close()
        return categorias

    def consultaCategoriasAll(self):
        session = db_session()
        categorias = session.query(Categorias).all()
        session.close()
        return categorias

    def updateCategoria(self):
        session = db_session()
        item = session.query(Categorias).filter(Categorias.id_categoria == self.id_categoria).update({
            Categorias.titulocategoria:self.titulocategoria,
            Categorias.descricaocategoria:self.descricaocategoria,
            Categorias.fg_ativo:self.fg_ativo,
        })
        session.commit()
        session.close()
        return True

    def deleteCategoria(self):
        session = db_session()
        item = session.query(Categorias).filter(Categorias.id_categoria == self.id_categoria)
        session.delete(item.one())
        session.commit()
        session.close()
        return True

class Produtos(Base):

    __tablename__ = 'tb_produtos'
    
    id_produto = Column("id_produto", Integer, primary_key=True)
    nomeproduto = Column("nomeproduto", String)
    descricaoproduto = Column("descricaoproduto", String)
    fg_ativo = Column("fg_ativo", Integer)
    id_categoria = Column("id_categoria", Integer, ForeignKey('tb_categorias.id_categoria'))
    valorunitario = Column("valorunitario", Numeric)
    quantidade = Column("quantidade", Integer)
    quantidademinima = Column("quantidademinima", Integer)

    # FKs
    #categoria = relationship("Categorias", back_populates="produtos")
    #fornecedor = relationship("Fornecedores", back_populates="produtos")
    
    def insertProduto(self):
        session = db_session()
        session.add(self)
        session.commit()
        session.close()
        res = True
        
        return res
    
    def consultaProdutos(self):
        session = db_session()
        produtos = session.query(Produtos).filter(Produtos.nomeproduto.like("%"+ self.nomeproduto +"%"))
        session.close()
        return produtos

    def consultaProdutosAll(self):
        session = db_session()
        produtos = session.query(Produtos).all()
        session.close()
        return produtos

    def updateProduto(self):
        session = db_session()
        item = session.query(Produtos).filter(Produtos.id_produto == self.id_produto).update({
            Produtos.titulocategoria:self.titulocategoria,
            Produtos.descricaocategoria:self.descricaocategoria,
            Produtos.fg_ativo:self.fg_ativo,
        })
        session.commit()
        session.close()
        return True

    def deleteProduto(self):
        session = db_session()
        item = session.query(Produtos).filter(Produtos.id_produto == self.id_produto)
        session.delete(item.one())
        session.commit()
        session.close()
        return True

class Fornecedores(Base):

    __tablename__ = 'tb_fornecedores'
    
    id_fornecedor = Column("id_categoria", Integer, primary_key=True)
    cnpj = Column("cnpj", String)
    razaosocial = Column("razaosocial", String)
    contato = Column("contato", String)
    telefone = Column("telefone", String)
    endereco = Column("endereco", String)
    
    # FKs
    #produtos = relationship("Produtos", back_populates="fornecedor")
    
    def insertFornecedor(self):
        session = db_session()
        session.add(self)
        session.commit()
        session.close()
        res = True
        
        return res
    
    def consultaFornecedores(self):
        session = db_session()
        fornecedores = session.query(Fornecedores).filter(Fornecedores.nomefornecedor.like("%"+ self.nomefornecedor +"%"))
        session.close()
        return fornecedores

    def consultaFornecedoresAll(self):
        #session = db_session()
        fornecedores = session.query(Fornecedores).all()
        session.close()
        return fornecedores

    def updateFornecedor(self):
        session = db_session()
        item = session.query(Fornecedores).filter(Fornecedores.id_fornecedor == self.id_fornecedor).update({
            Fornecedores.titulocategoria:self.titulocategoria,
            Fornecedores.descricaocategoria:self.descricaocategoria,
            Fornecedores.fg_ativo:self.fg_ativo,
        })
        session.commit()
        session.close()
        return True

    def deleteFornecedor(self):
        session = db_session()
        item = session.query(Fornecedores).filter(Fornecedores.id_fornecedor == self.id_fornecedor)
        session.delete(item.one())
        session.commit()
        session.close()
        return True
