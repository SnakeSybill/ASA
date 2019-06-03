import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Categorias(Base):

    __tablename__ = 'tb_categorias'
    engine = create_engine('postgresql://postgres:hambotregga@localhost:5432/teste_asa', echo = True)
    
    id_categoria = Column("id_categoria", Integer, primary_key=True)
    titulocategoria = Column("titulocategoria", String)
    descricaocategoria = Column("descricaocategoria", String)
    fg_ativo = Column("fg_ativo", Integer)

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    
    def insertCategoria(self):
        
        session = self.Session()
        session.add(self)
        session.commit()
        session.close()
        res = True
        
        return res
    
    def consultaCategorias(self):
        session = self.Session()
        categorias = session.query(Categorias).filter(Categorias.titulocategoria.like("%"+ self.titulocategoria +"%"))
        session.close()
        return categorias

    def consultaCategoriasAll(self):
        session = self.Session()
        categorias = session.query(Categorias).all()
        session.close()
        return categorias

    def updateCategoria(self):
        session = self.Session()
        item = session.query(Categorias).filter(Categorias.id_categoria == self.id_categoria).update({
            Categorias.titulocategoria:self.titulocategoria,
            Categorias.descricaocategoria:self.descricaocategoria,
            Categorias.fg_ativo:self.fg_ativo,
        })
        session.commit()
        session.close()
        return True

    def deleteCategoria(self):
        session = self.Session()
        item = session.query(Categorias).filter(Categorias.id_categoria == self.id_categoria)
        session.delete(item.one())
        session.commit()
        session.close()
        return True
