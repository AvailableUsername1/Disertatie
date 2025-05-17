# Disertatie
Această pagină conține codul folosit pentru lucrarea mea de disertație. Ea conține 2 părți:
1. Codul utilizat pentru formular
2. Codul utilizat pentru procesarea datelor, obținerea de imagini și analiza statistică a lor

## Codul pentru formular (în folderul numit ”formular”)
Fișiere:
 - app.py: partea de backend
 - data.db: baza de date unde vor fi salvate răspunsurile participanților
 - static: folderul ce conține imaginile
 - templates: folderul ce conține codul pentru paginile web văzute de utilizator
 - environment.yml: fișier ce conține modulele necesare funcționării formularului. Este utilizat pentru a recrea mediul în care s-a creat formularul

## Codul pentru procesarea datelor (în folderul numit ”procesare”)
Fișiere:
 - procesare.ipynb - curăță datele primite din formular
 - data.csv - rezultatul fișierului procesare.ipynb și inputul fișierului stat.Rmd (baza de date)
 - stat.Rmd - aici se vor analiza statistiic datele

Acest folder poate fi folosit pentru a recrea lucrarea mea de disertație.
