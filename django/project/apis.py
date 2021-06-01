from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from typing import List
from db.models import *
from .schemas import *

api = NinjaAPI()

# ====================================================================================


@api.get("/basics", response=List[BasicInformationOut])
def list_basics(request):
    return BasicInformation.objects.all()


@api.get("/basics/{id}", response=BasicInformationOut)
def get_basic(request, id: int):
    instance = get_object_or_404(BasicInformation, id=id)
    return instance


@api.post("/basics")
def create_basic(request, payload: BasicInformationIn):
    info = BasicInformation.objects.create(**payload.dict())
    return {"id": info.id}


@api.post("/basics_update/{id}")
def update_basic(request, id: int, payload: BasicInformationIn):
    instance = get_object_or_404(BasicInformation, id=id)
    for attr, value in payload.dict().items():
        setattr(instance, attr, value)
    instance.save()
    return {"success": True}


@api.post("/basics_delete/{id}")
def delete_basic(request, id: int):
    instance = get_object_or_404(BasicInformation, id=id)
    instance.delete()
    return {"success": True}

# ====================================================================================


@api.get("/")
def add(request):
    return {"result": 'home request'}
