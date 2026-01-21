
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    
    name : Annotated[str,Field(max_length=50,title = "name of the Patient",description=" Give the name of the patient in less than 50 characters", examples = ['Ajit','Akhilesh'])]
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt=0,ls=120)
    weight : Annotated[float,Field(gt=0,strict = True)]
    married : Annotated[bool,Field(default = None, description = "Is the patient marrid or not")]
    allergies : Annotated[Optional[List[str]] , Field(default=None,max_length=5)]
    contact_details : Dict[str, str]
    
def update_patient_data(patient : Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print('Updated')   

patient_info = {'name': 'ajit','email':'ajit@gmail.com','linkedin_url':"https://linkedin.com",'age':'30','weight':90.2,'married':False,'allergies':['pollen','dust'],'contact_details': {'email':'abc@gmail.com','phone':'9292929292'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)