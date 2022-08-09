class Departaments():
    def __init__(self,id_depto= None,nombre_depto= None,ciudad= None,cod_director= None) -> None:
        self.id = id_depto
        self.nombre_depto=nombre_depto
        self.ciudad= ciudad
        self.cod_director=cod_director

    def to_JSON(self):
        return {
            'id':self.id,
            'nombre_depto': self.nombre_depto,
            'ciudad':self.ciudad,
            'cod_director':self.cod_director
        }