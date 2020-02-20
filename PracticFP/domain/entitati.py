class Piesa():
#Abstractizez o piesa de teatru
    
    def __init__(self,titlu,regizor,gen,durata):
        self.__titlu = titlu
        self.__regizor = regizor
        self.__gen = gen
        self.__durata = durata

    def get_titlu(self):
        return self.__titlu


    def get_regizor(self):
        return self.__regizor


    def get_gen(self):
        return self.__gen


    def get_durata(self):
        return self.__durata


    def set_titlu(self, value):
        self.__titlu = value


    def set_regizor(self, value):
        self.__regizor = value


    def set_gen(self, value):
        self.__gen = value


    def set_durata(self, value):
        self.__durata = value

    def __str__(self):
        """
    Functia transforma entitatea in string pentru a putea fi tiparita
        """
        return str(self.get_titlu() + ' ' + self.get_regizor() + ' ' + self.get_gen() + ' ' + str(self.get_durata()))
    
    @classmethod
    def read_entity(cls,line):
        """
    Functia transforma o linie dintr-un fisier intr-o piesa de teatru
        """
        line = line.split(';')
        titlu = line[0]
        regizor = line[1]
        gen = line[2]
        durata = line[3]
        
        return Piesa(titlu,regizor,gen,durata)
    
    @classmethod
    def write_entity(cls,piesa):
        """
    Functia transforma o piesa intr-un string pentru a putea fi scrisa in fisier
        """
        return str(piesa.get_titlu() + ';' + piesa.get_regizor() + ';' + piesa.get_gen() + ';' + str(piesa.get_durata()))
    

class PiesaDTO(object):
#clasa derivata a unei piese de teatru  
    
    def __init__(self, _regizor, _titlu, an, _gen):
        self.__regizor = _regizor
        self.__titlu = _titlu
        self.__an = an
        self.__gen = _gen

    def get_regizor(self):
        return self.__regizor


    def get_titlu(self):
        return self.__titlu


    def get_an(self):
        return self.__an


    def get_gen(self):
        return self.__gen


    def set_regizor(self, value):
        self.__regizor = value


    def set_titlu(self, value):
        self.__titlu = value


    def set_an(self, value):
        self.__an = value


    def set_gen(self, value):
        self.__gen = value

    
    @classmethod
    def read_entity(cls,line):
        """
    Functia transforma o linie dintr-un fisier intr-o piesa de teatru
        """
        line = line.split(';')
        regizor = line[0]
        titlu = line[1]
        an = line[2]
        gen = line[3]
        
        return PiesaDTO(regizor,titlu,an,gen)
    
    @classmethod
    def write_entity(cls,piesa):
        """
    Functia transforma o piesa intr-un string pentru a putea fi scrisa in fisier
        """
        return str(str(piesa.get_regizor()) + ';' + str(piesa.get_titlu()) + ';' + str(piesa.get_an()) + ';' + str(piesa.get_gen()))
    

    def __str__(self):
        """
    Functia transforma entitatea in string pentru a putea fi tiparita
        """
        return str(str(self.get_regizor()) + ' ' + str(self.get_titlu()) + ' ' + str(self.get_an()) + ' ' + str(str(self.get_gen())))

