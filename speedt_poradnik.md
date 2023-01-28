# Speedtest w pythonie 

> czyli prędkość pobierania, wysyłania itd.

## Do zainstalowania moduły :

    pip install speedtest-cli

### Dodatkowe moduły użyte w mojej aplikacji

    pip install tqdm

    pip install colorama

> oczywiście jeżeli nie masz jeszcze ich zainstalowanych


## Czym jest speedtest-cli ?
Speedtest-cli to moduł używany w interfejsie wiersza poleceń do testowania przepustowości Internetu za pomocą speedtest.net. Aby uzyskać prędkość w megabitach, wpisz poniższe polecenie w terminalu.

    speedtest-cli

## Wersja modułu :
    
    speedtest-cli --version

## Wynik testu prędkości w megabitach

    speedtest-cli --bytes

## Pobieranie obrazkowej wersji 

    speedtest-cli --share

## Prosta wersja wyniku testu prędkości

    speedtest-cli --simple

## Aby uzyskać listę wszystkich dostępnych opcji, wpisz poniższe polecenie w terminalu

    speedtest-cli -h

lub

    speedtest-cli --help

## Oto prosty kod dla testów prędkości twojego internetu w pythonie

```py
import speedtest

s = speedtest.Speedtest()

print('Oczekiwanie na zakończenie testu szybkości pobierania...')
dow = s.download()

print('Oczekiwanie na zakończenie testu szybkości wysyłania...')
upload = s.upload()

print(f'Prędkość pobierania: {dow}')
print(f'Szybkość wysyłania: {upload}')
```

## Dzięki za przeczytanie tego poradnika dotyczącego speedtest'a w pythonie !
