# PROIECT NLP
# Realizarea unui algoritm de sanitizare a unui text folosind metode de procesare a limbajului natural
# Autor: Jilavu Alexandru
# Anul: 3, Grupa: 2

import os
from dotenv import load_dotenv

# Încărcarea variabilelor de mediu din fișierul .env
load_dotenv()

# Accesarea cheii API din variabilele de mediu
api_key = os.getenv('WORDSAPI_KEY')

# Funcție pentru citirea textului dintr-un fișier
def citeste_text_din_fisier(nume_fisier):
    with open(nume_fisier, 'r', encoding='utf-8') as fisier:
        continut = fisier.readlines()
    return continut

# Lista cuvintelor vulgare
cuvinte_vulgare = ['shit', 'fuck', 'fucking', 'bitch', 'dick', 'kys', 'cum']

# Funcție pentru procesarea textului
def proceseaza_text(text, cuvinte_vulgare,explicit):

    cuvinte = text.split()
    cuvinte_procesate = []
    explicit_count = 0

    for cuvant in cuvinte:
        cuvant_original = cuvant.lower().strip('''"', ;.!?-''')
        print(cuvant + " | " + cuvant_original)
        if cuvant_original in cuvinte_vulgare:
            cuvant = cenzureaza_cuvant(cuvant)
            explicit_count += 1

        else:
            # Verificarea similitudinii cuvintelor
            similar = test_similitudine(cuvant_original)
            if similar:
                # Dacă cuvântul este similar cu unul din lista cuvintelor vulgare, se va verifica dacă aparține limbii engleze.
                verificare = verifica_cuvant(cuvant_original, api_key)

                # Dacă cuvântul nu există în dicționarul limbii engleze sau este rar întâlnit, se va cenzura.
                if verificare == False or verificare == "rar":
                    cuvant = cenzureaza_cuvant(cuvant_original)
                    explicit_count += 1

        cuvinte_procesate.append(cuvant)

    if explicit_count>=3:
        print("\n\nTextul contine " + str(explicit_count) + " cuvinte vulgare.")
        explicit = 1

    text_procesat = ' '.join(cuvinte_procesate)
    text_procesat += '\n'
    return ( text_procesat,explicit)  


# Funcție pentru cenzurarea cuvântului în funcție de lungime
def cenzureaza_cuvant(cuvant):

    print("\n" + cuvant)

    cuvant_ajustat = cuvant.strip('''"', ;.!?-''')
    lungime = len(cuvant_ajustat)

    # Se va adăuga o cenzură pentru primele 4 litere, și încă una pentru fiecare 3 litere adiționale.
    numar_cenzuri = 1
    if lungime>4:
        numar_cenzuri += (lungime-4)//3

    litere_cuvant_cenzurat = list(cuvant_ajustat)

    # De la a doua literă încolo, se vor insera cenzurile.
    for i in range(numar_cenzuri):
        litere_cuvant_cenzurat[i+1] = '*'

    cuvant_cenzurat = ''.join(litere_cuvant_cenzurat)

    # Se va modifica secvența inițială, pentru a păstra delimitatori, semne de punctuație și alte simboluri.
    cuvant = cuvant.replace(cuvant_ajustat,cuvant_cenzurat)

    print( " { " + cuvant_ajustat + " | "+ cuvant_cenzurat + " | " + str(lungime) +  " | " + cuvant + " }")
    return cuvant


# Funcție de verificare a cuvântului în dicționarul limbii engleze
def verifica_cuvant(cuvant, api_key):
    import http.client
    import json

    # Conectare la API-ul WordsAPI
    conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

    # Construirea URL-ului pentru request
    url = f"/words/{cuvant}/frequency"

    # Realizarea request-ului
    conn.request("GET", url, headers=headers)

    # Primirea răspunsul
    res = conn.getresponse()
    data = res.read()

    # Decodificarea răspunsului
    data_decoded = data.decode("utf-8")
    response = json.loads(data_decoded)
    print(response)

    # Verificarea existenței cuvântului în dicționar
    if 'word' in response:
        print(f"Cuvântul '{cuvant}' există în dicționarul limbii engleze.")

        # Verificarea frecvenței de apariție a cuvântului
        if 'frequency' in response:
            if response['frequency']['perMillion'] < 1:
                print(f"Cuvântul '{cuvant}' este rar întâlnit.")
                return "rar"

        return True

    else:
        print(f"Cuvântul '{cuvant}' nu există în dicționarul limbii engleze.")
        return False

# Funcție pentru testarea similitudinii cuvintelor
def test_similitudine(cuvant):

    count_litere_similare = 0
    litere_cuvant = list(cuvant)

    # Parsarea cuvintelor vulgare
    for cuvant_vulgar in cuvinte_vulgare:

        litere_cuvant_vulgar = list(cuvant_vulgar)
        if len(litere_cuvant) == len(litere_cuvant_vulgar):
            for i in range(len(litere_cuvant)):
                if litere_cuvant[i] == litere_cuvant_vulgar[i]:
                    count_litere_similare += 1

        if count_litere_similare + 1 == len(litere_cuvant_vulgar):
            return (1, cuvant_vulgar)

        count_litere_similare = 0

    return False


if __name__ == '__main__':
    text_de_intrare = citeste_text_din_fisier('input.txt')
    text_sanitizat = []
    explicit = 0

    for linie in text_de_intrare:
        linie_procesata = proceseaza_text(linie, cuvinte_vulgare, explicit)
        text_sanitizat.append(linie_procesata[0])
        if linie_procesata[1]==1:
            explicit = 1

    if explicit==1:
        print("\n\nTextul a fost marcat ca fiind vulgar. Apar mai mult de 3 cuvinte vulgare.")

    with open('output.txt', 'w', encoding='utf-8') as fisier:
        fisier.writelines(text_sanitizat)