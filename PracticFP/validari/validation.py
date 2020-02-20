from exceptii.erori import ValidError

class ValidPiesa(object):
#In acesta clasa validez o piesa de teatru

    def validare_piesa(self,piesa):
        """
    Functia returneaza true daca piesa este valida
        """
        erori = "" #afisez toate erorile
        
    #validare titlu
        titlu = piesa.get_titlu()
        if titlu is None:
            erori = erori + "Titlu invalid \n"
            
    #validare regizor
        regizor = piesa.get_regizor()
        if regizor is None:
            erori = erori + "Regizor invalid \n"
            
    #validare durata
        durata = piesa.get_durata()
        try:
            durata = int(durata)
            
            if durata<0:
                erori = erori + "Durata invalida \n"
                
            piesa.set_durata(durata)
                
        except ValueError:
            erori = erori + "Durata invalida \n"
            
    #validare gen
        gen = piesa.get_gen()
        if gen!="Comedie" and gen!="Drama" and gen!="Satira" and gen!="altele":
            erori = erori + "Gen invalid \n"
            
        if erori=="":
            return True
        else:
            raise ValidError(erori)


