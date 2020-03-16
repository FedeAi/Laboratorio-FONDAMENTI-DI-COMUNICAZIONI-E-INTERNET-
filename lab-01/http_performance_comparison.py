# Paragonare i tempi di risposta di più server http
import requests
import matplotlib
import matplotlib.pyplot as plt
siti = ['http://www.gazzetta.it', 'http://www.netflix.it', 'http://www.facebook.it']

plt.figure() 

for url in siti:
    print("#"*35)
    print("Testing: ", url)
    statistiche = []
    for i in range(10):
        r = requests.get(url)
        statistiche.append(r.elapsed.microseconds/1000)
    
    plt.plot(statistiche, label=url)
    print("Tempo di risposta minimo: ", min(statistiche))
    print("Tempo di risposta medio: ", sum(statistiche)/len(statistiche))
    print("Tempo di risposta massimo: ", max(statistiche))
plt.title("Response time comparison")
plt.ylabel("Response time [ms]")
plt.xlabel("#measure")
plt.legend(loc="lower right", fontsize=8)
plt.grid()
plt.show()