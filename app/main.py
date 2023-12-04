from fastapi import FastAPI, status, HTTPException
from fastapi.responses import FileResponse

from app.models import database, Operation, Calc, CalcResult
from app.calculator import compute
import csv
import datetime


app = FastAPI(title="EasyRPN")

@app.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    return {"message": "Welcome to the EasyRPN API. Try route /docs for more infos"}

@app.get("/api/healthchecker", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "The API is LIVE!!"}

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


@app.get('/results', status_code=status.HTTP_200_OK, response_class=FileResponse)
async def download_results_in_csv_file():
    operations_list = await Operation.objects.all()

    date_time = datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")
    file_name = f'{date_time}_results.csv'
    file_path = f'/tmp/{file_name}'
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',')
        csvwriter.writerow(["ID", "Operation", "Result", "Timestamp"])
        for op in operations_list:
            csvwriter.writerow([op.id, op.expression, op.result, op.timestamp])

    response = FileResponse(file_path, media_type="text/csv")
    response.headers["Content-Disposition"] = f"attachement; filename={file_name}"
    return response

@app.post("/calculate", status_code=status.HTTP_201_CREATED)
async def calculate_operation(operation: Calc) -> CalcResult:
    result: float
    expression: str
    #Resolve operation
    try:
        result = compute(operation.operation_list)
    except(Exception) as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
    #Save in DB if successful
    expression = " ".join(str(i) for i in operation.operation_list)
    await Operation.objects.create(expression=expression, result=result)

    new_result = CalcResult()
    new_result.operation = expression
    new_result.result = result
    return new_result