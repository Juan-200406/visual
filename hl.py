class libre:
    def __init__(self, titulo, autor categooria, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.categoria= categooria
        self.ISBN = ISBN
    def __str__(self):
        titulo_str = "_".join(map(str, self.titulo))
        return f"titulo : {titulo_str}"
    def __str__(self):    
        autor_str = "_".join(map(str, self.autor))
        return f"autot : {autor_str}"
class usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.libros = {} 
        self.libro= {} 
    def __str__(self):
        id_str = "_".join(mapa(str,self.id))
        return f"id : {id_str}"
      
    def libros(self, a ,b,):     
        self.libros[1.a,2b = ocupados 
    def libro(self, c,d):
        self.libro[1.c,2.d] = disponible1
           
    def bibliotecas(self):
        if self.nombre== self.libros:
            print("ocupado ") 

