# Evidencija studenata

Ova aplikacija je namijenjena profesorima kako bi mogli bilježiti prisutnost studenata za pojedini kolegija.


## Funkcionalnosti
* Dodavanje novih studenata
* Brisanje postojećih studenata
* Mjenjanje vrijednosti prisutnosti
* Filtriranje studenata po prisutnosti


## Pokretanje backenda
### Stvaranje docker slike (image)
```python
cd Backend
docker build -t pis .
```
### Pokretanje docker slike
```python
docker run -p 8080:8080 pis
```
