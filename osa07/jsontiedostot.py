import json

def tulosta_henkilot(tiedosto: str):
    with open(tiedosto) as file:
        data = file.read()
    henkilot = json.loads(data)

    for ihmiset in henkilot:
        testi = ""
        testi += ihmiset["nimi"] + " "
        testi += str(ihmiset["ika"]) + " vuotta "
        harrastukset = '(' + ', '.join(ihmiset['harrastukset']) + ')'
        testi += harrastukset
        print(testi)
        
    
if __name__ == "__main__":
    tulosta_henkilot("tiedosto1.json")