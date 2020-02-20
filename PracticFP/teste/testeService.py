import unittest
from business.service import ServicePiesa
from infrastructure.repository import RepositoryFile
from validari.validation import ValidPiesa
from domain.entitati import Piesa, PiesaDTO

class TestService(unittest.TestCase):
#In aceasta clasa testez serviceul aplicatiei

    def setUp(self):
        
        self.valid = ValidPiesa()
        self.repo = RepositoryFile('./fisier_test.txt',Piesa)
        self.service = ServicePiesa(self.repo,self.valid)
        
    #adaug entitati in repository
        self.piesa1 = Piesa('papa','mirel','Comedie',100)
        self.piesa2 = Piesa('asda','razvan','Drama',100)
        self.piesa3 = Piesa('pascolopol','alex','Comedie',120)
        self.piesa4 = Piesa('papa','doina','Satira',130)
        self.piesa5 = Piesa('papagal','alex','Comedie',100)
        self.piesa6 = Piesa('papa','alex','Altele',111)
        
        self.repo.adauga_entitate(self.piesa1)
        self.repo.adauga_entitate(self.piesa2)
        self.repo.adauga_entitate(self.piesa3)
        self.repo.adauga_entitate(self.piesa4)
        self.repo.adauga_entitate(self.piesa5)
        self.repo.adauga_entitate(self.piesa6)
        
    def tearDown(self):
    #Golesc fisierul de test
        fisier = open('./fisier_test.txt','w')
        fisier.seek(0)
        fisier.truncate()
        fisier.close()
        
        
    def test_creeaza_piese(self):
        
        lungime_initiala = len(self.repo.get_all())
        numar_piese_adaugate = 3
        self.service.creeaza_piese(numar_piese_adaugate)
        self.assertEqual(lungime_initiala + numar_piese_adaugate, len(self.repo.get_all()))
        
    def test_exporta_piese(self):
    #export piesele
        self.service.exporta_piese('fisier_export.txt')
        
    #preiau piesele exportate din fisier
        fisier2 = open('fisier_export.txt','r')
        content = fisier2.read()
        content = content.split('\n')
        
        piese_exportate = []
        for line in content:
            if line.strip()=='':
                continue
            piesa_exportata = PiesaDTO.read_entity(line)
            piese_exportate.append(piesa_exportata)
            
        fisier2.close()
        
    #verific daca piesele conincid
        for piesa in piese_exportate:
            self.assertNotEqual(self.repo.cauta_entitate(piesa), -1)
            
    #verific sortarea
        self.assertEqual(piese_exportate[0].get_titlu(), self.piesa6.get_titlu())
        self.assertEqual(piese_exportate[0].get_regizor(), self.piesa6.get_regizor())
        self.assertEqual(piese_exportate[1].get_titlu(), self.piesa5.get_titlu())
        self.assertEqual(piese_exportate[1].get_regizor(), self.piesa5.get_regizor())
        self.assertEqual(piese_exportate[2].get_titlu(), self.piesa3.get_titlu())
        self.assertEqual(piese_exportate[2].get_regizor(), self.piesa3.get_regizor())

if __name__=='__main__':
    unittest.main()