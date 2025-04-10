import os
import time
print("        Debug Mode activator")
print("Lancé depuis:", os.getcwd())

path = os.path.join(os.getcwd(), "data.win")

print("Fichier data.win :", path)
ligne = 0x00725D8C

with open(path, "rb+") as data:
    data.seek(ligne)
    debug_bit = data.read(1)
    data.seek(ligne)
   
    if debug_bit == b'\x01':
        print("🟢 Debug Mode Activé")
        choixOn = input("Voulez vous désactiver le Debug Mode ? (y/n)")
        if choixOn == "y":
            print("Modification du jeux en cours...")
            data.write(b'\x00')
            time.sleep(1)
            print("Verification du changement")
            data.seek(ligne)
            debug_bit = data.read(1)
            if debug_bit == b'\x00':
                print("🔴 Le jeux a bien été modifié")
            else:
                print("Le jeu n'a pas été modifié, nous avons malheureusement modifié une valeur du jeu")
        else:
            print("Anulation de la désactivation")
   
    elif debug_bit == b'\x00':
        print("🔴 Debug Mode Désactivé")
        choixOff = input("Voulez vous activer le Debug Mode ? (y/n)")
        if choixOff == "y":
            print("Modification du jeux en cours...")
            data.write(b'\x01')
            time.sleep(1)
            print("Verification du changement")
            data.seek(ligne)
            debug_bit = data.read(1)
            if debug_bit == b'\x01':
                print("🟢 Le jeux a bien été modifié")
            else:
                print("Le jeu n'a pas été modifié, nous avons malheureusement modifié une valeur du jeu")
        else:
            print("Anulation de l'actiavtion")
    else:
        print("T'est sur d'etre en 1.001 ??")

    
os.system('pause')






