from abc import ABCMeta, abstractclassmethod

class AgenciaNoticia:

    def __init__(self):
        self.__inscritos = []
        self.__ultima_noticia = None

    def inscrever(self,inscrito):
        self.__inscritos.append(inscrito)
    
    def desinscrever(self,inscrito=None):
        if not inscrito:
            return self.__inscritos.pop()
        else:
            return self.__inscritos.remove(inscrito)
        
    def noticiar_todos(self):
        for insc in self.__inscritos:
            insc.notificar()
    
    def adicionar_noticia(self, noticia):
        self.__ultima_noticia = noticia
    
    def mostrar_noticia(self):
        return f'Urgente: {self.__ultima_noticia}'
    

    def inscritos(self):
        
    
        return  [type(valor).__name__  for valor in self.__inscritos] 

        
    



class TipoInscricao(metaclass=ABCMeta):

    @abstractclassmethod
    def notificar(self):
        pass



class InscSMS(TipoInscricao):

    def __init__(self,agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    
    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')


class InscWPP(TipoInscricao):

    def __init__(self,agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    
    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')


if __name__ == '__main__':
    agencia_noticia = AgenciaNoticia()

    InscSMS(agencia_noticia)

    InscWPP(agencia_noticia)

    #print(AgenciaNoticia.__dict__)

    print(f'inscritos: {agencia_noticia.inscritos()}')

    agencia_noticia.adicionar_noticia('teste noticia')

    agencia_noticia.noticiar_todos()

    print(f'descadastrado {type(agencia_noticia.desinscrever()).__name__}')

    print(f'inscritos: {agencia_noticia.inscritos()}')

