print("Inserisci la matrice (una riga per volta, separa gli elementi con spazi).")
print("Usa un punto (.) per lasciare una casella vuota.")
print("Scrivi 'riga' come ultima riga per avere il codice in una sola riga.")
print("Premi Invio su una riga vuota per terminare:")

matrice = []
modo_riga = False  # flag per capire se l'ultima riga è 'riga'

while True:
    riga = input()
    if riga == "":
        break
    if riga.strip().lower() == "riga":
        modo_riga = True
        break
    # separa i valori e sostituisce '.' con vuoto
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
