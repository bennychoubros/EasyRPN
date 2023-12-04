from fastapi import FastAPI, status

from app.models import database, Operation, Calc, CalcResult
from app.calculator import compute


app = FastAPI(title="EasyRPN")

@app.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    #return await Operation.objects.all()
    return {"message": "Welcome to the EasyRPN API. Try route /docs for more infos"}

@app.get("/api/healthchecker", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "The API is LIVE!!"}

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a first test entry
    await Operation.objects.get_or_create(expression="1 2 +", result=3.0)

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


#get : récupérer l'historique des opérations et résultats
@app.get('/results', status_code=status.HTTP_200_OK)
async def get_results():
    return await Operation.objects.all()

#post : calculer resultats
@app.post("/calculate", status_code=status.HTTP_201_CREATED)
async def calculate_result(operation: Calc) -> CalcResult:
    result: float
    expression: str
    #Resolve operation
    result = compute(operation.operation_list)
    #Save in DB if successful
    expression = " ".join(str(i) for i in operation.operation_list)
    await Operation.objects.create(expression=expression, result=result)

    new_result = CalcResult()
    new_result.operation = expression
    new_result.result = result
    return new_result