from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Numeric, Date
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
    compras = relationship("Compras")
    vendas = relationship("Vendas")
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
    id_fornecedor = Column("id_fornecedor", Integer, ForeignKey('tb_fornecedores.id_fornecedor'))

    # FKs
    compras = relationship("Compras")
    vendas = relationship("Vendas")
    
    def insertProduto(self):
        session = db_session()
        session.add(self)
        session.commit()
        session.close()
        res = True
        
        return res
    
    def consultaProdutos(self):
        session = db_session()
        produtos = session.query(Produtos, Categorias).outerjoin(Categorias, Produtos.id_categoria == Categorias.id_categoria).filter(Produtos.nomeproduto.like("%"+ self.nomeproduto +"%")).all()
        session.close()
        return produtos

    def consultaProdutosAll(self):
        session = db_session()
        produtos = session.query(Produtos, Categorias).outerjoin(Categorias, Produtos.id_categoria == Categorias.id_categoria).all()
        session.close()
        return produtos

    def updateProduto(self):
        session = db_session()
        item = session.query(Produtos).filter(Produtos.id_produto == self.id_produto).update({
            Produtos.id_categoria:self.id_categoria,
            Produtos.descricaoproduto:self.descricaoproduto,
            Produtos.fg_ativo:self.fg_ativo,
            Produtos.id_fornecedor:self.id_fornecedor,
            Produtos.nomeproduto:self.nomeproduto,
            Produtos.quantidade:self.quantidade,
            Produtos.quantidademinima:self.quantidademinima,
            Produtos.valorunitario:self.valorunitario,
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
    
    id_fornecedor = Column("id_fornecedor", Integer, primary_key=True)
    cnpj = Column("cnpj", String)
    razaosocial = Column("razaosocial", String)
    contato = Column("contato", String)
    telefone = Column("telefone", String)
    endereco = Column("endereco", String)
    fg_ativo = Column("fg_ativo", Integer)
    
    # FKs
    compras = relationship("Compras")
    produtos = relationship("Produtos")
    
    def insertFornecedor(self):
        session = db_session()
        session.add(self)
        session.commit()
        session.close()
        res = True
        
        return res
    
    def consultaFornecedores(self):
        session = db_session()
        fornecedores = session.query(Fornecedores).filter(Fornecedores.razaosocial.like("%"+ self.razaosocial +"%"))
        session.close()
        return fornecedores

    def consultaFornecedoresAll(self):
        session = db_session()
        fornecedores = session.query(Fornecedores).all()
        session.close()
        return fornecedores

    def updateFornecedor(self):
        session = db_session()
        item = session.query(Fornecedores).filter(Fornecedores.id_fornecedor == self.id_fornecedor).update({
            Fornecedores.razaosocial:self.razaosocial,
            Fornecedores.contato:self.contato,
            Fornecedores.endereco:self.endereco,
            Fornecedores.cnpj:self.cnpj,
            Fornecedores.telefone:self.telefone,
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

class Compras(Base):

    __tablename__ = 'tb_compras'
    
    id_compra = Column("id_compra", Integer, primary_key=True)
    id_categoria = Column("id_categoria", Integer, ForeignKey('tb_categorias.id_categoria'))
    id_produto = Column("id_produto", Integer, ForeignKey('tb_produtos.id_produto'))
    id_fornecedor = Column("id_fornecedor", Integer, ForeignKey('tb_fornecedores.id_fornecedor'))
    datacompra = Column("datacompra", Date)
    valortotal = Column("valortotal", Numeric)
    quantidade = Column("quantidade", Integer)
    fg_ativo = Column("fg_ativo", Integer)

    def insertCompra(self):
        
        session = db_session()
        session.add(self)
        session.commit()
        session.close()
        res = True
        
        return res
    
    def consultaCompras(self):
        session = db_session()
        compras = session.query(Compras, Produtos, Fornecedores, Categorias).outerjoin(Produtos, Compras.id_produto == Produtos.id_produto).outerjoin(Fornecedores, Compras.id_fornecedor == Fornecedores.id_fornecedor).outerjoin(Categorias, Compras.id_categoria == Categorias.id_categoria).filter(Compras.id_produto == self.id_produto).all()
        session.close()
        return compras

    def consultaComprasAll(self):
        session = db_session()
        compras = session.query(Compras, Produtos, Fornecedores, Categorias).outerjoin(Produtos, Compras.id_produto == Produtos.id_produto).outerjoin(Fornecedores, Compras.id_fornecedor == Fornecedores.id_fornecedor).outerjoin(Categorias, Compras.id_categoria == Categorias.id_categoria).all()
        session.close()
        return compras

    def updateCompra(self):
        session = db_session()
        item = session.query(Compras).filter(Compras.id_compra == self.id_compra).update({
            Compras.id_categoria:self.id_categoria,
            Compras.id_fornecedor:self.id_fornecedor,
            Compras.id_produto:self.id_produto,
            Compras.fg_ativo:self.fg_ativo,
        })
        session.commit()
        session.close()
        return True

    def deleteCompra(self):
        session = db_session()
        item = session.query(Compras).filter(Compras.id_compra == self.id_compra)
        session.delete(item.one())
        session.commit()
        session.close()
        return True

class Vendas(Base):

    __tablename__ = 'tb_vendas'
    
    id_venda = Column("id_venda", Integer, primary_key=True)
    id_categoria = Column("id_categoria", Integer, ForeignKey('tb_categorias.id_categoria'))
    id_produto = Column("id_produto", Integer, ForeignKey('tb_produtos.id_produto'))
    id_vendedor = Column("id_vendedor", Integer, ForeignKey('tb_vendedores.id_vendedor'))
    datavenda = Column("datavenda", Date)
    valortotal = Column("valortotal", Numeric)
    quantidade = Column("quantidade", Integer)
    fg_ativo = Column("fg_ativo", Integer)

    def insertVenda(self):
        
        session = db_session()
        session.add(self)
        session.commit()
        session.close()
        res = True
        
        return res
    
    def consultaVendas(self):
        session = db_session()
        vendas = session.query(Vendas, Produtos, Vendedores, Categorias).outerjoin(Produtos, Vendas.id_produto == Produtos.id_produto).outerjoin(Vendedores, Vendas.id_vendedor == Vendedores.id_vendedor).outerjoin(Categorias, Vendas.id_categoria == Categorias.id_categoria).filter(Vendas.id_produto == self.id_produto).all()
        session.close()
        return vendas

    def consultaVendasAll(self):
        session = db_session()
        vendas = session.query(Vendas, Produtos, Vendedores, Categorias).outerjoin(Produtos, Vendas.id_produto == Produtos.id_produto).outerjoin(Vendedores, Vendas.id_vendedor == Vendedores.id_vendedor).outerjoin(Categorias, Vendas.id_categoria == Categorias.id_categoria).all()
        session.close()
        return vendas

    def updateVenda(self):
        session = db_session()
        item = session.query(Vendas).filter(Vendas.id_venda == self.id_venda).update({
            Vendas.id_categoria:self.id_categoria,
            Vendas.id_vendedor:self.id_vendedor,
            Vendas.id_produto:self.id_produto,
            Vendas.fg_ativo:self.fg_ativo,
        })
        session.commit()
        session.close()
        return True

    def deleteVenda(self):
        session = db_session()
        item = session.query(Vendas).filter(Vendas.id_venda == self.id_venda)
        session.delete(item.one())
        session.commit()
        session.close()
        return True

class Vendedores(Base):

    __tablename__ = 'tb_vendedores'
    
    id_vendedor = Column("id_vendedor", Integer, primary_key=True)
    cpf = Column("cpf", String)
    nome = Column("nome", String)
    carteiratrabalho = Column("carteiratrabalho", String)
    telefone = Column("telefone", String)
    dataadmissao = Column("dataadmissao", String)
    fg_ativo = Column("fg_ativo", Integer)
    
    # FKs
    vendas = relationship("Vendas")
    
    def insertVendedor(self):
        session = db_session()
        session.add(self)
        session.commit()
        session.close()
        res = True
        
        return res
    
    def consultaVendedores(self):
        session = db_session()
        vendedores = session.query(Vendedores).filter(Vendedores.nome.like("%"+ self.nome +"%"))
        session.close()
        return vendedores

    def consultaVendedoresAll(self):
        session = db_session()
        vendedores = session.query(Vendedores).all()
        session.close()
        return vendedores

    def updateVendedor(self):
        session = db_session()
        item = session.query(Vendedores).filter(Vendedores.id_vendedor == self.id_vendedor).update({
            Vendedores.nome:self.nome,
            Vendedores.carteiratrabalho:self.carteiratrabalho,
            Vendedores.dataadmissao:self.dataadmissao,
            Vendedores.cpf:self.cpf,
            Vendedores.telefone:self.telefone,
            Vendedores.fg_ativo:self.fg_ativo,
        })
        session.commit()
        session.close()
        return True

    def deleteVendedor(self):
        session = db_session()
        item = session.query(Vendedores).filter(Vendedores.id_vendedor == self.id_vendedor)
        session.delete(item.one())
        session.commit()
        session.close()
        return True