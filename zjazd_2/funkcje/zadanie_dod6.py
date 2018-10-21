# SPK*(1 + P/100)^N

def odsetki(SPK=0, P=0, N=0):
    SPK = float(input("Podaj stan początkowy konta: "))
    P = float(input("Podaj oprocentowanie: "))
    N = int(input("Podaj liczbę lat: "))

    kwota_finalna = round(SPK*(1 + P/100)**N)

    print(f"Odsetek wychodzi {kwota_finalna-SPK} czyli hajsiwa łącznie {kwota_finalna}.")

odsetki()