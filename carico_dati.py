# -*- coding: utf-8 -*-
"""
Created on Wen Dec  21 02:43:23 2022

@author: Angelo
@author: Antonio
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def carico_dati(anno,mese):
    """
    

    Parameters
    ----------
    anno : int
         rappresenta l'anno su cui voglio svolgere l'analisi.
         l'int deve essere di fortmato **** (Esempio: 2022).
    mese : string
        rappresenta il numero del mese su cui voglio svolgere l'analisi.
        l'int deve essere di fortmato ** (Esempio: 04)
    bourogh : string
        rappresenta il distretto su cui voglio svolgere l'analisi.

    Returns
    -------
    il dataset grezzo e il file zone_lookup dove ci sono i nomi dei quartieri e i loro codici
    una stringa nella quale c'è un messaggio 
    nel quale viene specificato l'esito della funzione. Ad esempio 
    "Ho caricato i dati correttamente" o "Non sono riuscito a caricare i dati"

    """
    anno = '2022'
    mese = '04'

    data = pd.read_parquet(f'./dati/anni/{anno}/yellow_tripdata_{anno}-{mese}.parquet')
    #carico la tabella con i nomi dei quartieri e il loro codice
    zone_lookup = pd.read_csv("./dati/tabelle_di_conversione/taxi+_zone_lookup.csv", index_col="LocationID")
    
    print('Ho caricato i dati correttamente')    

    return data, zone_lookup