from db.models import *
from datetime import date
from ninja import Schema

# ====================================================================================


class BasicInformationIn(Schema):
    name: str = None
    code_id: str = None
    hospital: str = None
    gender: str = None
    birth_date: date = None
    education: str = None
    payment: str = None
    primary_kidney_disease: str = None
    dm_status: bool = None
    pd_initiation_date: date = None
    dropout_date: date = None
    dropout_category: str = None
    dropout_cause: str = None
    remarks: str = None


class BasicInformationOut(BasicInformationIn):
    id: int

# ====================================================================================


class PDInfectionSchema(Schema):
    name: str = None
    date: date = None
    type_of_infection: str = None
    causative_organism: str = None
    outcomes: str = None
    remarks: str = None

# ====================================================================================


class HospitalizationSchema(Schema):
    name: str = None
    admission_date: date = None
    reason: str = None
    remarks: str = None

# ====================================================================================
