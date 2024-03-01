import warnings

from fastapi import FastAPI, Query

from .dates import transform_date, get_dates_from_file
from .config import title
# from .testdates import dates

app = FastAPI(title=title)

# Desactiva la advertencia específica
warnings.filterwarnings("ignore", category=UserWarning, module="tzlocal")

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


@app.get("/test-dates", tags=['dates'])
def test_dates():
    dates = get_dates_from_file()
    # dates = [
    #     "Día 16 Mes 07",
    #     "21 / 07 / 2022"
    # ]
    responseOK = responseKO = []
    for d in dates:
        final_date = transform_date(d)
        if final_date['formato_identificado'] is None :
            responseKO.append(final_date)
        else:
            responseOK.append(final_date)
    return {
        "ko": {
            "total": len(responseKO),
            "data": responseKO
        },
        "ok": {
            "total": len(responseOK),
            "data": responseOK
        }
    }