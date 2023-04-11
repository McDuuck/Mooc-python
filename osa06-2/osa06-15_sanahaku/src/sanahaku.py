import re

def hae_sanat(hakusana: str):
    sanat.txt, pattern = hakusana.split(':')
    pattern = re.compile(pattern)
    with open("sanat.txt", 'r') as f:
        text = f.read()
        words = text.split()
        matches = [word for word in words if pattern.search(word)]
        return matches

print(hae_sanat("*vokes"))