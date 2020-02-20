from domain.entitati import Piesa,PiesaDTO
from Random import generate_random_string,generate_random_integer,generate_random_gen
class ServicePiesa(object):
    
    def __init__(self, repoPiesa, validPiesa):
        self.__repoPiesa = repoPiesa
        self.__validPiesa = validPiesa
        
    def adauga_piesa(self,titlu,regizor,gen,durata):
        
    #creez o piesa
        piesa = Piesa(titlu,regizor,gen,durata)
        
        if self.__validPiesa.validare_piesa(piesa): #validez
            self.__repoPiesa.adauga_entitate(piesa) #adaug in repository
            
    def modifica_piesa(self,titlu,regizor,gen,durata):
    
    #creez o piesa
        piesa = Piesa(titlu,regizor,gen,durata)
        
        if self.__validPiesa.validare_piesa(piesa): #validez
            self.__repoPiesa.modifica_entitate(piesa) #modific in repository
    

    def creeaza_piese(self,numar_piese):
        """
    Functia creeaza random piese de teatru
        """
        piese_adaugate = [] #retin piesele pe care le adauga
        for i in range (0,numar_piese,1):
        #creez random o piesa
            titlu = generate_random_string()
            regizor = generate_random_string()
            gen = generate_random_gen()
            durata = generate_random_integer(100,200)
            
            piesa = Piesa(titlu,regizor,gen,durata)
        #adaug in repository
            self.__repoPiesa.adauga_entitate(piesa)
            piese_adaugate.append(piesa)
            
        return piese_adaugate
    
    def exporta_piese(self,nume_fisier):
        """
    Functia exporta piesele de teatru intr-un fisier dat de utilizator sortate crescator dupa numele regizorului si titlu
        """
    
    #preiau piesele de teatru   
        piese = self.__repoPiesa.get_all()
    #le sortez crescator dupa regizor si titlu
        piese_sortate = sorted(piese,key = lambda x: (x.get_regizor(),x.get_titlu()))
        
    #Deschid fisierul
        fisier = open(nume_fisier,'w')
        
        for piesa in piese_sortate:
        #generez un an random
            an = generate_random_integer(1950, 2011)
            an = str(an)
            
        #scriu piesa in fisier sub forma (regizor,titlu,an,gen)
            piesa_export = PiesaDTO(piesa.get_regizor(),piesa.get_titlu(),an,piesa.get_gen())
            fisier.write(PiesaDTO.write_entity(piesa_export))
            fisier.write('\n')
            
        
        fisier.close()