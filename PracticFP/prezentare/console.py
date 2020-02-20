from exceptii.erori import ValidError,RepoError
class Console(object):
    
    
    def __init__(self, srvPiesa):
        self.__srvPiesa = srvPiesa
        
        self.__comenzi = {
        "add":self.__ui_adauga_piesa,
        "modify":self.__ui_modifica_piesa,
        "creator":self.__ui_creeaza_piese,
        "export":self.__ui_exporta}
        
    def __panou_comenzi(self):
        """
    Funtia tipareste functionalitatile diponibile
        """
        print("Comenzile disponibile ale aplicatiei sunt \n")
        print("add: pentru adaugarea unei piese de teatru \n")
        print("modify: pentru modificarea unei piese de teatru \n")
        print("creator: pentru a creea random piese de teatru \n")
        print("export: pentru a exporta piesele de teatru in alt fisier \n")
        print("exit: inchiderea aplicatiei \n")
        print("Separarea dintre comanda si parametrii se face cu ;")
        
    def __ui_adauga_piesa(self,parametrii):
        """
    Functia comunica cu utilizatorul pentru a adauga o piesa de teatru
        """
        if len(parametrii)!=4 : #titlu,regizor,gen,durata
            raise ValueError("Numar incorect de date introduse!")
        
        titlu = parametrii[0]
        regizor = parametrii[1]
        gen = parametrii[2]
        durata = parametrii[3]
        
        self.__srvPiesa.adauga_piesa(titlu,regizor,gen,durata)
        
    def __ui_modifica_piesa(self,parametrii):
        """
    Functia comunica cu utilizatorul pentru a modifica o piesa de teatru
        """
        if len(parametrii)!=4: #titlu,regizor,gen,durata
            raise ValueError("Numar incorect de date introduse!")
        
        titlu = parametrii[0]
        regizor = parametrii[1]
        gen = parametrii[2]
        durata = parametrii[3]
        
        self.__srvPiesa.modifica_piesa(titlu,regizor,gen,durata)
        
    def __ui_creeaza_piese(self,parametrii):
        """
    Functia comunica cu utilizatorul pentru a creea noi piese de teatru
        """
        if len(parametrii)!=1:
            raise ValueError("Numar incorect de date introduse!")
        
        numar_piese = int(parametrii[0])
        rezultat = self.__srvPiesa.creeaza_piese(numar_piese)
        
        for element in rezultat:
            print(element)
            
    def __ui_exporta(self,parametrii):
        """
    Functia comunica cu utilizatorul pentru a exporta piesele in alt fisier
        """
        if len(parametrii)!=1: #nume_fisier
            raise ValueError("Numar incorect de date introduse!")
        
        nume_fisier = parametrii[0]
        self.__srvPiesa.exporta_piese(nume_fisier)
        
    def run(self):
        """
    Functie principala de rulare a interfetei cu utilizatorul
        """
        self.__panou_comenzi()
        while True:
            comanda = input("Introduceti comanda dorita! ")
            
            if comanda is None:
                print("Comanda invalida!")
                
            if comanda == 'exit':
                print("Aplicatia a fost inchisa cu succes!")
                break
                
        #despart comanda
            comanda = comanda.split(';') #separator = ;
            nume_comanda = comanda[0]
            parametrii = comanda[1:]
            
            if nume_comanda in self.__comenzi.keys(): #verific daca exista comanda
            #execut si tratez eventualele erori
                try:
                    self.__comenzi[nume_comanda](parametrii)
                except ValueError as ve:
                    print("UI error: \n"  + str(ve))
                except ValidError as valide:
                    print("Valid error: \n" + str(valide))
                except RepoError as re:
                    print("Repo error: \n" + str(re))
                    
            else:
                print("Comanda invalida! ")
    



