from pydantic import BaseModel,EmailStr,computed_field
from typing import List, Dict

class Patient(BaseModel):
    
    name : str
    email : EmailStr
    age : int
    weight : float  #kg
    married : bool  
    height : float #mtr
    allergies : List[str]
    contact_details : Dict[str,str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    
    
    
def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print("BMI",patient.bmi)
    print('updated')
    
patient_info = {'name': 'ajit','email':'ajit@hdfc.com','linkedin_url':"https://linkedin.com",'age':'70','weight':90.2,'height':'1.72','married':False,'allergies':['pollen','dust'],'contact_details': {'email':'abc@hdfc.com','phone':'9292929292','emergency':'2211221122'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)