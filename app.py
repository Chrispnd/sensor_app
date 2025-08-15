from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fake_data import create_app
from datetime import date

store_dict = create_app()
app = FastAPI()

@app.get("/")
def visit(store_name: str, year: int, month:int, day:int, sensor_id: int | None = None) -> JSONResponse:

    if not(store_name in store_dict.keys()):
        return JSONResponse(status_code=404, content={"message": "Store not found"})

    if sensor_id and (sensor_id > 7 or sensor_id < 0):
        return JSONResponse(status_code=404, content={"message": "Sensor ID out of range"})

    if year < 2019:
        return JSONResponse(status_code=404, content={"message": "No data before 2019"})

    try:
        requested_date = date(year, month, day)
    except ValueError as e:
        logging.error(f"Could not cast date: {e}")
        return JSONResponse(status_code=404, content={"message": "Enter a valid date"})

    if date.today() < requested_date:
        return JSONResponse(status_code=404, content={"message": "Choose a date in the past"})

    if sensor_id is None:
        visit_counts = store_dict[store_name].get_all_traffic(requested_date)
    else:
        visit_counts = store_dict[store_name].get_sensor_traffic(sensor_id, requested_date)

    if visit_counts < 0:
        return JSONResponse(status_code=404, content={"message": "The store was closed, try another date"})

    return JSONResponse(status_code=200, content=visit_counts)