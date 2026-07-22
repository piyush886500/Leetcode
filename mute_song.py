from pycaw.pycaw import AudioUtilities

def mute_app(app_name, mute=True):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name().lower() == app_name.lower():
            volume = session.SimpleAudioVolume
            volume.SetMute(mute, None)
            print(f"{'Muted' if mute else 'Unmuted'} {app_name}")

mute_app("Spotify.exe", True)   # change to whatever you found abovefrom pycaw.pycaw import AudioUtilities

def mute_app(app_name, mute=True):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name().lower() == app_name.lower():
            volume = session.SimpleAudioVolume
            volume.SetMute(mute, None)
            print(f"{'Muted' if mute else 'Unmuted'} {app_name}")

mute_app("chrome.exe", True)   # change to whatever you found above