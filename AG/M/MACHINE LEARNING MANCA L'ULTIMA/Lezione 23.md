#ML-L23 [[Lezione 22]]
# Support Vector Machine SVM
\[Binary classification]
Al momento siamo in grado di separare tramite una retta i nostri campioni.
L'SVM ci permette di scegliere quella migliore, infatti ci permette di  scegliere quella che massimizza la distanza minima dei campioni dalla retta
Ne esistono 2 versioni:
- Hard SVM: Funziona solo con dati linearmente separabili
- Soft SVM: Funziona anche con dati non linearmente separabili
Idea:
$$
\max_{w, b} (\min(dist(x_i,line(w,b)\ )))
$$

![[SVG intro]]

## Hard SVM
$$
(\hat w, \hat b)= \arg \max_{\substack{w\in\mathbb R^d\\b\in \mathbb R}}\big(\min (d_i) \big)\qquad y_i\in \set{-1,1} 
$$
$$ 
d_i=y_i\frac{w^Tx_i+b}{||w||}
$$
#### Step 1
$$(\hat w, \hat b)= \arg \max_{\substack{w, b}}\left(\min \left(y_i\frac{w^Tx_i+b}{||w||}\right) \right)$$
#### Step 2
$$(\hat w, \hat b)= \arg \max_{\substack{w, b, \gamma}}\gamma\qquad s.t.\qquad
y_i\frac{w^Tx_i+b}{||w||}\ge \gamma$$
Se si massimizza un lowerbound è come massimizzare anche il minimo di quel valore
#### Step 3
$$(\hat w, \hat b)= \arg \max_{\substack{w, b, \gamma\\||w||=1}}\gamma\qquad s.t.\qquad
y_i\frac{w^Tx_i+b}{\gamma}\ge \frac \gamma\gamma=1$$
#### Step 4
$$(\hat w, \hat b)= \arg \max_{\substack{w, b, \gamma\\||w||=1}}\gamma\qquad s.t.\qquad
y_i\frac{w^T}{\gamma}x_i+\frac b{\gamma}\ge 1$$
$$
\bar w=\frac w\gamma\qquad \bar b=\frac b\gamma\qquad \qquad ||\bar w||=\frac 1\gamma
$$
#### Step 5
$$(\hat w, \hat b)= \arg \max_{\substack{\bar w,\bar b}}\frac 1{||\bar w||}\qquad s.t.\qquad
y_i\bar w^Tx_i+\bar b\ge 1$$
#### Step 6
$$(\hat w, \hat b)= \arg \min_{\substack{w, b}}||w||^2\qquad s.t.\qquad
y_i w^Tx_i+ b\ge 1$$
Questo  è convesso con dei vincoli lineari  [[LP.pdf]]

![[SVG Hard]]
Quello che si va a massiomizzare è la distanza tra le due righe tratteggiate. La soluzione è supportata da un piccolo subset di dati che corrispondono al Support Vector

### Lagrange Duality
[[AG/M/CONVEX OPTIMIZATION  ULTIME 2/Zdomande|Zdomande]] 
$$
y_i(w^T x_i+b)\ge 1\ \to\ (1-y_i(w^Tx_i+b)\le 0)
$$
 $$
 \begin{align}
 &L(w,b,\mu)=\frac 12 ||w||^2+\sum^m_{i=1}\mu_i(1-y_i(w^Tx_i+b))\Rightarrow g(\mu)=\inf L(w,b,\mu)\qquad \mu\in\mathbb R^n\ \ \  \mu\ge0\\
 &\inf L(w,b,\mu)=\begin{cases}
 \displaystyle-\infty \qquad \qquad if\ \ \ \ \sum^m_{i=1}\mu_iy_i\ne0\\
  \displaystyle\sum_{i=1}^m \mu_i-\frac 12\sum^m_{i,j=1} \mu_i\mu_j\ y_iy_j\ x_i^Tx_j
 \end{cases}\\
 \end{align}
 $$
### Trovare i valori di $\hat w$ e $\hat b$
$$\hat w=\sum^m_{i=1}\mu_iy_ix_i$$
 $\hat w$ dipende dalla soluzione dei moltiplicatori di $\hat mu=\arg\max_{\large\substack{\mu\in\mathbb R^n\\\mu\ge 0\\\exists \sum \mu_iy_i=0}} g(\mu)$ 
 ![[svm qualcosa]]
 Ci interessano solo i valori positivi
 $$
 L(w,b,\mu)=\frac 12||w||^2+\sum^m_{i=1}\mu_if_i(w,b)
 $$
 - $f_i(w,b)<0\Rightarrow \mu_i=0$
 - $f_i(w,b)=0\Rightarrow \mu_i>0$ 
E' al massimo quando o $f_i(w,b)$ o $\mu_i$ è pari a $0$

$\hat w=\sum_{i\in I}\hat \mu_iy_ix_i\qquad I=\set{i\in [m]s.t.\ \ (1-y_i(\hat w^Tx_i+\hat b))=0}$ 

I Datapoint nel set $I$ sono chiamati support vector


$\displaystyle \hat w=\sum_{i\in I}\hat \mu_iy_ix_i$ 
$\displaystyle h_{\hat w\hat b}(x)= \hat w^Tx+\hat b=\sum^m_{i=1}\hat \mu_iy_i{\color{lightgreen}x_i^Tx}+\hat b$   La soluzione dipende solo da datapoint e testpoint
$\displaystyle\hat\mu_i=\arg\max_{\substack{\mu_i\ge 0\\\exists \sum \mu_iy_i=0}}\sum_{i=1}^m \mu_i-\frac 12\sum^m_{i,j=1} \mu_i\mu_j\ y_iy_j\ {\color{lightgreen}x_i^Tx_j}$  

### Passaggio da Hard a Soft SVM
Si effettua una [[Integral Programming#Relaxation|relaxation]] 
$\displaystyle\hat w\  \hat b = \min_{\large w,\ b,\color{#B794FF} \xi_i\ge 0}\frac 12 ||w||^2{\color{#B794FF}+\lambda\sum^m_{i=1}\xi_i}$   
s.t.    $y_i(w^Tx_i+b)\ge 1\color{#B794FF}-\xi_i$ 
La relaxation serve per i valori che non vengono identificati correttamente e finiscono oltre la riga tratteggiata.
- $\xi_i=0$ se $y_i(w^Tx_i+b)\ge 1$                       è classificato correttamente
- $0<\xi_i<1$ se $1>y_i(w^Tx_i+b)>0$         è classificato correttamente ma dentro i tratteggi
- $\xi_i>1$ se $y_i(w^Tx_i+b)< 0$                       è classificato erratamente dentro o fuori i tratteggi
![[soft svm]]