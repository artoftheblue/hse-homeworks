import sys
import re
from collections import Counter

def find_most_common_words(text, num):
    temp = re.findall("[A-Za-z]+", text) 
    counter = Counter(temp)
    return list(counter.most_common(num))

print(find_most_common_words("aa b c d e f $$#$#$ f", 5))
    
