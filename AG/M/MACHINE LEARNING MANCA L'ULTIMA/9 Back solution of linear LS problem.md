#ML-L09-1 (LS dovrebbe essere least square)

- $\hat w =\arg\min\frac 1m||Y-Xw||^2$
- $X=USV^T=U_1S_1V_1^T$
- $\hat w =V_1S_1^{-1}U_1^TY$ è la soluzione minima
In un LS problem generico:
- $w=\arg\min ||b-Aw||^2$
- se $A$ è invertibile:
	$w^*=A^{-1}b$      s.t.     $Aw^*=AA^{-1}b=b$                $\Rightarrow b-Aw^*=0$ 
- se $A$ non è invertibile:
	e.g. $A\in \mathbb R^{n\times m}\qquad n>m$ 

![[Pseudo Inverse of the matrix A#Moore-Penrose pseudoinverse]]
