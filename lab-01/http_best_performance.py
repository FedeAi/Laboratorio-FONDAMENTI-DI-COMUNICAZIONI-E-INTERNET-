import requests

siti = ['http://www.google.com','http://www.netflix.com']

def calcola_response_time(url, nreq = 5):
    statistiche = []
    for _ in range(nreq):
        r = requests.get(url)
        statistiche.append(r.elapsed.microseconds/1000)
    return (sum(statistiche)/len(statistiche),url)
media_siti = []
for sito in siti:
    media_siti.append(calcola_response_time(sito))
print("-"*35)
print("Better avereaged response time for url: ", min(media_siti)[1])
print("Average response time: ", min(media_siti)[0])


