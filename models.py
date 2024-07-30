from datetime import datetime
import os
from typing import Dict, List
import uuid

class Inmobiliary:
    def __init__(self, db):
        self.db = db
        self.inmobiliary_collection = self.db[os.getenv('INMOBILIARY_COLLECTION')]

    def create_inmobiliary(self, nombre: str, nombre_corporativo: str, direccion: str, ciudad: str, estado: str, postal: str, pais: str, telefono: str, email: str, web: str, logo: str, fundacion: Dict[str, int], propiedades: List[str]) -> bool:
        if self.inmobiliary_collection.find_one({"business_name": nombre_corporativo}):
            return False
        id_inmobiliaria = str(uuid.uuid4())
        inmobiliary = {
            "_id": id_inmobiliaria,
            "name": nombre,
            "business_name": nombre_corporativo,
            "address": direccion,
            "city": ciudad,
            "state": estado,
            "postal_code": postal,
            "country": pais,
            "phone": telefono,
            "email": email,
            "website": web,
            "logo": logo,
            "founding_date": datetime(fundacion["year"], fundacion["month"], fundacion["day"]),
            "properties": propiedades
        }
        self.inmobiliary_collection.insert_one(inmobiliary)
        return True

    def find_inmobiliary_by_id(self, inmobiliary_id: str) -> dict:
        return self.inmobiliary_collection.find_one({"_id": inmobiliary_id})
    
    def find_inmobiliary_by_business_name(self, inmobiliary_corporative_name: str) -> dict:
        return self.inmobiliary_collection.find_one({"business_name": inmobiliary_corporative_name})

    def get_all_inmobiliaries(self) -> List[dict]:
        return list(self.inmobiliary_collection.find())

    def update_inmobiliary(self, inmobiliary_id: str, update_data: dict) -> bool:
        allowed_fields = {'name', 'address', 'city', 'state', 'postal_code', 'country', 'phone', 'email', 'website', 'logo', 'founding_date', 'properties'}
        filtered_data = {key: value for key, value in update_data.items() if key in allowed_fields}
        if 'founding_date' in filtered_data:
            fundacion = filtered_data['founding_date']
            if isinstance(fundacion, dict) and {'year', 'month', 'day'} <= fundacion.keys():
                filtered_data['founding_date'] = datetime(fundacion['year'], fundacion['month'], fundacion['day'])

        return self.inmobiliary_collection.update_one({"_id": inmobiliary_id}, {"$set": filtered_data}).modified_count > 0

    def delete_inmobiliary(self, inmobiliary_id: str) -> bool:
        return self.inmobiliary_collection.delete_one({"_id": inmobiliary_id}).deleted_count > 0
