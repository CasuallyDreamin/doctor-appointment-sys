class patient:
    def __init__(self,
                name: str,
                family_name: str,
                national_id: int,
                phone_number: int,
                password: str,
                sex: str,
                city: str,
                insurance_number: int):
        
        self.name: str             = name
        self.family_name: str      = family_name
        self.national_id: int      = national_id
        self.phone_number: int     = phone_number
        self.password: str         = password
        self.sex: str              = sex
        self.city: str             = city
        self.insurance_number: int = insurance_number
        