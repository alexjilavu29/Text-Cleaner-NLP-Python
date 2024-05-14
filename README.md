# NLP PROJECT
## Developing a text sanitization algorithm using natural language processing methods

---

### Description

This project aims to develop a lexical cleansing program using Natural Language Processing (NLP) techniques. The program detects and censors vulgar words in a given text while preserving the original context and the author's intent.

---

### Features

1. **Detection of vulgar words:** Using a predefined list of vulgar words.
2. **Partial word censorship:** Replacing part of the word with asterisks to preserve the general meaning of the text.
3. **Word similarity check:** Detecting words similar to vulgar ones by comparing letters.
4. **Dictionary consultation:** Using WordsAPI to verify if a word is real and its usage frequency.
5. **Handling special cases:** Managing rare words and attempts to bypass censorship.

---

### How to Run the Project

1. **Clone this repository:**
    ```bash
    git clone https://github.com/alexjilavu29/Text-Cleaner-NLP-Python
    cd repo
    ```

2. **Set environment variables:**
    - Create a `.env` file in the main directory of the project.
    - Add your WordsAPI key to the `.env` file:
      ```
      WORDSAPI_KEY=your_api_key
      ```

2. **Run the script:**
    ```bash
    python main.py
    ```

---

### Project Structure

- **main.py:** Contains the main logic of the program.
- **input.txt:** Input file containing the text to be processed.
- **output.txt:** Output file where the censored text will be saved.
- **.env:** File for environment variables (not included in the repository, must be created manually).
- 
---

### Important Functions

- **citeste_text_din_fisier(nume_fisier):** Reads text from a file.
- **proceseaza_text(text, cuvinte_vulgare, explicit):** Processes the text and censors vulgar words.
- **cenzureaza_cuvant(cuvant):** Partially censors a word.
- **verifica_cuvant(cuvant, api_key):** Checks if a word exists in the English dictionary using WordsAPI.
- **test_similitudine(cuvant):** Checks the similarity of a word to those in the vulgar words list.

---

### Usage Example

1. Insert the text into the `input.txt` file.
2. Run the `main.py` script.
3. Check the result in the `output.txt` file.

---

### Conclusion

This project demonstrates an efficient way to clean texts of vulgar language using NLP techniques while preserving the original context and format of the text. The program can be extended to include a larger variety of words and expressions, as well as to improve the similarity detection algorithm.

---


# Romanian Translation Below
--- 


# PROIECT NLP


## Realizarea unui algoritm de sanitizare a unui text folosind metode de procesare a limbajului natural

---

### Descriere

Acest proiect are ca scop dezvoltarea unui program de curățare lexicală folosind tehnici de Procesare a Limbajului Natural (NLP). Programul detectează și cenzurează cuvintele vulgare dintr-un text dat, păstrând contextul original și intenția autorului.

---

### Funcționalități

1. **Detectarea cuvintelor vulgare:** Utilizând o listă de cuvinte vulgare predefinite.
2. **Cenzurarea parțială a cuvintelor:** Înlocuirea unei părți din cuvânt cu asteriscuri pentru a păstra înțelesul general al textului.
3. **Verificarea similitudinii cuvintelor:** Detectarea cuvintelor similare cu cele vulgare prin compararea literelor.
4. **Consultarea unui dicționar:** Utilizarea WordsAPI pentru a verifica dacă un cuvânt este real și frecvența de utilizare a acestuia.
5. **Gestionarea cazurilor speciale:** Tratarea cuvintelor rare și a tentativelor de ocolire a cenzurii.

---

### Cum să rulezi proiectul

1. **Clonează acest repository:**
    ```bash
    git clone https://github.com/alexjilavu29/Text-Cleaner-NLP-Python
    cd repo
    ```

2. **Setează variabilele de mediu:**
    - Creează un fișier `.env` în directorul principal al proiectului.
    - Adaugă cheia API pentru WordsAPI în fișierul `.env`:
      ```
      WORDSAPI_KEY=cheia_ta_api
      ```

2. **Rulează scriptul:**
    ```bash
    python main.py
    ```

---

### Structura Proiectului

- **main.py:** Conține logica principală a programului.
- **input.txt:** Fișierul de intrare care conține textul ce urmează a fi procesat.
- **output.txt:** Fișierul de ieșire în care va fi salvat textul cenzurat.
- **.env:** Fișierul pentru variabile de mediu (nu este inclus în repository, trebuie creat manual).

---

### Funcții Importante

- **citeste_text_din_fisier(nume_fisier):** Citește textul dintr-un fișier.
- **proceseaza_text(text, cuvinte_vulgare, explicit):** Procesează textul și cenzurează cuvintele vulgare.
- **cenzureaza_cuvant(cuvant):** Cenzurează parțial un cuvânt.
- **verifica_cuvant(cuvant, api_key):** Verifică dacă un cuvânt există în dicționarul limbii engleze folosind WordsAPI.
- **test_similitudine(cuvant):** Verifică similitudinea unui cuvânt cu cele din lista de cuvinte vulgare.

---

### Exemplu de Utilizare

1. Introduceți textul în fișierul `input.txt`.
2. Rulați scriptul `main.py`.
3. Verificați rezultatul în fișierul `output.txt`.

---

### Concluzii

Acest proiect demonstrează un mod eficient de a curăța texte de limbaj vulgar folosind tehnici de NLP, păstrând contextul original și formatul textului. Programul poate fi extins pentru a include o varietate mai mare de cuvinte și expresii, precum și pentru a îmbunătăți algoritmul de detectare a similarităților.

---
