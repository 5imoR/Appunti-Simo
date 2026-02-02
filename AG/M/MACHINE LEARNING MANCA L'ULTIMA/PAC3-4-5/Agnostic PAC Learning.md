[[PAC Learning]] #ML-L05-1
![[LDh_graph|600]]

Sono entrambe strettamente positive
Quando il modello $H$ "non è abbastanza ricco"...(?) 
$$
\begin{align}
&h^*\in argmin_{h\in H}L_D(h)\qquad \text{non è calcolabile(il valore che rende minimo $L_D$) }\\\\
&\hat h_s \in argmin_{h\in H}L_S(h)= \frac{1}{m}\sum_{i=1}^{m}l(h,z_i)
\end{align}
$$

Il nostro obbiettivo è garantire che $L_D(\hat h_s<L_D(h^*)+\epsilon$ 
Quello che possiamo dire noi è:
$$
P[L_D(\hat h_s>L_D(h^*)+\epsilon]<\delta
$$
Questo accade se:
$$
\displaystyle m>\frac{2}{\epsilon^2}\log\left(\frac{2|H|}{\delta}\right)
$$

Per ottenerlo bisogna:
1. Uniform convergence of $L_S(h)$ to $L_D(h)$                    $\forall h\  |\  L_S(h)-L_D(h)|<\epsilon$ 
2. Il passo precedente garantisce che  $L_D(\hat h_s)<L_D(h^*)+2\epsilon$ 
3. Fare dei *probabilistic statements* sul punto 1


Procedimento:
1. 
### Definition $\epsilon$-Representative

Diciamo che un training set $S$ è $\epsilon$-Representative se:
$$
|L_S(h)-L_D(h)|<\epsilon\qquad\qquad \forall h\in H
$$
###
2. Se  $S$ è $\epsilon/2$-Representative allora:   
$$L_D(\hat h_s)<L_D(h^*)+\epsilon$$
Per provarlo possiamo dire che:
$$
\begin{align}
&L_D(\hat h_s)\leq L_S(\hat h_s)+\epsilon/2\qquad\text{$L_S(\hat h_s)$ è il valore minimo di $L_S$}\\\\
&\Rightarrow L_D(\hat h_s)\leq L_S(h^*)+\epsilon/2\qquad \\\\
&\text{Per la definizione di $\epsilon$-rapresentative(considerando $\epsilon/2$) possiamo dire che:}\\\\
&L_S(h^*)\leq L_D(h^*)+\epsilon/2\\\\
&\Rightarrow L_D(\hat h_s)\leq L_D(h^*)+\epsilon/2+\epsilon/2
\end{align}
$$

3. Qual'è la probabilità che $S$ sia $\epsilon/2$-rapresentative? 
(D'ora in poi $\epsilon/2$ viene sostituito con $\epsilon$ per comodità)

$$
\begin{align}
&P[S \text{ is $\epsilon$ -representative}]>1-\delta&\forall h\in H |L_D(h)-L_S(h)|<\epsilon\\
&P[S\text{ is not $\epsilon$ -representative}]<\delta&\exists h\text{ s.t. }|L_D(h)-L_S(h)|>\epsilon
\end{align} 
$$
--- 




### Refresh of probability
 ---
$$
\begin{align}
&L_S(h)=\frac{1}{m}\sum_{i=1}^m l(h,z_i)=\frac{1}{m}\sum_{i=1}^m w_i 
&w_i\text{ compongono una distribuzione che non conosciamo}\\
&\hat\mu=\frac{1}{m}\sum_{i=1}^m w_i\\\\
&\downarrow m\rightarrow+\infty\\\\
&\mu = E [w_i]\qquad\qquad (\ L_D(h)=E[l(h,z_i)]\ )
&\text{ valore atteso di $w_i$}\\

\end{align}
$$
---
Question: puoi trovare un limite superiore di questa probabilità?
#### Chebicev inequality
$$
\begin{align}
P[|\hat\mu_m-\mu|>\epsilon]&<\displaystyle\frac{\sigma^2\hat\mu_m}{\epsilon^2}\\
&<\frac{costant}{m}
\end{align}
$$ 

---
$$
\begin{align}
&x,y\quad E(x)=E(y)=0\\
&var(x+y)=E[(x+y)^2]=\underbrace{E[x^2]}_{var\ x}+\underbrace{E[y^2]}_{var\ y}+2\underbrace{E[xy]}_{0\text{ if uncorrelated}}\\
\\


\end{align}
$$
${\Large\sigma_{\hat\mu_m}=\frac{m\cdot var(w)}{m^2}=\frac{var(w)}{m}}$    

$\color{orange}var(ax) =a^2var(x)$  che è una costante

---


#### Hoeffding inequality
Avendo:
- $x_i$ sono i.i.d. variabili casuali
- $x_i\in[a,b]$ 
$E(x_i)=\mu$             $E$= mean           $\mu$=true average
$$
P\left[\left|\frac{1}{m}\sum_{i=1}^mx_i-\mu\right|>\epsilon\right]\leq 2e^{\huge-\frac{2m\epsilon^2}{(b-a)^2}}
$$
Essendo esponeziale è più ripido rispetto a quella precedente e quindi migliore

#### Proposition
If:
$$
m\geq \frac{1}{2\epsilon^2}\log\left(\frac{2|H|}{\sigma}\right)

$$
then:
$$
P[\ \exists h\quad|L_S(h)-L_D(h)|>\epsilon\ ]<\delta
$$
Proof:
$$
\begin{align}
&h\in H\\
&P[\ |L_S(h)-L_D(h)|>\epsilon]< 2e^{\huge-2m\epsilon^2}\\&\text{il denominatore dell'esponente è andato via perchè a=0 b=1 b-a=1}\\
&x_i=l\quad bouded\ [0,1]
\end{align}
$$
Where:
$$
\begin{align}
&L_S(h)=\sum_{i=1}^ml(h,z_i)\\
&L_D(h)=E[l(h,z_i)]\\
\\
&P\left[\bigcup_{h\in H}\ s:|L_S(h)-L_D(h)|>\epsilon\right]\leq \sum_{h\in H} P\left[|L_S(h)-L_D(h)|>\epsilon\right]\leq 2|H|e^{\large-2m\epsilon^2}
\end{align}
$$

$$
\begin{align}
m^*\ s.t.\qquad &2|H|e^{\Large-2m^*\epsilon^2}=\delta\\
&2m^*\epsilon^2=log\left(\frac{2|H|}{\delta}\right)\\
&m^*=\frac{1}{2\epsilon^2}log\left(\frac{2|H|}{\delta}\right)\\
\\
&\delta=2|H|e^{\Large-2m^*\epsilon^2} \text{allora S è $\epsilon$-rapresentative}
\end{align}
$$

Noi vogliamo garantire che:
$$
P[L_D(\hat h_s)>L_D(h^*) +\epsilon]<\delta
$$
Questo regge se $S$ è $\epsilon/2$-Rapresentative
quindi diventerà:
$$
m>\frac{2}{\epsilon^2}log\left(\frac{2|H|}{\delta}\right)\\
$$
(per dimezzare l'errore servono il quadruplo dei dati)
