import os
import re 

class FirefoxProfile:
    def __init__(self) -> None:
        self.username = os.getlogin()

    def get_profile_code_default(self) -> str:
        full_path = 'C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'.format(self.username)
        entries = os.listdir(full_path)
        for entry in entries:
            if "default-release" in entry: return entry.split('.')[0]
            if "default" in entry: return entry.split('.')[0]
        return ''