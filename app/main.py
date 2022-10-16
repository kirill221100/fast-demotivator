from fastapi import FastAPI
from uvicorn import run
from app.routes.dem import router

app = FastAPI(title='DemotivatorAPI', docs_url="/docs", redoc_url=None)

app.include_router(router)

if __name__ == '__main__':
    run('main:app', reload=True)
