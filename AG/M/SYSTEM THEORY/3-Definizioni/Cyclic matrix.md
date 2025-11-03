A partire dal caso di $m=1$ in [[PHB Reachability Test#Corollary]]
## Definition Cyclic matrix
#ST-L15 
Una matrice $F\in \mathbb R^{n\times n}$ è detta cyclic se $\exists v\in \mathbb R^n\ v\neq 0$ s.t.
la famiglia dei vettori $\underline v, F\underline v,F^2\underline v\dots F^{n-1}\underline v$  sia linearmente indipendente
### Proposition
Data $F\in \mathbb R^{n\times n}$ ciò che segue è equivalente:
- $F$ è cyclic
- $\exists g\in \mathbb R^n$ s.t. $(F,G)$ è reachable
- Per ogni autovalore di $F$ c'è un singolo miniblocco di Jordan
- Ogni autovalore di $F$ ha una molteplicità geometrica unitaria
- $\Psi_F(z)\equiv\Delta _F(z)$ 