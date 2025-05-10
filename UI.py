from clear_screen import clear
from sys import exit
from data_objects.doctor import doctor
from data_objects.patient import patient as pat
from view_model import view_model


def UI():
    running = True
    init()
    while running:
        running = main_menu()
    
    clear()
    exit()

def main_menu():
    clear()
    if vm.curr_user != None:
        print(f"User:{vm.curr_user.name} {vm.curr_user.family_name}")
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
    elif opt == 0: 
        #Update data files before exit
        with open("data_files/Cities.txt","w") as f:
            cities = vm.get_all_cities()
            curr_city = cities.head
            
            while curr_city != None:
                f.write(f"{curr_city.data}\n")
                curr_city = curr_city.next

        with open("data_files/Specialties.txt", "w") as f:
            specialties = vm.get_all_speci()
            curr_speci = specialties.head

            while curr_speci != None:
                f.write(f"{curr_speci.data}\n")
                curr_speci = curr_speci.next

        with open("data_files/Doctors.txt","w") as f:
            doctors = vm.get_all_doctors()
            curr_doctor = doctors.head

            while curr_doctor != None:
                curr_data:doctor = curr_doctor.data
                
                curr_doctor_info_write_formated = curr_data.name + "-" + curr_data.family_name + "-" + str(curr_data.national_id) + "-" + str(curr_data.med_id) + "-" + str(curr_data.phone_number) + "-" + curr_data.address + "-" + curr_data.city + "-" + curr_data.specialty + "-" + curr_data.password

                f.write(f"{curr_doctor_info_write_formated}\n")
                curr_doctor = curr_doctor.next

        return False
    return True

def doctor_panel():
    clear()
    
    if vm.curr_user != None:
        print(f"User:{vm.curr_user.name} {vm.curr_user.family_name}")
    print(
'''
Doctors Panel

1. register doctor
2. login
0. return
'''
    )
    valid_options = [1, 2, 0]
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
            doc_city = input("\ncity: ")
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
                print(curr_city.data, end=",")
                curr_city = curr_city.next

        invalid_speci = True
        while invalid_speci:
            doc_specialty = input("\nspecialty: ")
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
                print(curr_speci.data, end=",")
                curr_speci = curr_speci.next
        
        password = input("password: ")

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
    
        if vm.add_doctor(new_doctor):
            return input("Success.\nEnter to return")
        else:
            return input("national id already exists.")
    # login
    elif opt == 2:
        try:
            phone_number = int(input("Phone number: "))
        except ValueError: return input("invalid phone number")

        doct = vm.get_doctor_by_phone_number(phone_number)
        
        if doct == None:
            return input("Phone number was not found in the system.")
        
        password = input("Password: ")
        
        if password == doct.password:
            vm.curr_user = doct
            return input("Logged in\nEnter to return")
        
        else: return input("Wrong password")

    elif opt == 0: return
        
def admin_panel():
    clear()
    print(
'''
Admins Panel

1. See all doctors
2. Find doctor by national ID
3. Filter by Speciality
4. Add supported City
5. Add supported Speciality
0. return
'''
    )
    valid_options = [1, 2, 3, 4, 5, 0]
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
        
        doct = vm.get_doctor_by_national_id(national_id)
        
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
        specialty = input("Specialty: ")
        docts = vm.get_doctor_by_specialty(specialty)
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
    
    # Add city support
    # {Get City} -> {Add to DS}
    elif opt == 4:
        new_city = input("New City: ")
        
        #check if city already exists
        curr_city = vm.get_all_cities().head

        while curr_city != None:
            if curr_city.data == new_city:
                return input("City is already supported.")
            curr_city = curr_city.next

        vm.add_city(new_city)
        return
    
    # Add speciality support  
    # {Get speciality} -> {Add to DS}
    elif opt == 5:
        new_specialty = input("New specialty: ")
        
        #check if city already exists
        curr_specialty = vm.get_all_speci().head

        while curr_specialty != None:
            if curr_specialty.data == new_specialty:
                return input("specialty is already supported.\nEnter to return")
            curr_specialty = curr_specialty.next

        vm.add_specialty(new_specialty)
        return
    
    elif opt == 0: return
    
def patient_panel():
    clear()
    if vm.curr_user != None:
        print(f"User:{vm.curr_user.name} {vm.curr_user.family_name}")
    print(
'''
Patients Panel

1. register patient
2. login
3. Filter by Speciality
4. Add supported City
5. Add supported Speciality
0. return
'''
    )
    valid_options = [1, 2, 3, 4, 5, 0]
    
    opt = get_option(valid_options)
    
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
            phone_number = input("phone number: ")
            try:
                phone_number = int(phone_number)
                break
            except ValueError:
                print("Invalid phone number.")
        
        password = input("password: ")

        while True:
            sex = input("sex (Male/Female): ")
            if sex == "Male" or sex == "Female":
                break
            else:
                print("Invalid sex (case sensitive)")

        invalid_city = True
        
        while invalid_city:
            patient_city = input("\ncity: ")
            if patient_city == '0':
                return
            
            curr_city = vm.get_all_cities().head
            while curr_city != None:
                if curr_city.data == patient_city:
                    invalid_city = False
                    break
                curr_city = curr_city.next
            
            if not invalid_city:
                break

            print(f"{patient_city} is not a supported city\nSupported Cities:")
            curr_city = vm.get_all_cities().head
            while curr_city != None:
                print(curr_city.data, end=",")
                curr_city = curr_city.next
        
        while True:
            insurance_number = input("insurance number: ")
            try:
                insurance_number = int(insurance_number)
                break
            except ValueError:
                print("Invalid insurance number.")
         

        new_patient = pat(
            name         = name,
            family_name  = family_name,
            national_id  = national_id,
            phone_number = phone_number,
            password     = password,
            sex          = sex,
            city         = patient_city)
    
        if vm.add_patient(new_patient):
            return input("Success.\nEnter to return")
        else:
            return input("National id already exists.\nEnter to return")
        
    # login
    elif opt == 2:
        phone_number = input("Phone number: ")
        patient = vm.get_patient_by_phone_number(phone_number)
        
        if patient == None:
            return input("Phone number was not found in the system.")
        
        password = input("Password: ")
        
        if password == patient.password:
            vm.curr_user = patient
            return input("Logged in\nEnter to return")
        
        else: return input("Wrong password.")    
    
    elif opt == 0: return
    
def get_option(valid_options: list):
    while True:
        try: 
            opt = int(input("option: "))
            if opt in valid_options: break
        except: 
            print("Invalid option")
            input()
    return opt

def init():
    global vm 
    vm = view_model()
    
    with open("data_files/Cities.txt","r") as f:
        cities = [line.strip() for line in f.readlines()]
        for city in cities:
            vm.add_city(city)

    with open("data_files/Specialties.txt", "r") as f:
        specialties = [line.strip() for line in f.readlines()]
        for specialty in specialties:
            vm.add_specialty(specialty)

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

    with open("data_files/Patients.txt","r") as f:
        for line in f:
            patient = line.strip().split("-")
            new_patient = pat(
            name             = patient[0],
            family_name      = patient[1],
            national_id      = int(patient[2]),
            phone_number     = int(patient[3]),
            password         = patient[4],
            sex              = patient[5],
            city             = patient[6],
            insurance_number = patient[7])
        
            if not vm.add_patient(new_patient):
                exit("couldn't add a patient")   

if __name__ == "__main__":
    UI()