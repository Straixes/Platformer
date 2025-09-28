import os
import json

def saveSettings(settings):
    appdata = os.getenv("APPDATA")  
    
    game_folder = os.path.join(appdata, ".Platformer")
    os.makedirs(game_folder, exist_ok=True) 


    settingsFile = os.path.join(game_folder, "settings.json")

    with open(settingsFile, "w") as f:
        json.dump(settings, f, indent=4)


def loadSettings():
    appdata = os.getenv("APPDATA")  
    game_folder = os.path.join(appdata, ".Platformer")
    os.makedirs(game_folder, exist_ok=True) 
    settingsFile = os.path.join(game_folder, "settings.json")

    if os.path.exists(settingsFile):
        with open(settingsFile, "r") as f:
            settings = json.load(f)
    else:
        # valeurs par défaut si fichier absent
        settings = {"volume": 1.0, "resolution": [800, 600], "fullscreen": False}

        # 🔹 On écrit immédiatement le fichier
        with open(settingsFile, "w") as f:
            json.dump(settings, f, indent=4)

    return settings
