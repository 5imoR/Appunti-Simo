#ST-L28-2
### Definition 
Un full order observer $\Sigma_{CL}$ è un DBO per il DT ssm $\Sigma$ se 
$$\forall x(0),\hat x(0)\in X=\mathbb R^n\qquad e(t)=0\text{ in un numero finito di step}$$
equivalentemente:
$$
\exists N\in \mathbb Z+>0\ s.t.\ e(t)=0\quad \forall t\ge N
$$
###
Dato che $e(t)=(F+LH)^te(0)$ allora $\Sigma_{CL}$ è un DBO $\iff F+LH$ è [[Nilpotent matrix|nilpotent]] 
$\exists L\in \mathbb R^{n\times p}$ s.t. $F+LH$ sia nilpotent
$\phantom{ssssssssssss}\Updownarrow$
$\exists K\in \mathbb R^{p\times n}$ s.t. $F^T+H^TK$ è nilpotent
$\phantom{ssssssssssss}\Updownarrow$
$(F^T,H^T)$ ammette un [[DBC Dead Beat Controller]]

### Proposition \[caracterization of the existence of a DBO]
Dato un paio $(F,G)$ con $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$   che rappresenta un DT system ciò che segue è equivalente:
- $(F,H)$ ammette [[DBO Dead Beat Observer (Full Order Closed Loop)|DBO]] ($\exists L\in\mathbb R^{n\times p}$ s.t. $F+LH$ sia [[Nilpotent matrix|nilpotent]].)
- $(F,H)$ è [[Observability & Reconstructability DT|reconstructable]] 
- che $(F,H)$ sia [[Observability & Reconstructability DT|observable]] o meno la matrice $F_{22}$ è nilpotent
- se il rango di [[PHB Reachability Test]] $\begin{bmatrix} \lambda In-F \\H \end{bmatrix}=n$  allora $\forall\lambda\in\mathbb C\ \lambda\ne 0$ 
### Remark
Ereditiamo da DBC l'analisi del minimo nilpotency index che $F+LH$ può avere se una qualunque delle equivalenze precedenti tiene. Possiamo  riferirci ai due casi del terzo punto  andando a rimpiazzare il reachability index con l'observability index=$\min\set{K:rank\begin{bmatrix} H \\ \vdots \\ HF^{k-1} \end{bmatrix}=n}$ 
