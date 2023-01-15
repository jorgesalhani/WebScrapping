import os

class FirefoxProfile:
    def __init__(self) -> None:
        self.username = os.getlogin()
    
    def get_profile_code_default(self) -> str:
        full_path = 'C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'.format(self.username)
        entries = os.listdir(full_path)
        return entries
