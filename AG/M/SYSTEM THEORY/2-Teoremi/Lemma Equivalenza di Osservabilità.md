#ST-L29-2
senza nome
### Lemma
Per ogni $\lambda \in \mathbb C$ :
	di conseguenza $\forall \lambda\in\mathbb C$ con:
	$|\lambda|\ge 1$ DT       $Re(\lambda)\ge 0$ CT
$$rank\begin{bmatrix} \lambda I_{n-p}-A_{11} \\ A_{21} \end{bmatrix}
=n-p\iff rank\begin{bmatrix} \lambda I-F \\ H \end{bmatrix}=n$$
Questo equivale a dire che:
- $(A_{11},A_{21})$ è observable $\iff(F,H)$ è observable
- Se nessuno dei due paii è observable allora devono condividere lo stesso autovalore dell'unobservable subsystem
### Proof
$$
rank\begin{bmatrix} \lambda I-F \\ H \end{bmatrix}=\begin{bmatrix} \lambda I-A \\ C \end{bmatrix}=rank\begin{bmatrix} \lambda I_{n-p}-A_{11} & -A_{12}\\ -A_{21} & \lambda I_p-A_{22} \\ 0 & I_p\end{bmatrix}
$$
Di conseguenza:
$$
\begin{align}
n=rank\begin{bmatrix} \lambda I-F \\ H \end{bmatrix} 
&\Rightarrow \text{ all n clumns are lineary indipendent }\\
&\Rightarrow \text{ all columns of $\begin{bmatrix} \lambda I_{n-p}-A_{11} & -A_{12}\\ -A_{21} & \lambda I_p-A_{22} \\ 0 & I_p\end{bmatrix} $ are linearly indipendent }\\
&\Rightarrow \text{ the $n-p$ columns of $\begin{bmatrix} \lambda I_{n-p}-A_{11} \\ -A_{21} \\ 0\end{bmatrix} $ are linearly indipendent}\\ 
&\Rightarrow \text{ the $n-p$ columns of $\begin{bmatrix} \lambda I_{n-p}-A_{11} \\ -A_{21}\end{bmatrix} $ are linearly indipendent}\\ 
&\Rightarrow rank\begin{bmatrix} \lambda I_{n-p}-A_{11} \\ -A_{21}\end{bmatrix}=n-p
\end{align}
$$
Allo stesso tempo:
$$
\begin{align}
n-p=rank\begin{bmatrix} \lambda I_{n-p}-A_{11} \\ -A_{21}\end{bmatrix}
&\Rightarrow \text{ the $n-p$ columns are lineary indipendent }\\
&\Rightarrow \text{ the $n-p$ columns of $\begin{bmatrix} \lambda I_{n-p}-A_{11} \\ -A_{21} \\ 0\end{bmatrix} $ are linearly indipendent }\\
&\Rightarrow \text{all columns of $\begin{bmatrix} \lambda I_{n-p}-A_{11} & -A_{12}\\ -A_{21} & \lambda I_p-A_{22} \\ 0 & I_p\end{bmatrix} $ are linearly indipendent }\\ 
&\Rightarrow rank\begin{bmatrix} \lambda I-F \\ H \end{bmatrix} =n
\end{align}
$$
### Conseguenze
- La possibilità di progettare un [[State Observer#Reduced order Observer|ROO]] asintotico è indipendente dalla scelta di $V$ e può essere controllato a priori sul paio $(F,H)$ originale
- $$\begin{gather}\exists L\  \ s.t. A_{11}+LA_{21} \text{ è asimptotically stable}\\\Updownarrow\\\exists\tilde L\ \ s.t.\ F+\tilde LH \text{is asymptotically stable}\\\Updownarrow\\\exists \text{ asymptotic full order closed loop observer FOCLO }\end{gather}$$
- Entrambi i punti precedenti possono essere estesi al [[DBO Dead Beat Observer (Full Order Closed Loop)|DBO]]


$$
x(t) \xrightarrow[T]{\qquad} \bar x(t)= 
\begin{bmatrix}
 W(t)\\
 y(t)\\
\end{bmatrix}
\xrightarrow[]{\qquad}v(t)\leftarrow\hat v(t)
$$

| Estimate                                                         | Estimation Error                                                                                                             | Estimation Error Dinamics                                                                                 |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| $\hat v(t)$                                                      | $e_v(t)\triangleq v(t)-\hat v(t)$                                                                                            | $\begin{align}&e_v(t+1)=(A_{11}+LA_{21})e_v(t)\\&e_v(t)\underset{t \to +\infty}{\to}0\qquad *\end{align}$ |
| $$\begin{align}&\hat w(t)=\\&\ \ \ \hat v(t)-Ly(t)\end{align}$$  | $\begin{align}e_w(t)\triangleq& W(t)-\hat W(t)=\\&[v(t)-\cancel{Ly(t)}] \\-&[\hat v(t)-\cancel{Ly(t)}]\\&=e_v(t)\end{align}$ | $e_w(t)\underset{t \to +\infty}{\to}0$                                                                    |
| $\hat{\bar x}(t)=\begin{bmatrix}\hat W(t)\\ y(t)\\\end{bmatrix}$ | $\begin{align}e_\bar x(t)\triangleq&\bar x(t)-\hat{\bar x}(t)\\&=\begin{bmatrix} e_w(t)\\ 0\\\end{bmatrix}\end{align}$       | $e_\bar x(t)\underset{t \to +\infty}{\to}0$                                                               |
| $\hat x(t)=T\hat{\bar x}(t)$                                     | $\begin{align}e(t)\triangleq&x(t)-\hat{x}(t)\\&=Te_\bar x(t)\end{align}$                                                     | $e(t)\underset{t \to +\infty}{\to}0$                                                                      |
$*$ Assumendo $(A_{11},A_{21})$, equivalentemente $(F,H)$, detectable

