import scispacy
import spacy
import pandas as pd
import en_core_sci_md
import en_core_sci_scibert
import en_ner_jnlpba_md
from spacy import displacy

nlp = en_core_sci_md.load()
nlp1 = en_core_sci_scibert.load()

alcohol_warning_raw = 'It is not known whether it is safe to consume alcohol with Yasofyl 400mg Tablet. Please consult your doctor.'
alcohol_warning = nlp(alcohol_warning_raw)
list_alcoholwarning = [alcohol_warning_raw] + [alcohol_warning.ents]

print(list_alcoholwarning)

def sep_sent(text):
    dif_text = []
    sent = ""
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == "!":
            if (i-1 != ".") or (i+1 != "."):
                sent = sent + '.'
                dif_text = dif_text + [sent]
                sent = ""
        else:
            sent = sent + text[i]
    return dif_text

['It is not known whether it is safe to consume alcohol with Yasofyl 400mg Tablet. Please consult your doctor.', (consume, alcohol, Yasofyl, Tablet, Please, consult, doctor)]
