# PROIECT NLP
# Realizarea unui algoritm de sanitizare a unui text folosind metode de procesare a limbajului natural
# Autor: Jilavu Alexandru
# Anul: 3, Grupa: 2

import os
from dotenv import load_dotenv
import requests

# Încarcă variabilele de mediu din fișierul .env
load_dotenv()

# Accesează cheia API din variabilele de mediu
api_key = os.getenv('WORDSAPI_KEY')


def citeste_text_din_fisier(nume_fisier):
    # Aceasta functie va deschide fisierul si va citi continutul acestuia.
    with open(nume_fisier, 'r', encoding='utf-8') as fisier:
        continut = fisier.read()
    return continut

cuvinte_vulgare = ['shit', 'fuck', 'fucking', 'bitch', 'dick']  # Completează lista cu cuvintele vulgare reale.
explicit = 0

def cenzureaza_cuvant(cuvant):
    # Cenzuram cuvântul în funcție de lungimea acestuia.

    print("\n" + cuvant)

    cuvant_ajustat = cuvant.strip('", ;.!?-')

    lungime = len(cuvant_ajustat)

    numar_cenzuri = 1
    if lungime>4:
        numar_cenzuri += (lungime-4)//3  # Calculam numărul de litere ce trebuie cenzurate.

    litere_cuvant_cenzurat = list(cuvant_ajustat)  # Transformam cuvantul într-o listă de caractere pentru a putea modifica literele.

    for i in range(numar_cenzuri):
        litere_cuvant_cenzurat[i+1] = '*'  # Cenzuram litera respectivă.

    cuvant_cenzurat = ''.join(litere_cuvant_cenzurat)  # Convertim lista înapoi într-un string.

    cuvant = cuvant.replace(cuvant_ajustat,cuvant_cenzurat)

    print( " { " + cuvant_ajustat + " | "+ cuvant_cenzurat + " | " + str(lungime) +  " | " + cuvant + " }")

    return cuvant


def verifica_cuvant(cuvant, api_key):
    import http.client
    import json

    # Conectează-te la endpoint-ul WordsAPI
    conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

    # Pregătește header-urile pentru request
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

    # Formatează URL-ul pentru a include cuvântul căutat
    url = f"/words/{cuvant}"

    # Trimite requestul GET
    conn.request("GET", url, headers=headers)

    # Primește răspunsul
    res = conn.getresponse()
    data = res.read()

    # Decodifică și interpretează răspunsul
    data_decoded = data.decode("utf-8")
    response = json.loads(data_decoded)

    # Verifică dacă cuvântul există în răspuns
    if 'word' in response:
        print(f"Cuvântul '{cuvant}' există în dicționarul englez.")
    else:
        print(f"Cuvântul '{cuvant}' nu există în dicționarul englez.")


def proceseaza_text(text, cuvinte_vulgare):
    # Separăm textul în cuvinte și procesăm fiecare cuvânt.
    cuvinte = text.split()
    cuvinte_procesate = []
    explicit_count = 0

    for cuvant in cuvinte:
        cuvant_original = cuvant.lower().strip('.,!?-"')  # Normalizăm cuvantul pentru comparație.
        verifica_cuvant(cuvant_original, api_key)
        if cuvant_original in cuvinte_vulgare:
            cuvant = cenzureaza_cuvant(cuvant)  # Aplicăm cenzura dacă cuvantul este vulgar.
            explicit_count += 1
        cuvinte_procesate.append(cuvant)

    if explicit_count>=3:
        print("\n\nTextul contine " + str(explicit_count) + " cuvinte vulgare.")
        explicit = 1
    return ' '.join(cuvinte_procesate)  # Reunim cuvintele înapoi într-un text.

if __name__ == '__main__':
    text_de_intrare = citeste_text_din_fisier('input.txt')
    text_sanitizat = proceseaza_text(text_de_intrare, cuvinte_vulgare)
    if explicit == 1:
        print("\n\nTextul a fost marcat ca fiind vulgar. Apar mai mult de 3 cuvinte vulgare.")
    print(text_sanitizat)
    with open('output.txt', 'w', encoding='utf-8') as fisier:
        fisier.write(text_sanitizat)