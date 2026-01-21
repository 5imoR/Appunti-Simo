#CO-L19-1
$$
\begin{cases}
\min f(x)\\
g_i(x)\le 0\quad i=1,\dots, m\\
h_i(x)=0\quad i = 1,\dots,p
\end{cases}
$$
- $D\ne \emptyset$
- NON assumiamo che sia convesso
- $p^*$ optimal value

L'idea è di fare una [[Integral Programming#Relaxation|relaxation]] sul problema spostando i vincoli all'interno della objective function con dei pesi.
Aggiungendo moltiplicatori $\lambda\in\mathbb R^m_+$ per le $m$ disequazioni e dei moltiplicatori liberi $\pi\in\mathbb R^p$ per le $p$ equazioni andando ad ottenere la "Lagrangian objective function":
$$
L(x,\lambda,\pi)=f(x)+\sum^m_{i=1}\lambda_i g_i(x)+\sum^p_{i=1}\pi_ih_i(x)
$$
Il quale dominio è formato da: $D\times \mathbb R^m_+\times \mathbb R^p$ 
Per $(\lambda,\pi)$ fissati possiamo ottimizzare $L(x,\lambda,\pi)$ su $x$ ottenendo la "Lagrange dual function":
$$
l(\lambda,\pi)=\inf_{x\in D}L(x,\lambda,\pi)
$$
Questa  è sempre una concave function e da un lower bound di $p^*$ 
### Proposition 7.1
Per qualunque $\lambda\ge 0, \pi \to l(\lambda,\pi)\le p^*$ 
#### Proof
[[Duality.pdf#page=1|guarda il pdf]] in fondo alla pagina
$$
l(\lambda,\pi)\le L(x,\lambda,\pi)\le f(x)
$$
###
Quindi chiamiamo un punto dual feasible se $\lambda\ge 0$ e $l(\lambda,\pi)>-\infty$.
Dato che $l(\lambda,\pi)$ da sempre un lower bound possiamo chiamare ciò che segue come dual optimization problem
$$
\begin{cases}
\sup l(\lambda,\pi)\\
\lambda\ge 0
\end{cases}
$$
Questo è sempre un [[Convex Set|convex optimization problem]] dato che il dominio è convesso e che la funzione duale è concava.

Chiamiamo $d^*$ il valore ottimo del Lagrange dual problem, per definizione anche questo è un lowerbownd di $p^*$. La differenza tra i due è chiamata optimal duality gap ed è sempre non negativa.
## Slater's conditions
Consideriamo ora un convex optimization problem nel quale $f, g_i$ sono convesse e l'equazione $h(x)$ è affine e può quindi essere scritta come $Ax=b$
### Definition 7.1
Un punto $x\in\text{rel interior } D\ s.t.\ g_i(x)<0$ e $Ax=b$ è chiamato *strictly feasible solution*
### Theorem 7.1
Se un convex optimization problem ammette uno strictly feasible point $\bar x$ allora regge la *strong duiality* ed è raggiuinta ovvero esiste $l(\lambda^*,\pi^*)=d^*=p^*$ 
#### Proof
[[Duality.pdf#page=2|guarda il pdf]] 

## Complementary slackness
#CO-L20-1
Finora abbiamo trovato condizioni sufficienti per la strong duality.
Ora prendiamo un altro punto di vista: assumiamo che ci sia strong duality e che sia raggiungibile e vediamo quali condizioni necessarie possiamo ottenere. NON stiamo assumendo convexity.
- $(x^*)$ soluzione ottima primale
- $(\lambda^*,\pi^*)$ soluzione ottima duale
Per la strong duality si ha:
$$
\begin{align}
f(x^*)&=l(\lambda^*,\pi^*)\\
&=\inf_{x\in D} f(x)+\sum^m_{i=1}\lambda_i^* g_i(x)+\sum^p_{i=1}\pi_i^*h_i(x)\\
&\le f(x^*)+\underbrace{\sum^m_{i=1}\lambda_i^* g_i(x^*)}_{\le 0}+\underbrace{\sum^p_{i=1}\pi_i^*h_i(x^*)}_{=0}\\
&\le f(x^*)
\end{align}
$$
Questo implica  che tutte le disuguaglianze reggono nel caso dell'uguaglianza e quindi
$$\sum^m_{i=1}\lambda_i^* g_i(x^*)=0$$
Dato che ogni termine della sommatoria è non positivo questo implica che tutti gli elementi della sommatoria sono pari a $0$ 
Questo prende il nome di  complementary slackness conditions. L'intuizione è la stessa del caso [[Linear Programming]] se un vincolo è inutile nella soluzione ottima allora il suo moltiplicatore è $0$ mentre se un moltiplicatore duale è strettamente positivo allora il vincolo deve essere stretto.
Un altra conseguenza è che $x^*$ è un minimizer di $L(x,\lambda^*,\pi^*)$ 
## KKT conditions
Assumiamo ora che le funzioni $f,g,h$ siano derivabili. Allora anche $L(x,\lambda,\pi)$ è derivabile rispetto a $x$ e dato che $x^*$ è la soluzione ottima il gradiente deve essere pari a $0$ per quel valore di $x$
$$
\nabla f(x^*)+\sum_{i=1}^m\lambda_i^*\nabla{g_i}(x^*)+\sum_{i=1}^p\pi_i^*\nabla h_i(x^*)=0
$$
Qundi se la strong duality regge e le funzioni sono differenziabili qualunque *optimal primal-dual pair* $(x^*,(\lambda^*,\pi^*))$  deve soddisfare il seguente sistema:
$$
\begin{cases}
g(x^*)\le 0\\
h(x^*)=0\\
\lambda^*\ge 0\\
\lambda_i^*g_i(x^*)=0\qquad i =1\dots m\\
\nabla f(x^*)+\sum_{i=1}^m\lambda_i^*\nabla{g_i}(x^*)+\sum_{i=1}^p\pi_i^*\nabla h_i(x^*)=0
\end{cases}
$$
Essere una soluzione di questo sistema è una condizione necessaria per essere un *optimal primal-dual pair*. 
Se tutte le funzioni sono convesse possiamo anche provare che qualunque *optimal primal-dual pair* che soddisfa il KKT system è ottimo con $0$ duality gap.

Attenzione questo non ci garantisce di trovare qualunque soluzione, ma torna utile sono quando tutte le condizioni del sistema sono assecondate, in questo caso si ha:
- se strong duality regge allora il KKT sys da una condizione necessaria
- se le funzioni sono convesse  il KKT sys da una condizione sufficiente
- se le funzioni sono convesse e [[Lagrangian Duality#Slater's conditions|Slater's conditions]] sono soddisfatte allora il KKT sys è sia necessario che sufficiente