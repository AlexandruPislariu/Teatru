import unittest
from infrastructure.repository import RepositoryFile
from exceptii.erori import RepoError
from domain.entitati import Piesa
from _ast import With


class TestRepo(unittest.TestCase):
#In acesta clasa testez repository

    def setUp(self):
    #Adaug entitati in repository
        self.repo = RepositoryFile('./fisier_test.txt',Piesa)
        
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
    #Golesc continutul fisierului de test dupa fiecare test
        fisier = open('./fisier_test.txt','w')
        fisier.seek(0)
        fisier.truncate()
        fisier.close()
        
        
    def test_get_all(self):
        
        self.assertEqual(self.repo.get_all(), [self.piesa1,self.piesa2,self.piesa3,self.piesa4,self.piesa5,self.piesa6])
        
    def test_get_entitate(self):
        
        self.assertEqual(self.repo.get_entitate(0), self.piesa1)
        self.assertEqual(self.repo.get_entitate(1), self.piesa2)
        self.assertEqual(self.repo.get_entitate(5), self.piesa6)
        self.assertEqual(self.repo.get_entitate(3), self.piesa4)
        
    def test_cauta_entitate(self):
        
        self.assertEqual(self.repo.cauta_entitate(self.piesa1), 0)
        self.assertEqual(self.repo.cauta_entitate(self.piesa2), 1)
        self.assertEqual(self.repo.cauta_entitate(self.piesa6), 5)
        self.assertEqual(self.repo.cauta_entitate(self.piesa3), 2)
        
    def test_adauga_entitate(self):
        
        piesa7 = Piesa('dada','razvan','Comedie',100)
        self.repo.adauga_entitate(piesa7)
        self.assertEqual(self.repo.get_all(), [self.piesa1,self.piesa2,self.piesa3,self.piesa4,self.piesa5,self.piesa6,piesa7])
       
        piesa8 = Piesa('papa','alex','Comedie',130)
        with self.assertRaises(RepoError):
            self.repo.adauga_entitate(piesa8)
            
    def test_modifica_entiate(self):
        
        piesa8 = Piesa('papa','alex','Comedie',130)
        self.repo.modifica_entitate(piesa8)
        self.assertEqual(self.piesa6.get_gen(), piesa8.get_gen())
        self.assertEqual(self.piesa6.get_durata(), piesa8.get_durata()) 
        
        piesa9  = Piesa('papa','doina','Drama',200)
        self.repo.modifica_entitate(piesa9)
        self.assertEqual(self.piesa4.get_gen(), piesa9.get_gen())
        self.assertEqual(self.piesa4.get_durata(), piesa9.get_durata())
        
if __name__=='__main__':
    unittest.main()


