# Dokumentarij je aplikacija za ispis i unos studenata
# na kolegiju Razvoj poslovnih aplikacija

class DokumentarijView:
    def display_title_bar(self):
        print("\t****************************************************")
        print("\t***  Dokumentarij - Razvoj poslovnih aplikacija  ***")
        print("\t****************************************************")

    def get_user_choice(self):
        # Ispisujemo korisniku meni što može raditi u aplikaciji
        # Na kraju ga pitamo i uzimamo njegov odabir te te taj odabir vracamo 
        print("\n[1] Pogledaj listu studenata.")
        print("[2] Dodaj novog studenta.")
        print("[x] Izlaz.")
        return input("Što želite napraviti u dokumentariju?")

    def show_names(self):
        # prikazuje imena svih studenata dodanih u listu
        print("\nOvo je popis studenata na kolegiju Razvoj poslovnih aplikacija 2019/2020:\n")
        for name in self.names:
            print(name.title())

    def get_new_name(self):
        # uzimamo kroz input od korisnika novo ime te ga dodajemo u listu ako to ime već nije u listi
        new_name = input("\nUnesite ime studenta: ")
        if new_name in self.names:
            print("\n{} je već upisan/a u dokumentariju!".format(new_name.title()))
        else:
            self.names.append(new_name)
            print("\n Dobrodošao/la {}!\n".format(new_name.title()))

class DokumentarijController:
    def __init__(self, view):
        self.view = view


class DokumentarijController:
    def __init__(self, view):
        self.view = view
    
    
    
        
    
    def play(self):
        self.view.names = [] # ZA VJEŽBU: staviti početnu inicijalizaciju varijable names u init metodu (konstruktor) klase Dokumentarij
        choice = ''
        self.view.display_title_bar()
        while choice != 'x':
            choice = self.view.get_user_choice()
            self.view.display_title_bar()
            if choice == '1':
                self.view.show_names()
            elif choice == '2':
                self.view.get_new_name()
            elif choice == 'x':
                print("\nHvala na pregledu/uređivanju dokumentarija. Pozdrav.")
            else:
                print("Greška - treba napraviti kod za hvatanje izuzetaka") # ZA VJEŽBU: napraviti posebnu klasu za hvatanje izuzetaka i raiseati je ovdje
            
if __name__ == "__main__":
    game = DokumentarijController(DokumentarijView())
    game.play()
                
                
            
            
            
        
    
    
    
        
    
    