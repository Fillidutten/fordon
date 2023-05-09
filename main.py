import personbil
import lastbil


looping =True

#initiera objekt av classer 
opel_gron=personbil.personbil("opel", "gron", 420)
bmw_vit=personbil.personbil("bmw", "vit", 69)

Scania_Rosa = lastbil.lastbil("Scania", "Rosa", 4200)
Volvo_Rost = lastbil.lastbil("Volvo", "Rost", 0.5)

personbils_lista =[opel_gron, bmw_vit]
lastbils_lista = [Scania_Rosa, Volvo_Rost]

def print_fordonslista(fordonslista):
    for ettfordon in fordonslista:
        ettfordon.print_fordon()

while looping:

    print("-----------------------------------")
    print("\nklasser och arv av fordon \n ")


    val_fordon = input("vilken fordonstyp vill du lista? 1=lastbil 2=personbil: ")

    if(val_fordon== "1"):
        print("\n-lastbilar-")
        print("\-------------------------")
        print_fordonslista(lastbils_lista)
   
    elif (val_fordon == "2"):
        print("\n-personbilar-")
        print("-------------------------")
        print_fordonslista(personbils_lista)
        
    else:
        print("\nogiltig inmatning! \n")
   
   
   
    go =input("\n vill ni lista fordonen igen? j/n")

    if (go == "n"):
        break