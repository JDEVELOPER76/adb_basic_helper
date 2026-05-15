import os 
import sys
import subprocess


class Adb:
    def __init__(self, adb_path=None):
        if adb_path is None:
            adb_path = self.find_adb()
        self.adb_path = adb_path
    

    def delet_system_app(self, package_name):
        command = f"{self.adb_path} shell pm uninstall -k --user 0 {package_name}"
        os.system(command)

    def list_installed_apps(self):
        command = f"{self.adb_path} shell pm list packages"
        os.system(command)
        return os.popen(command).read()

    def find_adb(self):
        if sys.platform.startswith('win'):
            adb_executable = 'adb.exe'
        else:
            raise FileNotFoundError("ADB executable not found in PATH.")
        return adb_executable

    
    def check_device_connected(self):
        command = f"{self.adb_path} devices"
        result = os.popen(command).read()
        if "device" in result:
            return True
        return False

    def instalar_apk(self, apk_path):
        command = f"{self.adb_path} install {apk_path}"
        os.system(command)

    def kill_proccess(self, package_name):
        command = f"{self.adb_path} shell am force-stop {package_name}"
        os.system(command)

    def force_start_app(self, package_name):
        command = f"{self.adb_path} shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1"
        os.system(command)



        
