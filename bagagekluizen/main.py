kluizen_file = 'kluizen.txt'
kluizen_max = 12

def read_all_from_kluizen():
      file = open(kluizen_file)
      return file.read().splitlines()

def add_to_kluizen(str):
      with open(kluizen_file, 'a') as file:
            file.write(str + "\n")

def remove_kluis(str):
      pass

def kluis_format(kluisnummer, wachtwoord):
      return str(kluisnummer) + ";" + str(wachtwoord)

def toon_aantal_kluizen_vrij(): 
      return kluizen_max - len(read_all_from_kluizen());

def lijst_kluizen_vrij():
      kluizen_list = list(range(1, kluizen_max + 1))
      if toon_aantal_kluizen_vrij() > 0:
            for kluis in read_all_from_kluizen():
                  kluizen_list.remove(int(kluis.split(';')[0]));

      return kluizen_list

def maak_nieuwe_kluis(kluisnummer, wachtwoord):
      add_to_kluizen(kluis_format(kluisnummer, wachtwoord))

# Display functions
def display_aantal_kluizen_vrij():
      print("Er zijn in totaal " + str(toon_aantal_kluizen_vrij()) + " kluizen vrij.")

def display_maak_nieuwe_kluis():
      display_aantal_kluizen_vrij()
      if toon_aantal_kluizen_vrij() <= 0:
            print("Er zijn geen kluizen vrij")
      else:
            nieuwe_kluis = lijst_kluizen_vrij()[0]  # Geef het nummer van de eerste kluis die vrij is
            print("Kluisnummer " + str(nieuwe_kluis) + " is voor jou gekozen.")
            wachtwoord = input("Kies een wachtwoord: ")
            maak_nieuwe_kluis(nieuwe_kluis, wachtwoord)

def display_open_kluis():
      kluisnummer = input("Kies jouw kluisnummer: ")
      wachtwoord = input("Kies jouw wachtwoord: ")
      for kluis in read_all_from_kluizen():
            if kluis_format(kluisnummer, wachtwoord) == kluis:
                  print("Je hebt je kluis geopend")
                  return

      print("Je wachtwoord/kluisnummer was incorrect.")

def display_verwijder_kluis():
      pass

def display_menu():
      menu_options = {
            1 : display_aantal_kluizen_vrij,
            2 : display_maak_nieuwe_kluis,
            3 : display_open_kluis,
            4 : display_verwijder_kluis,
      }


      print("1: Ik wil weten hoeveel kluizen nog vrij zijn\n" +
      "2: Ik wil een nieuwe kluis\n" +
      "3: Ik wil even iets uit mijn kluis halen\n" +
      "4: Ik geef mijn kluis terug\n")

      choice = input("Maak een keuze: ")

      try: 
            if int(choice) <= len(menu_options):
                  menu_options[int(choice)]()
      except ValueError:
            print("Ongeldige waarde ingevoerd")

display_menu()