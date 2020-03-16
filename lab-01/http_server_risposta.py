# Valutazione del tempo di risposta di un server google
import requests
r = requests.get('http://www.google.com')

print(type(r))
print(r.url)
print("qual è lo status code della richiesta? --", r.status_code)
#http status_code: 2xx successo, 4xx client error (400 errore nell' url), 5xx erver error
print("tempo di risposta [ms]: --", r.elapsed.microseconds/1000)