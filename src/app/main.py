from typing import Union

from fastapi import FastAPI, Query

from dates import transform_date
from config import title

app = FastAPI(title=title)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/dates", tags=['dates'])
def format_date(date: str, dateFormat: str = '%Y-%m-%d'):
    """
    Endpoint para convertir fechas utilizando un formato especificado.

    dates format codes
    https://docs.python.org/es/3/library/datetime.html#format-codes
    """
    final_date = transform_date(date, dateFormat)
    return {"code": "200", "dateFormatted": final_date, "dateFormat": dateFormat}
