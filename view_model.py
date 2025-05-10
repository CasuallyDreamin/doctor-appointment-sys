from doctors import doctors
from patients import patients
from data_objects.doctor import doctor
from data_objects.patient import patient

class view_model:
    def __init__(self):
        self.doctors = doctors()
        self.patients = patients()
    
    # Patient methods
    def add_patient(self, patient: patient) -> bool:
        return self.patients.add_patient(patient)
    
    def get_patient_by_national_id(self, national_id: int) -> patient:
        return self.patients.get_by_national_id(national_id)

    def get_doctor_by_phone_number(self, phone_number: int) -> patient:
        return self.patients.get_by_phone_number(phone_number)
    
    # Doctor methods
    def add_doctor(self, new_doctor: doctor) -> bool:
        return self.doctors.add_doctor(new_doctor)
    
    def get_all_doctors(self):
        return self.doctors.get_all()
    
    def get_doctor_by_national_id(self, national_id: int) -> doctor:
        return self.doctors.get_by_national_id(national_id)

    def get_doctor_by_phone_number(self, phone_number: int) -> doctor:
        return self.doctors.get_by_phone_number(phone_number)
    
    def get_doctor_by_specialty(self, specialty):
        return self.doctors.get_all_by_specialty(specialty)
    
    # Admin methods
    def add_city(self, city):
        self.doctors.add_city(city)

    def add_specialty(self, specialty):
        self.doctors.add_specialty(specialty)
    
    def get_all_cities(self):
        return self.doctors.get_all_cities()
    
    def get_all_speci(self):
        return self.doctors.get_all_specialties()