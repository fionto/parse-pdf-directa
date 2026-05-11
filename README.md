## Script per il parsing dei file di patrimonio Directa.

# patrimonio-directa

Uno script Python per trasformare l'estratto conto patrimoniale di Directa SIM in un foglio Excel analizzabile.

---

## Il problema

Directa SIM fornisce il rendiconto del portafoglio titoli come PDF. È un documento pensato per essere stampato e letto, non per essere elaborato: i dati sono bloccati in un formato che non si presta ad analisi, confronti nel tempo, o calcoli personalizzati.

Chi vuole rispondere a domande semplici come _"quanto pesa la componente azionaria sul totale?"_ o _"quanti bond governativi ho in portafoglio?"_ deve farlo a mano, ricopiando cifre dal PDF in un foglio Excel.

---

## La soluzione

Questo script legge il PDF di Directa, estrae automaticamente tutti i titoli con le relative quantità e controvalori, li arricchisce con metadati finanziari (tipo di strumento, settore di mercato, ticker) e produce un file Excel pronto per l'analisi.

Il risultato è un foglio Excel con una riga per ogni titolo in portafoglio, ordinato per categoria (azioni, ETF, bond governativi, bond corporate) e formattato per la lettura.

---

## Cosa produce

Per ogni titolo in portafoglio vengono estratti o recuperati questi dati:

| Campo | Fonte |
|---|---|
| Nome (come appare nel PDF) | PDF Directa |
| ISIN | PDF Directa |
| Quantità | PDF Directa |
| Prezzo | PDF Directa |
| Controvalore in EUR | PDF Directa |
| Flag ISEE (asterisco) | PDF Directa |
| Codice FIGI Bloomberg | OpenFIGI API |
| Settore di mercato (Equity, Govt, Corp...) | OpenFIGI API |
| Tipo strumento (Common Stock, ETP, EURO-ZONE...) | OpenFIGI API |
| Nome standardizzato Bloomberg | OpenFIGI API |
| Ticker di borsa | OpenFIGI API |

---

## Note operative

**BTP Italia CUM** — I BTP Italia nella versione con bonus fedeltà (ISIN "CUM") non risultano sul mercato secondario e non sono riconoscibili tramite API. Per questi titoli è necessario indicare manualmente la corrispondenza con l'ISIN della versione di mercato.

**Chiamate API** — I metadati finanziari vengono recuperati tramite [OpenFIGI](https://www.openfigi.com), un servizio Bloomberg gratuito che non richiede registrazione per uso base. Una volta recuperati, i dati vengono salvati in una cache locale e non vengono ri-scaricati nelle esecuzioni successive.

---

## File di test

Il file `estratto_test.pdf` è un rendiconto fittizio intestato a "Mario Rossi" con 10 titoli di esempio (azioni italiane, ETF, BTP, OAT e bond corporate) generato per verificare il corretto funzionamento dello script senza dover usare dati reali.