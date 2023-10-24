import pandas as pd
import string

def get_data(wordlist, lengths, number):
    return pd.Series(filter(lambda x: x % 2 == number, lengths), index=filter(lambda x: lengths[wordlist.index(x)] % 2 == number, wordlist)).sort_index().astype("int64")

def length_stats(words):
    wordlist = list(set(words.lower().translate(str.maketrans("", "", string.punctuation + string.digits)).split()))
    lengths = [len(word) for word in wordlist]
    return get_data(wordlist, lengths, 1), get_data(wordlist, lengths, 0)

odd, even = length_stats('Мама мыла раму')
print(odd)
print(even)
