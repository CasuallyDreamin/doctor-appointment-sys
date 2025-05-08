from doctors import doctors
from data_objects.doctor import doctor

class view_model:
    def __init__(self):
        self.doctors = doctors()

    def add_doctor(self, new_doctor: doctor):
        self.doctors.add_doctor(new_doctor)
    
    def get_all_doctors(self):
        return self.doctors.get_all()
    
    def get_by_national_id(self, national_id: int):
        return self.doctors.get_by_national_id(national_id)

    def get_by_speciality(self, speciality):
        return self.doctors.get_all_by_speciality(speciality)
    
    def add_city(self, city):
        self.doctors.add_city(city)

    def add_speciality(self, speciality):
        self.doctors.add_speciality(speciality)
