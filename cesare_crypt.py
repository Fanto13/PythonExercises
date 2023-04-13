
def cesare_coder(testo, shift):
    alfabeto = list("abcdefghijklmnopqrstuvwxyz")
    coded_text = ""
    for char in testo:
        if char.isalpha():
            char_index = alfabeto.index(char.lower())#alfabeto.index restituisce l'indice del carattere inserito e char.lower() trasforma il carattere in minuscolo
            char_code = alfabeto[(char_index + shift) % 26]#il modulo 26 serve per evitare che il carattere inserito sia maggiore di 26
            if char.isupper():#se invece il carattere inserito è maiuscolo
                coded_text += char_code.upper()#char_code.upper() trasforma il carattere in maiuscolo
            else:
                coded_text += char_code
        else:
            coded_text += char
    return coded_text

while True:
    testo_input = input("Inserisci il testo da codificare: ")
    shift_input = input("Inserisci lo spostamento di codifica: ")
    if not shift_input.isnumeric():
        print("Errore: lo spostamento deve essere un numero intero.")
        continue
    shift_input = int(shift_input)
    testo_codificato = cesare_coder(testo_input, shift_input)
    print("Il testo codificato è:", testo_codificato)

    testo_input2 = input("Inserisci il testo da decodificare: ")
    shift_input2 = input("Inserisci lo spostamento di decodifica: ")
    if not shift_input2.isnumeric():
        print("Errore: lo spostamento deve essere un numero intero.")
        continue
    shift_input2 = int(shift_input2)
    testo_decodificato = cesare_coder(testo_input2, -shift_input2)
    print("Il testo decodificato è:", testo_decodificato)
    break