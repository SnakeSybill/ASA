class User:
    __id = None
    __nome = None    
    __idade = None
    __cidade = None

    def __init__(self, id, nome, idade, cidade):
        self.__id = id
        self.__nome = nome        
        self.__idade = idade
        self.__cidade = cidade

    def getUserId(self):
        return self.__id

    def getUserNome(self):
        return self.__nome

    def getUserIdade(self):
        return self.__idade

    def getUserCidade(self):
        return self.__cidade

    def getUserName(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self.__nome
        else:
            retorno = "usuario nao encontrado!!"
        return (retorno)