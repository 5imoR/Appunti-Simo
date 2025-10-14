[[FCA]]

<div style="display: flex; gap: 10px;">
  <img src="JackInTheBox.PNG" width="350">
  <img src="JackInTheBoxF.PNG" width="200">
</div>
![[JackInTheBox.PNG]]
questa sinusoide se si va a guardare nel domino della frequenza equivale ad un punto.
![[JackInTheBoxF.PNG]]
### Trasformata di Fourier
La trasformata di fourier permette di passare dal dominio del tempo a quello della frequenza 

$$
\int_{-\infty}^{\infty}{f(t)e^{-jwt}dt}\qquad\qquad e^{jt}=\cos(t)+j\sin(t)
$$
![[fourier.png]]
Nel dominio delle frequenze si vedrà che all'aumentare della frequenza l'ampiezza tende a 0

![[f1.PNG]]



###
![[esF.png]]
 $e^{-\sigma t}$ è dovuto allo smorzamento
 $e^{-jwt}$ è dovuto alla costante elastica 
L'equilibrio di m si ottiene tramite:
$$m\ddot{x}+kx=0$$



### Trasformata di Laplace
Riprende la trasformata di Fourie con delle modifiche per renderla plausibile nel mondo reale
- per avere un effetto serve una causa(viene tolto il tempo negativo)$\textcolor{lightgreen}{■}$
- si tiene conto dello smorzamento$\textcolor{orange}{■}$
$$
\int_\textcolor{lightgreen}{0}^{\infty}{f(t)\ \textcolor{orange}{e^{-\sigma t}}\ e^{-jwt}}dt=\int_\textcolor{lightgreen}{0}^{\infty}{f(t)\ e^{(\textcolor{orange}{-\sigma}-jw)t}}dt
$$
 $(-\sigma -jw)= s$ 

Risolvendola si passa sul piano di S (quello con poli(X) e zeri(O))
![[esL.PNG]]
<div style="display: flex; align-items: center; gap: 15px;">
  <img src="esL1.png" width="200">
  <p>Una volta trovati gli zero e i poli si può trovare la funzione di trasferimento[TF(s)]: zeros/poles </p>
</div>
Solitamente il processo è:
$f(t) \rightarrow \mathcal{L}(f(t))\rightarrow f(s) \rightarrow find \frac{zeros}{poles}\rightarrow get\ impulse\ response$ 