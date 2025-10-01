[[ALGEBRA]]
### Spazio vettoriale

#### Campo 
Un campo k è un insieme non vuoto dotato di due operazioni $+$ e $\cdot$ che soddisfano le seguenti proprietà:
- P. Associativa
- P. Commutativa
- Esiste un elemento neutro per $+$ e $\cdot$  (0 e 1)
- Ogni elemento ha il suo opposto ( a+(-a) = 0)
- Ogni elemento ha il suo inverso $a \cdot a^{-1}=1$
- P. Distributiva  $(a+b)\cdot c = (a\cdot c)+(b\cdot c)$
###### Esempio
$k = {0,1}$

| +   | 0   | 1   |
| --- | --- | --- |
| 0   | 0   | 1   |
| 1   | 1   | 0   |

| $\cdot$ | 0   | 1   |
| ------- | --- | --- |
| 0       | 0   | 1   |
| 1       | 1   | 0   |

#### Definizione
Sia K un campo qualsiasi.
Uno spazio vettoriale è un insieme non vuoto V dotato di un operazione di somma e una di prodotto (tra uno scalare $\lambda$ e un vettore)

	$k^n = {(a_1,...,a_n) | a_i \in k}$
	$\lambda \in k$
	$v=(a_1,...,a_n)$
	$\lambda \cdot v = (\lambda a_1,...,\lambda a_n)$
	![[R123]]
	$a_1 v_1+...+a_rv_r \in V$
	I vettori $v_1,...,v_r$ sono linearmente indipendenti se l'unica soluzione è $a_1=...=a_r=0$
	I vettori $v_1,...,v_r$ sono linearmente dipendenti se $\exists a\neq0$  tali che $a_1 v_1+...+a_rv_r = 0$ 
- Nel caso di due vettori essere indipendenti equivale non essere paralleli
- Se un vettore è la combinazione lineare degli altri vettori comporta che i vettori sono dipendenti
#### Base
$S = \{v1,...,vn\}$ è un insieme di vettori di $V$ 
Il sottospazio vettoriale generato da $S$ è il più piccolo sottospazio di $V$ che contiene $S$ (scritto $L(S)$ o $<S>$)
Sono un sistema di generatori di V se $<S> = V$ ovvero se ogni vettore $v\in V$ si può scrivere come combinazione lineare dei vettori dati.
Una base di uno spazio vettoriale $V$ è un sistema di generatori V costituito da vettori linearmente indipendenti

Un vettore con base $v$ si scrive:
$$
\begin{bmatrix}
\lambda_1 \\
\lambda_2 \\
\vdots \\
\lambda_n
\end{bmatrix}^{\underline{v}}
$$

#### Dimensione
- La dimensione di un vettore è il numero di elementi  di una base $\mathbb{R}^n = \{v_0,...,v_n\}$
- Risolvendo un sistema di equazioni la dimensione equivale al nomero di parametri liberi di variare
##### Formula di Grassman
$$
\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)
$$
La somma di due sottospazi si dice diretta se $\dim(U \cap W) = \{\vec{0}\}$
