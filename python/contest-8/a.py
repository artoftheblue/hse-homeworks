import pandas as pd
import string

def length_stats(words):
    wordlist = set(words.lower().translate(str.maketrans("", "", string.punctuation + string.digits)).split())
    s = pd.Series([len(word) for word in wordlist], index=wordlist)
    s = s.sort_index()
    return s

bullshit_text = "tHIS iS some REALLY funny bullshit for testin4234jsgkldjd, 1324,ad, ,32,dsf, as, , ,, , ,,,, "

print(length_stats(bullshit_text))
