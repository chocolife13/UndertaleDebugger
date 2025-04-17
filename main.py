import win32api
import time
import os



os.system('cls')





logfile = open(os.path.join("Backup","logs","log.txt"), "w", encoding="utf-8")

def log(text):
    print(text)
    logfile.write(text + "\n")







path = os.path.join(os.getcwd())
offset =  0x00725D8C
data_missing = not os.path.exists(r'data.win')
UNDERTALE_missing = not os.path.exists(r'UNDERTALE.exe')








log("""===============================
   UNDERTALE DEBUG TOOL v0.3
===============================""")



log("""Initialization
    """)


if UNDERTALE_missing:
    log("❌ UNDERTALE.exe is missing !")
    log("🤣 Are you sure you put this .exe in your undertale folder ??????")
    os.system('pause')
else:
    log("- ✅ Undertale.exe found")
    exe_info = win32api.GetFileVersionInfo(path + r"\UNDERTALE.exe", "\\")
    version = f"{exe_info['FileVersionMS'] >> 16}.{exe_info['FileVersionMS'] & 0xFFFF}.{exe_info['FileVersionLS'] >> 16}.{exe_info['FileVersionLS'] & 0xFFFF}"


if data_missing:
    log("❌ data.win is missing !")
    log("🤣 Are you sure you put this .exe in your undertale folder ??????")
    os.system('pause')
else:
    log("- ✅ data.win found")

log("===============================")











log("""Backup
    """)

if os.path.exists(r'Backup\\Data'):
    log("- ✅ Backup folder found")
else:
    log("- ❌ Backup missing!")
    log('- ⏳ Creation the folder Backup')
    os.system('mkdir Backup\\data')
    os.system('attrib +h Backup')
    log("- ⏳ Verification")


    time.sleep(1)

    if os.path.exists(r'Backup\\Data'):
        log("- ✅ Backup was created")
    else:
        log("❌ Error !")
        os.system('pause')








if os.path.exists(r'Backup\\Data\\data.win'):
    log("- ✅ Backup data.win found")
else:
    log("- ⚠️  Backup data.win missing!")
    log('- ⏳ Creation the data.win Backup')
    os.system(f"copy {os.path.join(path, "data.win")} {os.path.join(path, "Backup", "data")} >nul")
    log("- ⏳ Verification")




    time.sleep(1)





    if os.path.exists(r'Backup\\Data\\data.win'):
        log("- ✅ Backup data.win was created")
    else:
        log("❌ Error !")
        os.system('pause')





log("===============================")

log("""Information
    """)

log("- 📁 Undertale from : " + path)


if version == "0.9.9.5":
    offset = 0x00725D8C
    log("- ✅ UNDERTALE.exe v1.001")




log("===============================")

log("""DebugMode
    """)







with open(path + r"\data.win", "rb+") as data:
    
    
    data.seek(offset)
    debug_bit = data.read(1)
    data.seek(offset)
    
    
    
    if debug_bit == b'\x00':
    
        log("- 🔴 Debug Mode is Off")
        choixOff = input("Do you want to enable the DebugMode ? (y/n)")
    else:
        log("- 🟢 Debug Mode is On")
        choixOff = input("- ❓ Do you want to disable the DebugMode ? (y/n)")
        
    
    
    
    if choixOff == "y":
        log("- ⏳ Applying changes to the game")
        
        
        if debug_bit == b'\x01':
            data.write(b'\x00')
        else:
            data.write(b'\x01')
    
        
        
        log("- ⏳ Verification")
        time.sleep(1)
        
       
       
        
        
        
        data.seek(offset)
        
        debug_bit_modified = data.read(1)
        if not debug_bit == debug_bit_modified:
            
            log("- ✅ The game has been successfully modified.")
            
        else:
            
            log("- ❌ Ur game is Dead 💀")
    
    
    
    
    else:
        log("- 👋 Exiting from the user")
        
        
        
        
        
        
        
       
   

    
os.system('pause')




logfile.close()








