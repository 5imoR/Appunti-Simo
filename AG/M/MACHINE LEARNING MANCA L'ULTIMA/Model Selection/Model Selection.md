#ML-L13-1
# Il problema
Bisogna scegliere il modello migliore ovvero quello in grado di predirre con meno errore

**ERM** ci da $h=\arg\min_{h\in H} L_S(h)$ ed in linear regression abbiamo: $H=\set{h(x)_h(x)=w^Tx\quad w\in \mathbb R^d}$

Cosa succede se sono presenti più candidati?
#### Esempio
![[H1]]
serve trovare $h(x)$ tale che $y(x)\simeq h(x)$ 
- $H_1=H_{LIN}=\set{h(x):h(x)=w_0+w_1x}$
- $H_2=\set{h(x):h(x)=w_0+w_1x+w_2x^2}$
- $H_3=\begin{bmatrix}w_0 & w_1 & w_2 & w_3 \\\end{bmatrix}\begin{bmatrix}x_0 \\x_1 \\x_2 \\x_3 \\\end{bmatrix}$ 
Questo è lineare in $w$ ma non in $x$. Questo non va ad impedirci di fare ciò che facevamo in LR
#### Trovare l'**ERM** 

$\displaystyle\hat h_2= \arg\min_{h\in H_2} L_S(h)\iff\hat w =\arg \min_{w\in \mathbb R^3}\frac1m \sum^m_{i=1}\left(y_i-w^T\begin{bmatrix}1 \\x_i \\x_i^2 \\\end{bmatrix}\right)$  
ed è da scegliere il più giusto tra $h_1$ ed $h_2$ 
![[h2]]

Come si sceglie il miglior modello?
Non si può guardare semplicemente l'ERM minore dato che una funzione di grado maggiore avrà sempre un errore minore ma potrebbe non andare a predirre correttamente

# Le possibili soluzioni
- ![[Train Validation Split]] 