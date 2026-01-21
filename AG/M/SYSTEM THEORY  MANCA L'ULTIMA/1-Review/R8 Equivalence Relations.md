#ST-L20-2
### Equivalence Relation
Dato un set $S$ una relazione su $S$ è chiamata equivalence Relation($\sim$) se soddisfa tre proprietà:
- Reflexivity: $\forall a\in S\ a\sim a$
- Symmetry: $\forall a,b\in S\ a\sim b\Rightarrow b\sim a$ 
- Transitivity: $\forall a,b,c\in S\ a\sim b,\ b\sim c\Rightarrow a\sim c$ 

### Equivalence Class
 Dato un set $S$ e un equivalence relation $\sim$  associamo, per ogni $a\in S$, la sua Equivalent Class:
 $$[a]\triangleq\set{b\in S:a\sim b}$$
 se $a,b\in S$ allora possiamo avere solo 2 casi:
 - $a\sim b\Rightarrow [a]=[b]$ 
 - $a\nsim b\Rightarrow [a]\cap[b]=\emptyset$ 
 $\Rightarrow$ Il set di classi equivalenti ci da una partizione di $S$ 
 We denote the set of all equivalence classes con $S_{/\sim}$ 

### Family of Invariant for $\sim$
Dato un set $S$ ed un equivalence relation $\sim$  una famiglia di funzioni $f_1(\cdot)\dots f_r(\cdot)$ definita in $S$  è una famiglia di invarianti per $\sim$ $$a,b\in S\ a\sim b \Rightarrow f_1(a)=f_1(b)\dots f_r(a)=f_r(b)$$
	Un invariante equivale a $a,b\in S\ a\sim b\Rightarrow f(a)=f(b)$
Si dice completa se:
$$
a,b\in S\ a\sim b \iff f_1(a)=f_1(b)\dots f_r(a)=f_r(b)
$$
In particolare questo concetto specifica una singola invariant function $f(\cdot)$ 