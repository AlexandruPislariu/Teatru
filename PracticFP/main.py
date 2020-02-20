'''
Created on 3 feb. 2020

@author: Alex
'''
#teste
from teste.testeRepo import TestRepo
from teste.testeValid import TestValid
from teste.testeService import TestService

#validare
from validari.validation import ValidPiesa
validPiesa = ValidPiesa()

#repository
from infrastructure.repository import RepositoryFile
from domain.entitati import Piesa
repoPiesa = RepositoryFile('./piese.txt',Piesa)

#service
from business.service import ServicePiesa
srvPiesa = ServicePiesa(repoPiesa,validPiesa)

#ui
from prezentare.console import Console
ui = Console(srvPiesa)
ui.run()