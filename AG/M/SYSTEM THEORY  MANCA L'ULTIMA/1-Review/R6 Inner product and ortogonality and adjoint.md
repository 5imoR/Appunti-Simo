#ST-L10
### Definition
Dato uno spazio vettotriale $V$ in $\mathbb R$ un'*inner product* function è una funzione $<\cdot,\cdot>:V\times V\rightarrow\mathbb R$ 
Questo soddisfa 3 proprietà:
- Simmetria $\forall v_1,v_2\in V\quad <v_1,v_2>=<v_2,v_1>$ 
- Bilinearità $\forall v_1,v_2 \in V\quad \forall \alpha_1,\alpha_2\in \mathbb R <\alpha_1v_1+\alpha_2v_2,v>=\alpha_1<v_1,v>+\alpha_2<v_2,v>$
- Positive definiteves $\forall v\in V\quad <v,v>\ \geq 0\iff v=0$ 

### Definition
Dati due vettori sono detti ortogonali se $<v_1,v_2>=\underline 0$ 

### Definition
Sia $U$ un sottospazio vettoriale di $V$ allora:
$(U^\perp)^\perp\triangleq\set{v\in V_i:<v_1,u>=0\ \forall u\in U}$ 
#### Proprietà 
- $(U^\perp)^\perp\supseteq U$ 
- $U\cap U^\perp=\set{\underline 0}$ 
 se $V$ è un finite dimensional vector space allora:
- $(U^\perp)^\perp= U$ 
- $U\oplus U^\perp=\set{u+w:u\in U\ w\in U^\perp}$ 
	non c'è l'intersezione per definizione

### Definition Adjoint
Siano $V$ e $W$ due spazi vettoriali in $\mathbb R$ 
Assumiamo di avere 2 inner product,
- in $V\ <\cdot,\cdot>_V$
- in $W\ <\cdot,\cdot>_W$
Sia $\mathcal A:V\rightarrow W$ la trasformazione lineare che corrisponde alla mappa per passare da $V$ a $W$ per la quale vale:         $\mathcal A(\alpha_1v_1+\alpha_2v_2)=\alpha_1\mathcal A(v_1)+\alpha_2\mathcal A(v_2) \qquad\forall v_1,v_2\in V\quad \forall \alpha_1,\alpha_2 \in \mathbb R$ 


Una trasformazione lineare è detta *adjoint* della trasformazione lineare $\mathcal A$ se:
$$
<\mathcal A(v),w>_W=<v,\mathcal A^*(w)>_V\qquad \forall v\in V\quad\forall w\in W
$$
$\mathcal A^*$ non è detto che esista ma in caso è unica
$\mathcal A: V\rightarrow W$  $V,W$ spazi vettoriali reali

#### Caso 1 
Assumiamo:
- $V=\mathbb R^k$ 
- $W=\mathbb R^p$ 
- assumiamo l'inner product in $V$ e $W$ 
	$<w_1,w_2>\triangleq W_1^TW_2^T\qquad\forall w_1,w_2\in W$
	$<v_1,v_2>\triangleq V_1^TV_2^T\quad \qquad\forall v_1,v_2\in V$
Sia:
- $\mathcal A:V\rightarrow W$ una trasformazione lineare

Se assumiamo di avere una base in $V$ ed una in $W$ allora $\mathcal A(\cdot)$ è rappresentata dalla matrice $A\in\mathbb R^{p\times k}$ 

$$
\begin{align}
\mathcal A&:V\rightarrow W\\
&:v\rightarrow Av
\end{align}
$$
Noi vogliamo dimostrare che $\mathcal A^*$ è rappresentata da $A^T$
$$
\begin{align}
\mathcal A&:W\rightarrow V\\
&:w\rightarrow A^Tw
\end{align}
$$
##### Dimostrazione
- $\forall v\in V\quad\forall w\in W$ 
$$
\begin{align}
<Av,w>_W& =<v,\mathcal A^*(w)>_V\\
[Av]^Tw&=v^T[\mathcal A^*(w)]\\
v^T[A^Tw]&=v^T[\mathcal A^*(w)]
\end{align}
$$
#### Caso 2
$V=\mathcal U|_{[0,t]}$  è il set di piece wise continuous function definito in $[0,t]$ e prendendo i valori in $U=\mathbb R^n$ 
$w=X=\mathbb R^n$
Assumiamo l'inner product:
$$<u_1,u_2>_{\mathcal U|_{[0,t]}}\triangleq\int_0^tu_1^T(\tau)u_2(\tau)d\tau$$
$$<x_1,x_2>_X\triangleq x_1^Tx_2\qquad \forall x_1,x_2\in X$$



$$\begin{align}\mathcal A&:\mathcal U|_{[0,t]}\rightarrow X\\
&:u(\tau)\rightarrow\int_0^tM(\tau)u(\tau)d\tau\end{align}$$
$M(\tau$) è una matrix valued function $\in \mathbb R^{n\times m}$

Vogliamo identificare $\mathcal A^*:X\rightarrow\mathcal U|_{[0,t]}\qquad \forall u(\cdot)\in \mathcal U|_{[0,t]} \quad \forall x\in X$ 
$$
\begin{align}
<\mathcal A(u(\cdot)),x>_X&=<u(\cdot),\mathcal A^*(x)>_{\mathcal U|_{[0,t]}}&=\int_0^tu^T(\tau){\color {orange}[\mathcal A^*(x)]}(\tau)d\tau\\
‖\qquad\qquad&&\\
<\left[\int_0^tM(\tau)u(\tau)d\tau\right],x>_X&=\left[\int_0^tM(\tau)u(\tau)d\tau\right]^Tx&=\int_0^tu^T(\tau){\color {orange}[M^T(\tau)x]}(\tau)d\tau\\
\Rightarrow\mathcal A^*:x\in X\rightarrow M^T(\tau)x\ \tau\in[0,t]
\end{align}
$$

#### Proprietà adjoint
- $\ker\mathcal A\equiv(Im\mathcal A^*)^\perp$
- $\ker \mathcal A=\ker[\mathcal A^*A]=$
- $Im \mathcal A\subseteq(\ker \mathcal A^*)^\perp$ 
- $Im \mathcal A\supseteq Im(\mathcal A \mathcal A^*)$
Nelle ultime due se $Im \mathcal A$ è un  finite dimensional  vector space allora sono due uguaglianze