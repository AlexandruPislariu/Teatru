import unittest
from validari.validation import ValidPiesa
from exceptii.erori import ValidError
from domain.entitati import Piesa

class TestValid(unittest.TestCase):
#In aceasta clasa testez validarea unei piese de teatru

    def setUp(self):
    #Creez entitati
        self.valid = ValidPiesa()
        
        self.piesa1 = Piesa('','alex','Comedie',100)
        self.piesa2 = Piesa('asda','','Comedie',100)
        self.piesa3 = Piesa('pascolopol','alex','Comedie',-1)
        self.piesa4 = Piesa('papa','alex','cc',100)
        self.piesa5 = Piesa('papagal','alex','Comedie',100)
        self.piesa6 = Piesa('','alex','Comedie',-1)
        
    def tearDown(self):
        pass
    
    def test_validare_piesa(self):
        
        with self.assertRaises(ValidError):
            self.valid.validare_piesa(self.piesa1)
            self.valid.validare_piesa(self.piesa2)
            self.valid.validare_piesa(self.piesa3)
            self.valid.validare_piesa(self.piesa4)
            self.valid.validare_piesa(self.piesa6)
            
        self.assertEqual(self.valid.validare_piesa(self.piesa5),True)
        
if __name__=='__main__':
    unittest.main()


