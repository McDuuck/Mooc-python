# Tee ratkaisu tänne
def anagrammi(a, b):
    a = sorted(a)
    b = sorted(b)
    if a == b:
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrammi("talo", "tola"))
    print(anagrammi("tammi", "mitta"))
