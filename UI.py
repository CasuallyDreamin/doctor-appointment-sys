from clear_screen import clear
from sys import exit
from data_objects.doctor import doctor
from view_model import view_model

vm = view_model()

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
    """)
    valid_options = [1,2,3,0]
    
    opt = get_option(valid_options)

    if opt == 1: doctor_panel()
    elif opt == 2: admin_panel()
    elif opt == 3: patient_panel()
    elif opt == 0: return False
    return True

def doctor_panel():
    clear()
    print(
'''
1. register doctor
'''
    )
    valid_options = [1]
    opt = get_option(valid_options)
    
    # register doctor
    # {Get doctor info from user} -> {Create doctor object} -> {Add to DS}
    if opt == 1:
        name         = input("name: ")
        family_name  = input("family name: ")
        national_id  = input("national id: ") 
        med_id       = input("med id: ")
        phone_number = input("phone number: ")
        address      = input("address: ")
        city         = input("city: ")
        speciality   = input("specialiy: ")
        
        new_doctor = doctor(
            name         = name,
            family_name  = family_name,
            national_id  = national_id,
            med_id       = med_id,
            phone_number = phone_number,
            address      = address,
            city         = city,
            speciality   = speciality)
    
        vm.add_doctor(new_doctor)

def admin_panel():
    clear()
    print(
'''
1. See all doctors
'''
    )
    valid_options = [1]
    opt = get_option(valid_options)
    
    # See all doctors
    # {Get all doctors from DS} -> {Show}
    if opt == 1:
        curr_doc_node = vm.get_all_doctors().head
        
        print("name, family name, national ID , med ID, phone number, address, city, speciality")
        
        while curr_doc_node != None:
            curr_doc:doctor = curr_doc_node.data

            print(curr_doc.name, ",",
                  curr_doc.family_name, ",",
                  curr_doc.national_id, ",",
                  curr_doc.med_id, ",",
                  curr_doc.phone_number, ",",
                  curr_doc.address, ",",
                  curr_doc.city, ",",
                  curr_doc.speciality)
            
            curr_doc_node = curr_doc_node.next

        input("Enter to return. ")
    
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

def get_option(valid_options: list):
    while True:
        try: 
            opt = int(input("option: "))
            if opt in valid_options: break
        except: 
            print("Invalid option")
            input()
    return opt
    
if __name__ == "__main__":
    main_menu()