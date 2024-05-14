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
