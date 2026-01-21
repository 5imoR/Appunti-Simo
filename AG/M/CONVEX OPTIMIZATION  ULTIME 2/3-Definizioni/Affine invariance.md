#CO-L17-1

### Definizione
Se si fa un cambio di cordinate il metodo si comporta allo stesso modo. Assumiamo di avere $f(\cdot)$ ed un punto iniziale $x^{(0)}$ con il quale si raggiungono i punti $x^{(1)}\ x^{(2)}\dots$ Ora facciamo un cambio di coordinate tramite la matrice $A\in\mathbb R^{n\times m}$ quindi:
$y=Ax$ e così otteniamo una nuova funzione:
$g(y)=f(Ax)$ 
Quindi ora possiamo utilizzare lo stesso metodo partendo da $y^{(0)}$ andando ad ottenere $y^{(1)}\ y^{(2)}\dots$


### Note
Questa caratteristica ci dice che il nostro metodo non migliora o peggiora in base alle coordinate di partenza.

- Gradients methods non sono affine invariance dato che dipendono dal punto di partenza
- Newton method è affine invariant
