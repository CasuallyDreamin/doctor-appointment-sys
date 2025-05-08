from data_objects.doctor import doctor
from data_structures.sll import sll
from data_structures.hashtable import hashtable as ht
from data_structures.parent_child_ll import parent_child_ll

class doctors:
    def __init__(self):
        self.count = 0
        self.doctors = ht()
        self.specialty_order = parent_child_ll()
        self.city_order = parent_child_ll()

    def add_doctor(self, doct: doctor) -> bool:
        if not self.doctors.insert(doct.national_id, doct):
            return False
        self.specialty_order.add_child(doct.specialty, doct)
        self.city_order.add_child(doct.city, doct)
        return True

    def add_specialty(self, specialty):
        self.specialty_order.add_parent(specialty)

    def add_city(self, city):
        self.city_order.add_parent(city)
        
    def get_all(self) -> sll:
        return self.doctors.get_all()

    def get_by_national_id(self, national_id: int) -> doctor:
        return self.doctors.get(national_id)

    def get_all_by_specialty(self, specialty: str) -> sll:
        return self.specialty_order.get_children(specialty)
    
    def get_all_cities(self):
        return self.city_order.get_parents()
    
    def get_all_specialties(self):
        return self.specialty_order.get_parents()
    