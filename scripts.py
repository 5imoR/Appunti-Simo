print("Inserisci la matrice (una riga per volta, separa gli elementi con spazi).")
print("Usa un punto (.) per lasciare una casella vuota.")
print("Scrivi 'riga' come ultima riga per avere il codice in una sola riga.")
print("Premi Invio su una riga vuota per terminare (se è la prima riga creerà una matrice simbolica):")

matrice = []
modo_riga = False  # flag per capire se l'ultima riga è 'riga'

# prima riga
prima = input()

# --- NUOVA FUNZIONALITÀ ---
if prima == "":
    print("Prima riga vuota: creo una matrice simbolica.")

    dims = input("Inserisci numero di righe e colonne (es. '3 4'): ").split()
    if len(dims) != 2:
        raise ValueError("Devi inserire esattamente due numeri: righe e colonne.")

    m, n = map(int, dims)

    # indici finali in un'unica riga
    indici = input("Inserisci gli indici finali per colonna e riga (es. 'n q'): ").split()
    if len(indici) != 2:
        raise ValueError("Devi inserire esattamente due simboli: indice colonna e indice riga.")

    indice_col, indice_riga = indici

    # crea matrice simbolica base
    matrice = [[f"k_{{{i+1}{j+1}}}" for j in range(n)] for i in range(m)]

    # --- penultima colonna = \dots ---
    if n >= 2:
        for i in range(m):
            matrice[i][n-2] = r"\dots"

    # --- penultima riga = \vdots ---
    if m >= 2:
        for j in range(n):
            matrice[m-2][j] = r"\vdots"

    # --- cella in comune = \ddots ---
    if m >= 2 and n >= 2:
        matrice[m-2][n-2] = r"\ddots"

    # --- ultima colonna: k_{i indice_col}, tranne la penultima riga ---
    for i in range(m-1):
        matrice[i][n-1] = f"k_{{{i+1}{indice_col}}}"

    # correzione richiesta: penultima riga, ultima colonna = \vdots
    matrice[m-2][n-1] = r"\vdots"

    # --- ultima riga: k_{indice_riga j} ---
    for j in range(n-1):
        matrice[m-1][j] = f"k_{{{indice_riga}{j+1}}}"

    # penultima colonna dell'ultima riga = \dots
    matrice[m-1][n-2] = r"\dots"

    # ultima cella = k_{indice_riga indice_col}
    matrice[m-1][n-1] = f"k_{{{indice_riga}{indice_col}}}"

else:
    # prima riga normale
    if prima.strip().lower() == "riga":
        modo_riga = True
    else:
        elementi = ["" if x == "." else x for x in prima.split()]
        matrice.append(elementi)

    # leggere righe successive
    if not modo_riga:
        while True:
            riga = input()
            if riga == "":
                break
            if riga.strip().lower() == "riga":
                modo_riga = True
                break
            elementi = ["" if x == "." else x for x in riga.split()]
            matrice.append(elementi)

# genera LaTeX
if modo_riga:
    latex = "\\begin{bmatrix} "
    latex += " \\\\ ".join(" & ".join(r) for r in matrice)
    latex += " \\end{bmatrix}"
else:
    latex = "\\begin{bmatrix}\n"
    for r in matrice:
        latex += " & ".join(r) + " \\\\\n"
    latex += "\\end{bmatrix}"

print("\nEcco la tua matrice in formato MathJax/LaTeX:")
print(latex)
