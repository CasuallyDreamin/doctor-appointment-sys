from clear_screen import clear
from sys import exit

def UI():
    running = True

    while running:
        running = main_menu()
    
    clear()
    exit()

def main_menu():
    clear()
    print(
    """
1. doctor panel
2. admin panel
3. patient panel
0. exit
    """
    )
    valid_options = [1,2,3,0]
    
    while True:
        try: 
            opt = int(input("option: "))
            if opt in valid_options: break
        except: 
            print("Invalid option")
            input()
    
    if opt == 1: doctor_panel()
    elif opt == 2: admin_panel()
    elif opt == 3: patient_panel()
    elif opt == 0: return False
    return True

def doctor_panel():
    clear()
    print("This is the doctor panel")
    input("Enter to exit")
    # Todo:

    # register doctor 
    #   {Take data} -> {Add to DS}

def admin_panel():
    clear()
    print("This is the admin panel")
    input("Enter to exit")
    # Todo:
    
    # See all doctors 
    # {Get all doctors from DS} -> {Show}
    
    # Find doctor by national ID
    # {Get national ID} -> {Get Doctor from DS} -> {Show}

    # Find all doctors by speciality
    # {Get speciality} -> {Get Doctors from DS} -> {Show}

    # Add city support
    # {Get City} -> {Add to DS}

    # Add speciality support 
    # {Get speciality} -> {Add to DS}

def patient_panel():
    clear()
    print("This is the patient panel")
    input("Enter to exit")

if __name__ == "__main__":
    main_menu()