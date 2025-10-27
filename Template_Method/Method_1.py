from abc import ABCMeta , abstractmethod


class Compiler(metaclass=ABCMeta):

    @abstractmethod
    def coletar_fonte(self):
        pass

    @abstractmethod
    def compiler_object(self):
        pass

    @abstractmethod
    def executar(self):
        pass


    def compiler_executar(self):
        self.coletar_fonte()
        self.compiler_object()
        self.executar()
    



class IosCompiler(Compiler):

    def coletar_fonte(self):
        print('compiler swift')

    def compiler_object(self):
        print('compilando para bytecode')

    def executar(self):
        print('executando')


class AndroidCompiler(Compiler):

    def coletar_fonte(self):
        print('compiler kotlin')

    def compiler_object(self):
        print('compilando para bytecode')

    def executar(self):
        print('executando')


ios = IosCompiler()
ios.compiler_executar()
print("=-="*30)
android = AndroidCompiler()
android.compiler_executar()