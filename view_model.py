from doctors import doctors
from data_objects.doctor import doctor

class view_model:
    def __init__(self):
        self.doctors = doctors()

    def add_doctor(self, new_doctor: doctor):
        self.doctors.add_doctor(new_doctor)
    
    def get_all_doctors(self):
        return self.doctors.get_all()
