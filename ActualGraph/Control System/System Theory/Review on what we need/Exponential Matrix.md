[[SYSTEM THEORY]]
Data una matrice $F\in \mathbb C^{n\times n}$  definiamo l'esponente di $F$ nella seguente maniera:
$$
e^{Ft}=\exp(Ft)\triangleq\sum_{k=0}^{+\infty} F^k\frac{t^k}{k!}
$$
## Proprietà
- $\displaystyle e^{Ft} | _{t=0}=In+Ft+F^2\frac{t^2}{2!}+\dots|_{t=0}\equiv In$    
- $\displaystyle\frac{d}{dt}[e^{Ft}]=F+F^2t+F^3\frac{t^2}{2!}+\dots = Fe^{Ft}=e^{Ft}F$ 
- $\displaystyle e^{Ft}$ è una matrice invertibile $\displaystyle\forall t\in \mathbb R$ e $[e^{Ft}]^{-1}=e^{-Ft}=e^{(-F)t}=e^{F(-t)}$ 
- se $v\neq0$ è un autovettore di $F$ corrispondente a l'autovalore $\lambda\in\mathbb C$ allora: $Fv=\lambda v$ allora $\forall t\in \mathbb R \quad e^{Ft}v=e^{\lambda t}v$ 

### Exponential Matrix in Jordan form

![[Jordan Form#Jordan Form]]

dato che $J$ e $J_i$ sono matrici diagonali a blocchi allora $J^k$ e $J_i^k$ sono diagonali a blocchi $\forall k\geq 0$ 
Guardando alla definizione di esponeziale si deduce che:
$$
e^{Jt}=\begin{bmatrix}[e^{J_1t}]&0&\cdots& 0\\0&[e^{J_2t}]&\cdots& 0\\\vdots&\vdots&\ddots&\vdots&\\0&0&\cdots&[e^{J_rt}]\end{bmatrix}
\qquad
e^{J_it}=\begin{bmatrix}[e^{J_{i1}t}]&0&\cdots& 0\\0&[e^{J_{i2}t}]&\cdots& 0\\\vdots&\vdots&\ddots&\vdots&\\0&0&\cdots&[e^{J_{is_i}t}]\end{bmatrix}
$$
Di conseguenza l'espressione $e^{Jt}$ è nota una volta conoscito l'esponenziale di un mini-block generico

$$
J_\lambda=\begin{bmatrix}\lambda_i&1&\cdots& 0\\0&\lambda_i&\ddots& 0\\\vdots&\vdots&\ddots&1&\\0&0&0&\lambda_i\end{bmatrix}
\longrightarrow\large e^{J_\lambda}=
\begin{bmatrix}
e^{\lambda t}&te^{\lambda t}&\frac{t^2}{2!}e^{\lambda t}&\cdots& \frac{t^{\nu-1}}{(\nu-1)!}e^{\lambda t}\\
0&e^{\lambda t}&te^{\lambda t}&\ddots& \vdots\\
0&0&e^{\lambda t}&\ddots&\frac{t^2}{2!}e^{\lambda t}&\\
0&0&0&\ddots&te^{\lambda t}\\
0&0&0&0&e^{\lambda t}
\end{bmatrix}
$$
Gli elementi della prima riga equivalgono alle *elementary modes* distinte associate al miniblocco

Usando gli stessi argomenti usati per la potenza di una matrice $J_i$ possiamo affermare che ogni $\lambda_i$  è associato ad $n{_i1}$ elementary modes distinte
Allora andando a considerare tutti gli autovalori abbiamo $n_{11}+n_{21}+\dots$ elem. modes distinte


Siccome qualunque matrice $F$ è simile ad una matrice in Jordan form $J$ :
$$
\begin{align}
&\exists T\in \mathbb C^{n\times n}\text{ non singular s.t. }\\ 
&T^{-1}FT=J \qquad F=TJT^{-1}\ e\ F^k=TJ^kT^{-1}\\
&\Rightarrow e^{ft}=\sum_{k=0}^{+\infty} F^k\frac{t^k}{k!}=\ \ \ 
\sum_{k=0}^{+\infty} TJ^kT^{-1}\frac{t^k}{k!}=\ \ \ 
T\left[\sum_{k=0}^{+\infty} J^k\frac{t^k}{k!}\right]T^{-1}=Te^{Jt}T^{-1}
\end{align}
$$
#### Esempio 1
$$
J=
\begin{bmatrix}
	1\\
	 &2\\
	 & &1&1\\
	 & & &1\\ 
	 & & & &0\\
	 & & & & &2&1\\
	 & & & & & &2&1\\
	 & & & & & & &2\\
	 & & & & & & & &0&1\\
	 & & & & & & & & &0 
\end{bmatrix}
$$


| $i$ | $\lambda_i$ | n_i | $s_i$ | elementary modes                                            |
| --- | ----------- | --- | ----- | ----------------------------------------------------------- |
| 1   | 0           | 3   | 2     | $1\ /\ t$                                                   |
| 2   | 1           | 3   | 2     | $e^t\ /\ te^t$                                              |
| 3   | 2           | 4   | 2     | $\displaystyle e^{2t}\ /\ te^{2t}\ /\ \frac{t^2}{2!}e^{2t}$ |
