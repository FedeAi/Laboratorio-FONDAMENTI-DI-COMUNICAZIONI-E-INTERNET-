# Valutazione del tempo di risposta di un server google
import requests
import matplotlib
import matplotlib.pyplot as plt
r = requests.get('http://www.google.com')

print(type(r))
print(r.url)
print("qual è lo status code della richiesta? --", r.status_code)
#http status_code: 2xx successo, 4xx client error (400 errore nell' url), 5xx erver error
print("tempo di risposta [ms]: --", r.elapsed.microseconds/1000)

#Ripetere la misura 10 volte per estrarre statistiche riguardo il fenomeno che stiamo osservando
statistiche = []
for i in range(20):
    print("richiesta #",i)
    r2 = requests.get('http://www.google.com')
    statistiche.append(r2.elapsed.microseconds/1000)
    #print("tempo di risposta [ms]: --", r2.elapsed.microseconds/1000)
print("Tempo di risposta minimo: --", min(statistiche))
print("Tempo di risposta massimo: --", max(statistiche))
print("Tempo di risposta medio: --", sum(statistiche)/len(statistiche))



# Valutare il tempo di risposta medio, minimo e massimo
# 1) Salvare le 10 misure in un vettore 
# 2) Fare il print delle statistiche

# Creare il grafico delle statistiche

plt.figure()
plt.plot(statistiche)
plt.plot(statistiche, "*")
plt.ylim([min(statistiche)*0.9,max(statistiche)*1.1])
plt.title("Test Server http://www.google.com")
plt.ylabel("Response time [ms]")
plt.xlabel("#request")
plt.grid()
plt.show()
