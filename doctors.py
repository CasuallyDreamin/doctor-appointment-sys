from data_objects.doctor import doctor
from data_structures.sll import sll
from data_structures.hashtable import hashtable as ht
from data_structures.parent_child_ll import parent_child_ll

class doctors:
    def __init__(self):
        self.count = 0
        self.doctors = ht()
        self.speciality_order = parent_child_ll()
        self.city_order = parent_child_ll()

    def add_doctor(self, doct: doctor) -> bool:
        self.doctors.insert(doct.national_id, doct)
        self.speciality_order.add_child(doct.speciality, doct)
        self.city_order.add_child(doct.city, doct)

    def add_speciality(self, speciality):
        self.speciality_order.add_parent(speciality)

    def add_city(self, city):
        self.city_order.add_parent(city)
        
    def get_all(self) -> sll:
        return self.doctors.get_all()

    def get_by_national_id(self, national_id: int) -> doctor:
        return self.doctors.get(national_id)

    def get_all_by_speciality(self, speciality: str) -> sll:
        return self.speciality_order.get_children(speciality)
    