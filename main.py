from adb import Adb


def main():
    adb = Adb()
    if not adb.check_device_connected():
        print("No device connected. Please connect an Android device and try again.")
        return

    while True:
        print("\nMenu:")
        print("1. List installed apps")
        print("2. Uninstall system app")
        print("3. Install APK")
        print("4. Force stop app")
        print("5. Force start app")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            adb.list_installed_apps()
        elif choice == '2':
            package_name = input("Enter the package name of the system app to uninstall: ")
            adb.delet_system_app(package_name)
        elif choice == '3':
            apk_path = input("Enter the path to the APK file: ")
            adb.instalar_apk(apk_path)
        elif choice == '4':
            package_name = input("Enter the package name of the app to force stop: ")
            adb.kill_proccess(package_name)
        elif choice == '5':
            package_name = input("Enter the package name of the app to force start: ")
            adb.force_start_app(package_name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
main()