import sys
import os

# Add the 'scripts' directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from scripts.nmap_script import run_nmap
from scripts.nikto_script import run_nikto
from scripts.nessus_script import run_nessus
from scripts.dirb_script import run_dirb
from scripts.dnsenum_script import run_dnsenum
from scripts.openvas_script import run_openvas

def main():
    print("Select the tool you want to use:")
    print("1. Nmap")
    print("2. Nikto")
    print("3. Nessus")
    print("4. Dirb")
    print("5. Dnsenum")
    print("6. OpenVAS")

    choice = input("Enter the number corresponding to your choice: ")
    ip = input("Enter the target IP address: ")

    if choice == '1':
        run_nmap(ip)
    elif choice == '2':
        run_nikto(ip)
    elif choice == '3':
        run_nessus(ip)
    elif choice == '4':
        run_dirb(ip)
    elif choice == '5':
        run_dnsenum(ip)
    elif choice == '6':
        run_openvas(ip)
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
