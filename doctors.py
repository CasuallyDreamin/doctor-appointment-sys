from data_objects.doctor import doctor
from data_structures.sll import sll
from data_structures.hashtable import hashtable as ht

class doctors:
    def __init__(self):
        self.count = 0
        self.doctors = ht()

    def add_doctor(self, doct: doctor) -> bool:
        self.doctors.insert(doct.national_id, doct)

    def get_all(self) -> sll:
        return self.doctors.get_all()

    def get_by_national_id(national_id: int) -> doctor:
        ...

    def get_all_by_speciality(speciality: str) -> sll:
        ...
    