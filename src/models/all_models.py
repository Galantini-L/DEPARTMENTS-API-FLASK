import curses
from ..database.db import get_connection
from .entities import Departaments


###------DEPARTAMENTS------###
class Model_Departaments():

    @classmethod
    def get_departaments(self):
        try:
            cnx = get_connection()
            depts= []
            with cnx.cursor() as cursor:
                cursor.execute('SELECT id, name, price, department FROM products')
                dep_select= cursor.fetchall()
            
                for row in dep_select:
                    dep = Departaments(row[0],row[1],row[2],row[3])
                    depts.append(dep.to_JSON())
                    
            cnx.close()
            return depts
        except Exception as ex:
            raise ex

    @classmethod
    def get_departament(self,id):
            try:
                cnx = get_connection()
                with cnx.cursor(buffered=True) as cursor:
                    cursor.execute('SELECT id_depto,nombre_depto,ciudad,cod_director FROM departamentos WHERE id_depto = %(id)s', {'id':id})
                    row= cursor.fetchone()
                
                    if row != None:
                        dep = Departaments(row[0],row[1],row[2],row[3])
                        dept = dep.to_JSON()
                cnx.close()
                return dept
            except Exception as ex:
                raise ex

    @classmethod
    def post_department(self,departments):
        try:
            cnx = get_connection()
            data_insert = []
            with cnx.cursor() as cursor:
                for dept in departments:
                    cursor.execute('INSERT INTO products (id,name,price,department) VALUES (%(id)s, %(name)s, %(price)s, %(department)s)', {'id':dept['id'], 'name':dept['name'], 'price':dept['price'], 'department':dept['department']})
                    product_obj = Departaments(dept['id'],dept['name'],dept['price'],dept['department'])
                    data_insert.append(product_obj.to_JSON())
                    cnx.commit()
                cursor.execute('SELECT LAST_INSERT_ID()')
                cursor.close()
            cnx.close()
            return 
        except Exception as ex:
            print(f'exceotion {ex} at "all modules"')
            

###------PERSONS------###

class Model_Personos():
    def get_persons(self):
        pass

