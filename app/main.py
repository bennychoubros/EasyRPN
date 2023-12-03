from fastapi import FastAPI
from starlette.responses import JSONResponse


from app.models import database, Operation


app = FastAPI(title="EasyRPN")

@app.get("/")
async def read_root():
    return await Operation.objects.all()

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

# defining exceptional JSON-response for incorrect  queries
@app.exception_handler(Exception)
async def error_handler(request, exc):
    return JSONResponse({
        'detail': f'{exc}'
    })