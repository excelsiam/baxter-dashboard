from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/")
def add(request):
    return {"result": 'home request'}


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
