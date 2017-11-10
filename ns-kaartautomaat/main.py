#!/usr/bin/python3

stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht"]

price_per_station = 5

def get_index_station(station):
    index_station = None
    if station in stations:
        index_station = stations.index(station)

    return index_station


def ask_begin_station():
    begin_station = input("Wat is je beginstation? ")
    return begin_station, get_index_station(begin_station)


def ask_eind_station():
    eind_station = input("Wat is je eindstation? ")
    return eind_station, get_index_station(eind_station)


while True:
    while True:
        name_begin, index_begin = ask_begin_station()
        if index_begin is not None:
            break

    while True:
        name_eind, index_eind = ask_eind_station()
        if index_eind is not None:
            break

    print("Het beginstation " + name_begin + " is het " + str(index_begin) + "e station in het traject.")
    print("Het eindstation " + name_eind + " is het " + str(index_eind) + "e station in het traject.")

    if index_begin < index_eind:
        distance = index_eind - index_begin;
        print("De afstand bedraagt " + str(distance) + " station(s).")
        print("De prijs van het kaartje is " + str(distance * price_per_station) + " station(s).")

        print("Jij stapt in de trein in: " + name_begin)

        if distance != 1:
            for station_index in range(index_begin + 1, index_eind):
                print("- " + stations[station_index])

        print("Jij stapt uit in: " + name_eind)

        break
    else:
        print("Het eindstation nummer is lager dan het beginstation")
        continue
