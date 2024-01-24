from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM dojos
        """

        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query)



        dojos = []
        for row in results:
            new_dojo = cls(row)
            dojos.append(new_dojo)


        return dojos

    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO dojos (name) 
            VALUES(%(name)s);
        """
        return connectToMySQL("dojo_and_ninjas_schema").query_db(query, form_data)

    @classmethod
    def read_ninjas(cls, id):
        data = {
            "id":id
        }

        query = """
            SELECT * FROM dojos 
            JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query, data)
        if len(results) == 0:
            return []
        
        dojo = cls(results[0])

        for row_from_db in results:
            ninja_data = {
            "id" : row_from_db["ninjas.id"],
            "first_name" : row_from_db["first_name"],
            "last_name" : row_from_db["last_name"],
            "age" : row_from_db["age"],
            "created_at" : row_from_db["ninjas.created_at"],
            "updated_at" : row_from_db["ninjas.updated_at"],
            }
            dojo.ninjas.append(Ninja(ninja_data))
            
        return dojo
        # ninjas = []

        # for row in results:
        #     new_ninja = cls(row)

        #     dojo_data = {
        #         **row,
        #         "id" : row["dojos.id"],
        #         "created_at" : row["dojos.created_at"],
        #         "updated_at" : row["dojos.updated_at"]
        #     }

        #     new_dojo = Dojo(dojo_data)

        #     new_ninja.dojo = new_dojo
        #     ninjas.append(new_ninja)
        
        
        # return ninjas
