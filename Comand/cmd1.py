

class Instaler:

    def __init__(self,fonte,destino):
        self.opcoes = []
        self.destino = destino
        self.fonte = fonte

    def preferencias(self,escolha):
        quest = input((f'deseja continuar instalar {escolha} ')).strip().lower()

        if quest == 'sim':
            self.opcoes.append(escolha)
        else:
            pass

        

    def executar(self):
        for opcoes in self.opcoes:         
            print(f'Copiando os binarios de {self.fonte}/{opcoes} para {self.destino}')
           
        print('operação finalizada')
    

if __name__ == '__main__':
    soft = Instaler('python','user/desktop')

    soft.preferencias('python')
    soft.preferencias('java')

    soft.executar()