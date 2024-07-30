import os
import unittest
from models import Inmobiliary
from pymongo import MongoClient

class InmobiliaryTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar la conexión a la base de datos de prueba
        cls.client = MongoClient(os.getenv('MONGO_URI'))
        cls.test_db = cls.client[os.getenv('TEST_DATABASE_NAME')]
        cls.inmobiliary_model = Inmobiliary(cls.test_db)
        cls.inmobiliary_collection = cls.inmobiliary_model.inmobiliary_collection

    @classmethod
    def tearDownClass(cls):
        # Borrar DB después de las pruebas
        cls.client.drop_database(os.getenv('TEST_DATABASE_NAME'))

    def setUp(self):
        # Limpiar la colección antes de cada prueba
        self.inmobiliary_collection.drop()

    def test_create_inmobiliary(self):
        inmobiliary_data = {
            "nombre": "Inmobiliaria XYZ",
            "nombre_corporativo": "Inmobiliaria XYZ S.A.",
            "direccion": "Calle Falsa 123",
            "ciudad": "Ciudad",
            "estado": "Estado",
            "postal": "12345",
            "pais": "País",
            "telefono": "123456789",
            "email": "contacto@inmobiliariaxyz.com",
            "web": "http://www.inmobiliariaxyz.com",
            "logo": "logo.png",
            "fundacion": {"year": 2000, "month": 1, "day": 1},
            "propiedades": []
        }
        result = self.inmobiliary_model.create_inmobiliary(**inmobiliary_data)
        self.assertTrue(result)

        # Crear una inmobiliaria con el mismo nombre corporativo debería fallar
        result = self.inmobiliary_model.create_inmobiliary(**inmobiliary_data)
        self.assertFalse(result)

    def test_update_inmobiliary(self):
        inmobiliary_data = {
            "nombre": "Inmobiliaria XYZ",
            "nombre_corporativo": "Inmobiliaria XYZ S.A.",
            "direccion": "Calle Falsa 123",
            "ciudad": "Ciudad",
            "estado": "Estado",
            "postal": "12345",
            "pais": "País",
            "telefono": "123456789",
            "email": "contacto@inmobiliariaxyz.com",
            "web": "http://www.inmobiliariaxyz.com",
            "logo": "logo.png",
            "fundacion": {"year": 2000, "month": 1, "day": 1},
            "propiedades": []
        }
        self.inmobiliary_model.create_inmobiliary(**inmobiliary_data)
        inmobiliary = self.inmobiliary_model.find_inmobiliary_by_business_name("Inmobiliaria XYZ S.A.")

        update_data = {
            "name": "Inmobiliaria Actualizada",
            "address": "Calle Actualizada 456"
        }
        result = self.inmobiliary_model.update_inmobiliary(inmobiliary["_id"], update_data)
        self.assertTrue(result)

        updated_inmobiliary = self.inmobiliary_model.find_inmobiliary_by_id(inmobiliary["_id"])
        self.assertNotEqual(inmobiliary, updated_inmobiliary)

        result = self.inmobiliary_model.update_inmobiliary("non_existing_inmobiliary_id", update_data)
        self.assertFalse(result)

    def test_delete_inmobiliary(self):
        inmobiliary_data = {
            "nombre": "Inmobiliaria XYZ",
            "nombre_corporativo": "Inmobiliaria XYZ S.A.",
            "direccion": "Calle Falsa 123",
            "ciudad": "Ciudad",
            "estado": "Estado",
            "postal": "12345",
            "pais": "País",
            "telefono": "123456789",
            "email": "contacto@inmobiliariaxyz.com",
            "web": "http://www.inmobiliariaxyz.com",
            "logo": "logo.png",
            "fundacion": {"year": 2000, "month": 1, "day": 1},
            "propiedades": []
        }
        self.inmobiliary_model.create_inmobiliary(**inmobiliary_data)
        inmobiliary = self.inmobiliary_model.find_inmobiliary_by_business_name("Inmobiliaria XYZ S.A.")

        result = self.inmobiliary_model.delete_inmobiliary(inmobiliary["_id"])
        self.assertTrue(result)

        result = self.inmobiliary_model.delete_inmobiliary("non_existing_inmobiliary_id")
        self.assertFalse(result)

    def test_get_all_inmobiliaries(self):
        inmobiliary_data1 = {
            "nombre": "Inmobiliaria XYZ",
            "nombre_corporativo": "Inmobiliaria XYZ S.A.",
            "direccion": "Calle Falsa 123",
            "ciudad": "Ciudad",
            "estado": "Estado",
            "postal": "12345",
            "pais": "País",
            "telefono": "123456789",
            "email": "contacto@inmobiliariaxyz.com",
            "web": "http://www.inmobiliariaxyz.com",
            "logo": "logo.png",
            "fundacion": {"year": 2000, "month": 1, "day": 1},
            "propiedades": []
        }
        inmobiliary_data2 = {
            "nombre": "Inmobiliaria ABC",
            "nombre_corporativo": "Inmobiliaria ABC S.A.",
            "direccion": "Calle Verdadera 456",
            "ciudad": "Otra Ciudad",
            "estado": "Otro Estado",
            "postal": "67890",
            "pais": "Otro País",
            "telefono": "987654321",
            "email": "contacto@inmobiliariaabc.com",
            "web": "http://www.inmobiliariaabc.com",
            "logo": "logo2.png",
            "fundacion": {"year": 2005, "month": 5, "day": 5},
            "propiedades": []
        }

        self.inmobiliary_model.create_inmobiliary(**inmobiliary_data1)
        self.inmobiliary_model.create_inmobiliary(**inmobiliary_data2)

        result = self.inmobiliary_model.get_all_inmobiliaries()
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()
