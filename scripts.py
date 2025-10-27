print("Inserisci la matrice (una riga per volta, separa gli elementi con spazi). Premi Invio su una riga vuota per terminare:")

matrice = []
while True:
    riga = input()
    if riga == "":
        break
    # separa i valori della riga (es: "1 2 3" -> ["1","2","3"])
    matrice.append(riga.split())

latex = "\\begin{bmatrix}\n"

for r in matrice:
    latex += " & ".join(r) + " \\\\\n"  # unisci elementi con & e termina la riga con \\
latex += "\\end{bmatrix}"

print("\nEcco la tua matrice in formato MathJax/LaTeX:")
print(latex)
