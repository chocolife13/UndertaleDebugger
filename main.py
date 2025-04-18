import win32api
import datetime
import time
import os


os.system('cls')

os.makedirs("Backup/logs", exist_ok=True)
if not os.path.exists(r'Backup\\logs\\log.txt'):
    log_file = open(os.path.join("Backup","logs","log.txt"), "w", encoding="utf-8")
    log_file.write(f"log.txt was created: {datetime.datetime.now()}\n ")
    log_file.close()  


def log(text):
    
    log_file = open(os.path.join("Backup","logs","log.txt"), "a+", encoding="utf-8")
    log_file.write(f"{text}\n")
    log_file.close()
    print(text)
    




def exit():
    os.system('pause')
    os._exit(0)





path = os.path.join(os.getcwd())
offset =  0x00725D8C
data_missing = not os.path.exists(r'data.win')
UNDERTALE_missing = not os.path.exists(r'UNDERTALE.exe')






log_file = open(os.path.join("Backup","logs","log.txt"), "a+", encoding="utf-8")
log_file.write(f"###############################################################################################\n")
log_file.close()



log("""===============================
   UNDERTALE DEBUG TOOL v0.3""")
log_file = open(os.path.join("Backup","logs","log.txt"), "a+", encoding="utf-8")
log_file.write(f"   {datetime.datetime.now()}\n")
log_file.close()
log("""===============================""")



log("""Initialization
    """)


if UNDERTALE_missing:
    log("❌ UNDERTALE.exe is missing !")
    log("🤣 Are you sure you put this .exe in your undertale folder ??????")
    exit()
else:
    log("- ✅ Undertale.exe found")
    exe_info = win32api.GetFileVersionInfo(path + r"\UNDERTALE.exe", "\\")
    version = f"{exe_info['FileVersionMS'] >> 16}.{exe_info['FileVersionMS'] & 0xFFFF}.{exe_info['FileVersionLS'] >> 16}.{exe_info['FileVersionLS'] & 0xFFFF}"


if data_missing:
    log("❌ data.win is missing !")
    log("🤣 Are you sure you put this .exe in your undertale folder ??????")
    exit()
else:
    log("- ✅ data.win found")

log("===============================")

log("""Backup
    """)

if os.path.exists(r'Backup\\data'):
    log("- ✅ Backup folder found")
else:
    log("- ❌ Backup missing!")
    log('- ⏳ Creation the folder Backup')
    os.system('mkdir Backup\\data')
    os.system('attrib +h Backup')
    log("- ⏳ Verification")


    time.sleep(1)

    if os.path.exists(r'Backup\\data'):
        log("- ✅ Backup was created")
    else:
        log("❌ Error !")
        exit()








if os.path.exists(r'Backup\\data\\data.win'):
    log("- ✅ Backup data.win found")
else:
    log("- ⚠️  Backup data.win missing!")
    log('- ⏳ Creation the data.win Backup')
    os.system(f"copy \"{os.path.join(path, 'data.win')}\" \"{os.path.join(path, 'Backup', 'data', 'data.win')}\" >nul")
    log("- ⏳ Verification")




    time.sleep(1)





    if os.path.exists(r'Backup\\data\\data.win'):
        log("- ✅ Backup data.win was created")
    else:
        log("❌ Error !")
        exit()

log("===============================")





















log("""Information
    """)

log("- 📁 Undertale from : " + path)


if version == "0.9.9.5":
    offset = 0x00725D8C
    log("- ✅ UNDERTALE.exe <= v1.001")
else:
    log("❌ Your Undertale is not in 1.001")
    exit()


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
    
    elif debug_bit == b'\x01':
        
        log("- 🟢 Debug Mode is On")
        choixOff = input("- ❓ Do you want to disable the DebugMode ? (y/n)")
        
    else:
        log("- ❌ Error version")
    
    
    if choixOff.lower() == "y":
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
        
        
        
        
        
        
        
       
   

    
exit()













