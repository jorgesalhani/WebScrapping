import os
import re
class FirefoxProfile:
    def __init__(self) -> None:
        self.username = os.getlogin()

    def get_profile_default_path(self) -> str:
        full_path = 'C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'.format(self.username)
        if not self.__check_file_exits(full_path): return ''

        entries = os.listdir(full_path)
        for entry in entries:
            if re.search('default', entry):
                return ''.join([full_path, f'\\{entry}'])
        return ''

    def __check_file_exits(self, path: str) -> bool:
        return os.path.exists(path)
