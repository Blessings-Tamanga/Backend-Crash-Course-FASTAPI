from fastapi import APIRouter
from fastapi import HTTPException
from app.models import VehicleModel, UpdateModel
from app.databases import vehicles

router = APIRouter()

@router.get("/vehicles")
def get_vehicles():
    return vehicles

@router.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id : int):
    for vehicle in vehicles:
        if vehicle_id == vehicle["vehicle_id"]:
            return {
                "vehicle_name": vehicle["vehicle_name"],
                "vehicle_price" : vehicle["vehicle_price"]
                }
        
    raise HTTPException(status_code = 404, detail = "vehicle not found")


@router.post("/vehicles")
def add_vehicle(vehicle : VehicleModel):
        vehicle_id = len(vehicles) + 1
        new_vehicle = {
            "vehicle_id" : vehicle_id,
            "vehicle_name" : vehicle.name,
            "vehicle_price" : vehicle.price
        }

        vehicles.append(new_vehicle)

        return {"message": "newvehicle added"}



@router.put("/vehicles/{vehicle_id}")
def update_vehicle(vehicle_id : int, updated_vehicle : UpdateModel):
    for vehicle in vehicles:
        if vehicle_id == vehicle["vehicle_id"]:
            vehicle["vehicle_name"] = updated_vehicle.name
            vehicle["vehicle_price"] = updated_vehicle.price
           
            return{
                    "message":"vehicle updated"
               }
        
    raise HTTPException(status_code = 404, detail = "vehicle not found")


@router.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id : int):
    for vehicle in vehicles:
        if vehicle_id == vehicle["vehicle_id"]:
           vehicles.remove(vehicle)
        return {"message":"vehicle deleted"}
    raise HTTPException(status_code = 404, detail = "vehicle not found")