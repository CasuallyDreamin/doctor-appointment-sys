from clear_screen import clear
from sys import exit
from data_objects.doctor import doctor
from view_model import view_model

vm = view_model()

with open("data_files/Cities.txt","r") as f:
    cities = [line.strip() for line in f.readlines()]
    for city in cities:
        vm.add_city(city)

with open("data_files/Specialties.txt", "r") as f:
    specis = [line.strip() for line in f.readlines()]
    for speci in specis:
        vm.add_specialty(speci)

with open("data_files/Doctors.txt","r") as f:
    for line in f:
        doc = line.strip().split("-")
        new_doctor = doctor(
        name         = doc[0],
        family_name  = doc[1],
        national_id  = int(doc[2]),
        med_id       = int(doc[3]),
        phone_number = int(doc[4]),
        address      = doc[5],
        city         = doc[6],
        specialty    = doc[7],
        password     = doc[8])
    
        if not vm.add_doctor(new_doctor):
            exit("couldn't add a doctor")   


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
        
        while True:
            national_id = input("national id: ")
            try:
                national_id = int(national_id)
                break
            except ValueError:
                print("Invalid national id.")
        
        while True:
            med_id = input("med id: ")
            try:
                med_id = int(med_id)
                break
            except ValueError:
                print("Invalid med id.")
        
        while True:
            phone_number = input("phone number: ")
            try:
                phone_number = int(phone_number)
                break
            except ValueError:
                print("Invalid phone number.")
    
        address = input("address: ")
        
        invalid_city = True
        
        while invalid_city:
            doc_city = input("city: ")
            if doc_city == '0':
                return
            
            curr_city = vm.get_all_cities().head
            while curr_city != None:
                if curr_city.data == doc_city:
                    invalid_city = False
                    break
                curr_city = curr_city.next
            
            if not invalid_city:
                break

            print(f"{doc_city} is not a supported city\nSupported Cities:")
            curr_city = vm.get_all_cities().head
            while curr_city != None:
                print(curr_city.data)
                curr_city = curr_city.next

        invalid_speci = True
        while invalid_speci:
            doc_specialty = input("specialty: ")
            if doc_specialty == '0':
                return
            
            curr_speci = vm.get_all_speci().head
            while curr_speci != None:
                if curr_speci.data == doc_specialty:
                    invalid_speci = False
                    break
                curr_speci = curr_speci.next
            
            if not invalid_speci:
                break

            print(f"{doc_specialty} is not a supported specialty\nSupported Specialties:")
            curr_speci = vm.get_all_speci().head
            while curr_speci != None:
                print(curr_speci.data)
                curr_speci = curr_speci.next
        
        password = input("password")

        new_doctor = doctor(
            name         = name,
            family_name  = family_name,
            national_id  = national_id,
            med_id       = med_id,
            phone_number = phone_number,
            address      = address,
            city         = doc_city,
            specialty   = doc_specialty,
            password     = password)
    
        vm.add_doctor(new_doctor)

def admin_panel():
    clear()
    print(
'''
1. See all doctors
2. Find doctor by national ID
3. Filter by Speciality
'''
    )
    valid_options = [1, 2, 3]
    opt = get_option(valid_options)
    
    # See all doctors
    # {Get all doctors from DS} -> {Show}
    if opt == 1:
        curr_doc_node = vm.get_all_doctors().head
        
        print("name, family name, national ID , med ID, phone number, address, city, specialty, password")

        while curr_doc_node != None:
            curr_doc:doctor = curr_doc_node.data

            print(curr_doc.name, ",",
                  curr_doc.family_name, ",",
                  curr_doc.national_id, ",",
                  curr_doc.med_id, ",",
                  curr_doc.phone_number, ",",
                  curr_doc.address, ",",
                  curr_doc.city, ",",
                  curr_doc.specialty, ",",
                  curr_doc.password)
            
            curr_doc_node = curr_doc_node.next

        return input("Enter to return. ")
    
    # Find doctor by national ID
    # {Get national ID} -> {Get Doctor from DS} -> {Show}
    elif opt == 2:
        while True:
            try:
                national_id = int(input("national id: "))
                if national_id == 0:
                    return
                break
            except ValueError:
                print("Invalid national ID")
        
        doct = vm.get_by_national_id(national_id)
        
        if doct == None:
            input("Doctor not found. \nEnter to return. ")
        else:
            print("name: ", doct.name, "\n",
                  "family name: ", doct.family_name, "\n",
                  "national ID : ", doct.national_id, "\n",
                  "med ID: ", doct.med_id, "\n",
                  "phone number: ", doct.phone_number, "\n",
                  "address: ", doct.address, "\n",
                  "city: ", doct.city, "\n",
                  "specialty: ", doct.specialty, "\n")
            input("Enter to return.")
        return

    # Find all doctors by specialty
    # {Get specialty} -> {Get Doctors from DS} -> {Show}
    elif opt == 3:
        specialty = input("national id: ")
        docts = vm.get_by_specialty(specialty)
        curr_doc_node = docts.head
        if curr_doc_node == None:
            input("no doctors found. \nEnter to return. ")
        else:
            while curr_doc_node != None:
                curr_doc:doctor = curr_doc_node.data

                print(curr_doc.name, ",",
                    curr_doc.family_name, ",",
                    curr_doc.national_id, ",",
                    curr_doc.med_id, ",",
                    curr_doc.phone_number, ",",
                    curr_doc.address, ",",
                    curr_doc.city, ",",
                    curr_doc.specialty, ",",
                    curr_doc.password)
                
                curr_doc_node = curr_doc_node.next
            
            input("Enter to return.")
        return
    # TODO: Add city support
    # {Get City} -> {Add to DS}

    # TODO: Add speciality support  
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