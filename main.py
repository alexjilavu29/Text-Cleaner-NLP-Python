# PROIECT NLP
# Realizarea unui algoritm de sanitizare a unui text folosind metode de procesare a limbajului natural
# Autor: Jilavu Alexandru
# Anul: 3, Grupa: 2

def citeste_text_din_fisier(nume_fisier):
    # Aceasta functie va deschide fisierul si va citi continutul acestuia.
    with open(nume_fisier, 'r', encoding='utf-8') as fisier:
        continut = fisier.read()
    return continut

cuvinte_vulgare = ['shit', 'fuck', 'fucking', 'bitch', 'dick']  # Completează lista cu cuvintele vulgare reale.

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
def proceseaza_text(text, cuvinte_vulgare):
    # Separăm textul în cuvinte și procesăm fiecare cuvânt.
    cuvinte = text.split()
    cuvinte_procesate = []

    for cuvant in cuvinte:
        cuvant_original = cuvant.lower().strip('.,!?-"')  # Normalizăm cuvantul pentru comparație.

        if cuvant_original in cuvinte_vulgare:
            cuvant = cenzureaza_cuvant(cuvant)  # Aplicăm cenzura dacă cuvantul este vulgar.
        cuvinte_procesate.append(cuvant)

    return ' '.join(cuvinte_procesate)  # Reunim cuvintele înapoi într-un text.

if __name__ == '__main__':
    text_de_intrare = citeste_text_din_fisier('input.txt')
    text_sanitizat = proceseaza_text(text_de_intrare, cuvinte_vulgare)
    print(text_sanitizat)
    with open('output.txt', 'w', encoding='utf-8') as fisier:
        fisier.write(text_sanitizat)