#!/usr/bin/python3
import xmltodict

xml_file = 'data.xml'
station_text_format = "{} \t- {}"

def read_xml():
      file = open(xml_file)
      return xmltodict.parse(file.read())

def data_to_text(treinXML):
    case_1 = []
    case_2 = []
    case_3 = []
    for station in treinXML["Stations"]["Station"]:
        case_1.append(station_text_format.format(station["Code"], station["Type"]))
        case_3.append(station_text_format.format(station["Code"], station["Namen"]["Lang"]))

        if station["Synoniemen"] is not None:
            case_2.append(station_text_format.format(station["Code"], station["Synoniemen"]))

    return case_1, case_2, case_3

def display_station_case(textList):
    for val in textList:
        print(val)

def display_stations():
    treinXML = read_xml()
    case_1, case_2, case_3 = data_to_text(treinXML)

    print("Dit zijn de codes en types van de {} stations:".format(len(treinXML["Stations"]["Station"])))
    display_station_case(case_1)
    print()

    print("Dit zijn alle stations met één of meer synoniemen:")
    display_station_case(case_2)
    print()

    print("Dit is de lange naam van elk station:")
    display_station_case(case_3)


display_stations()
