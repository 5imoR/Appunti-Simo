# 📘 Dinamica dei Sistemi – Formulario

---

## 🔹 Momento Angolare

$$\vec{L} = \vec{r} \times \vec{p} = \vec{r} \times (m \, \vec{v})$$  

- **$\vec{L}$** = momento angolare rispetto a un punto $[kg \, m^2/s]$  
- **$\vec{r}$** = posizione rispetto al polo $[m]$  
- **$\vec{p}$** = quantità di moto $[kg \, m/s]$  
- **$m$** = massa $[kg]$  
- **$\vec{v}$** = velocità $[m/s]$  

---

## 🔹 Momento della Forza (o Coppia)

$$\vec{M} = \vec{r} \times \vec{F}$$  

- **$\vec{M}$** = momento della forza rispetto al polo $[N \, m]$  
- **$\vec{r}$** = posizione del punto di applicazione della forza $[m]$  
- **$\vec{F}$** = forza applicata $[N]$  

---

## 🔹 Teorema del Momento Angolare

$$\frac{d \vec{L}}{dt} = \vec{M}_{tot}$$  

- **$\vec{L}$** = momento angolare $[kg \, m^2/s]$  
- **$\vec{M}_{tot}$** = momento risultante delle forze esterne $[N \, m]$  
- **$t$** = tempo $[s]$  

---

## 🔹 Centro di Massa

$$\vec{r}_{cm} = \frac{\sum_i m_i \vec{r}_i}{M}$$  

- **$\vec{r}_{cm}$** = posizione del centro di massa $[m]$  
- **$m_i$** = masse delle particelle $[kg]$  
- **$\vec{r}_i$** = posizione delle particelle $[m]$  
- **$M = \sum_i m_i$** = massa totale del sistema $[kg]$  

---

### Velocità del centro di massa

$$\vec{v}_{cm} = \frac{\sum_i m_i \vec{v}_i}{M}$$  

- **$\vec{v}_{cm}$** = velocità del centro di massa $[m/s]$  
- **$m_i$** = masse delle particelle $[kg]$  
- **$\vec{v}_i$** = velocità delle particelle $[m/s]$  
- **$M$** = massa totale del sistema $[kg]$  

---

### Accelerazione del centro di massa

$$\vec{a}_{cm} = \frac{\sum_i m_i \vec{a}_i}{M}$$  

- **$\vec{a}_{cm}$** = accelerazione del centro di massa $[m/s^2]$  
- **$m_i$** = masse delle particelle $[kg]$  
- **$\vec{a}_i$** = accelerazione delle particelle $[m/s^2]$  
- **$M$** = massa totale del sistema $[kg]$  

---

## 🔹 Quantità di Moto di un Sistema

$$\vec{P} = \sum_i m_i \vec{v}_i = M \, \vec{v}_{cm}$$  

- **$\vec{P}$** = quantità di moto totale del sistema $[kg \, m/s]$  
- **$m_i$** = masse delle particelle $[kg]$  
- **$\vec{v}_i$** = velocità delle particelle $[m/s]$  
- **$M$** = massa totale del sistema $[kg]$  
- **$\vec{v}_{cm}$** = velocità del centro di massa $[m/s]$  

---

## 🔹 Equazioni Cardinali della Dinamica

### Prima equazione cardinale (traslazione del centro di massa)

$$\vec{F}_{ext} = M \, \vec{a}_{cm}$$  

- **$\vec{F}_{ext}$** = risultante delle forze esterne $[N]$  
- **$M$** = massa totale del sistema $[kg]$  
- **$\vec{a}_{cm}$** = accelerazione del centro di massa $[m/s^2]$  

### Seconda equazione cardinale (rotazione attorno al centro di massa)

$$\frac{d \vec{L}_{cm}}{dt} = \vec{M}_{ext,cm}$$  

- **$\vec{L}_{cm}$** = momento angolare rispetto al centro di massa $[kg \, m^2/s]$  
- **$\vec{M}_{ext,cm}$** = momento risultante delle forze esterne rispetto al centro di massa $[N \, m]$  
- **$t$** = tempo $[s]$  

➡️ Per un corpo rigido che ruota attorno a un asse fisso (asse principale):  

$$\vec{M}_{ext,cm} = I \, \alpha$$  

- **$I$** = momento di inerzia del corpo rispetto all’asse $[kg \, m^2]$  
- **$\alpha$** = accelerazione angolare $[rad/s^2]$  

---

## 🔹 Traslazione del Centro di Massa e Rotazione

### Conservazione del momento angolare interno
$$L' = 0$$  

- **$L'$** = momento angolare interno rispetto al centro di massa $[kg \, m^2/s]$  

---

### Quantità di moto totale
$$\vec{p}_{tot} = M_{tot} \, \vec{v}_{cm}$$  

- **$\vec{p}_{tot}$** = quantità di moto totale del sistema $[kg \, m/s]$  
- **$M_{tot}$** = massa totale del sistema $[kg]$  
- **$\vec{v}_{cm}$** = velocità del centro di massa $[m/s]$  

---

### Momento angolare totale
$$\vec{L}_o = \vec{r}_{cm} \times (M_{tot} \, \vec{v}_{cm})$$  

- **$\vec{L}_o$** = momento angolare del sistema rispetto a un polo $O$ $[kg \, m^2/s]$  
- **$\vec{r}_{cm}$** = posizione del centro di massa rispetto al polo $O$ $[m]$  
- **$M_{tot}$** = massa totale del sistema $[kg]$  
- **$\vec{v}_{cm}$** = velocità del centro di massa $[m/s]$  

---

### Energia cinetica del centro di massa
$$E_k = \tfrac{1}{2} M_{tot} \, v_{cm}^2$$  

- **$E_k$** = energia cinetica traslazionale del centro di massa $[J]$  
- **$M_{tot}$** = massa totale del sistema $[kg]$  
- **$v_{cm}$** = velocità del centro di massa $[m/s]$  

---

### Velocità di una particella del sistema
$$\vec{v}_i = \vec{v}_{cm} + \vec{\omega} \times \vec{r}_i$$  

- **$\vec{v}_i$** = velocità della particella $i$ $[m/s]$  
- **$\vec{v}_{cm}$** = velocità del centro di massa $[m/s]$  
- **$\vec{\omega}$** = velocità angolare del corpo $[rad/s]$  
- **$\vec{r}_i$** = posizione relativa della particella $i$ rispetto al centro di massa $[m]$  
