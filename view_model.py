from doctors import doctors
from data_objects.doctor import doctor

class view_model:
    def __init__(self):
        self.doctors = doctors()

    def add_doctor(self, new_doctor: doctor):
        return self.doctors.add_doctor(new_doctor)
    
    def get_all_doctors(self):
        return self.doctors.get_all()
    
    def get_by_national_id(self, national_id: int):
        return self.doctors.get_by_national_id(national_id)

    def get_by_specialty(self, specialty):
        return self.doctors.get_all_by_specialty(specialty)
    
    def add_city(self, city):
        self.doctors.add_city(city)

    def add_specialty(self, specialty):
        self.doctors.add_specialty(specialty)
    
    def get_all_cities(self):
        return self.doctors.get_all_cities()
    
    def get_all_speci(self):
        return self.doctors.get_all_specialties()