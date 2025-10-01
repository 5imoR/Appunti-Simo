#ML-L1
Presentazione del corso e cose inutili
#ML-L2
# Componenti dell'insegnamento
- Input $x \in X = \mathbb{R}^{d=p}$ \[vettore di $p$ valori dal quale vogliamo fare predizioni]
- Output $y\in Y$           \[valore che vogliamo prevedere]
- Target Function $f:X\rightarrow Y$ \[formula che vorremmo imparare]
- Hypotesis $h:X\rightarrow Y$ \[formula che elaboriamo]\[Model classes $H$ $(h\ in\ H)$]
- Data (esempi) $(x_1,y_1)...(x_n,y_n)$   $S=sample = \{\underbrace{(x_i,y_i)}_{z_i} \quad i= 1\dots n\}$ 
Sample set= training set = learning data = examples è:
- Indipendent
	esempio: se alleni la macchina a riconoscere un gatto non puoi chiedergli di riconoscere un serpente
- Identical distribution
	esempio: se vuoi vedere quanto spesso esce testa devi sempre usare la stessa moneta sennò  quello che stai misurando non ha senso
# Learning Process (semplificato)
![[LearningProces]]
h deve rimanere generica per poter funzionare anche con valori al di fuori di quelli con il quale è stata allenata.
L'algoritmo deve essere in grado di bilanciare il numero di parametri

# Types of Learning

- Supervised learning: $y_i$ sono conosciute e il training set è del tipo: $\{(x_1,y_1)...\}$ 
- Unsupervised learning: $y_i$ sono ignote e il training set è del tipo:$x_1,x_2 ...$
L'output può essere:
- discreto
- continuo(un esempio è il valore della temperatura)

|           | supervised                          | unsupervised                 |
| --------- | ----------------------------------- | ---------------------------- |
| discrete  | classification or<br>categorization | clustering                   |
| continous | regression                          | dimensionality<br> reduction |

- Reinforcement Learning: L'agente viene ricompensato per svolgere il compito correttamente. In control system è l'opposto si guarda la perdita che deve essere più vicino allo zero possibile

# Binary Classification(non mi è chiaro quello che segue)
- $x \in X (= \mathbb{R}^d)$
- $y\in \{0,1\}$
- $S=\{z_i\quad i=1 ... n\}$ 

**Assumption on data**
- $x\sim \overline S_x$ 
- $y|x \sim \overline S_{y|x}$ 
**Loss Function**
- $l(h,z)\geq 0$
- close to $0$ if it's good
- $l(h,z)=\begin{cases}1\quad h(x) \neq y\\0\quad h(x)=y\end{cases}$ 
**Empirical Loss (Risk)**
- $L_s=1/m\sum_{i=1}^ml(h,z_i)$ 
- $h \in H$
- $S= \{z_i\quad i=1 ...m\}$
da finire