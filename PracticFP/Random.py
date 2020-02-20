import random
import string
def generate_random_integer(a,b):
    """
Returneaza un numar intreg intre a si b
    """
    return random.randint(a,b)


def generate_random_gen():
    """
Genereaza un gen valid random
    """
    genuri = ['Comedie','Drama','Satira','Altele']
    return "".join(random.choice(genuri))


def generate_random_string():
    """
Genereaza un string cu un spatiu la mijloc
    """
    letters = string.ascii_lowercase
    vocale = 'aeiou'
    lungime = generate_random_integer(8,12)
    
    string_creat = ''
    for i in range(0,lungime//4):
    #aleg consoana
        consoana = random.choice(letters)
        while consoana in vocale:
            consoana = random.choice(letters)
    
    #aleg vocala
        vocala = random.choice(vocale)   
        string_creat = string_creat + consoana + vocala
   
    string_creat = string_creat + ' '
    
    for i in range(0,lungime//4):
    #aleg consoana
        consoana = random.choice(letters)
        while consoana in vocale:
            consoana = random.choice(letters)
    
    #aleg vocala
        vocala = random.choice(vocale)   
        string_creat = string_creat + consoana + vocala
    
    return string_creat


