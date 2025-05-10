from data_objects.patient import patient
from data_structures.sll import sll
from data_structures.hashtable import hashtable as ht

class patients:
    def __init__(self):
        self.count = 0
        self.patients = ht()
        self.patients_by_number = ht()
        
    def add_patient(self, patient: patient) -> bool:
        if not self.patients.insert(patient.national_id, patient):
            return False
        self.patients_by_number.insert(patient.phone_number, patient)
        return True
    
    def get_all(self) -> sll:
        return self.patients.get_all()

    def get_by_national_id(self, national_id: int) -> patient:
        return self.patients.get(national_id)
    
    def get_by_phone_number(self, phone_number: int) -> patient:
        return self.patients_by_number.get(phone_number)