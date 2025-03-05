class Libro:
    """
    Representa un libro con atributos como título, autor, categoría e ISBN.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    """
    Representa a un usuario de la biblioteca con atributos como nombre, ID de usuario y una lista de libros prestados.
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Gestiona las colecciones de libros, usuarios y préstamos.
    """

    def __init__(self):
        self.libros = {}  # ISBN: Libro
        self.usuarios = set()  # IDs de usuario
        self.usuarios_registrados = {} # id_usuario: Usuario

    def agregar_libro(self, libro):
        """Añade un libro a la biblioteca."""
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print(f"Error: El libro con ISBN {libro.isbn} ya existe.")

    def quitar_libro(self, isbn):
        """Quita un libro de la biblioteca."""
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"Error: No se encontró ningún libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca."""
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con ID {usuario.id_usuario}.")
        else:
            print(f"Error: El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        """Da de baja a un usuario existente de la biblioteca."""
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.usuarios_registrados[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"Error: No se encontró ningún usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        """Presta un libro a un usuario."""
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            usuario = self.usuarios_registrados[id_usuario]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            else:
                print(f"Error: El libro '{libro.titulo}' ya está prestado a {usuario.nombre}.")
        else:
            print("Error: Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        """Permite a un usuario devolver un libro."""
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            usuario = self.usuarios_registrados[id_usuario]
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print(f"Error: El libro '{libro.titulo}' no está prestado a {usuario.nombre}.")
        else:
            print("Error: Usuario o libro no encontrado.")

    def buscar_libros(self, criterio, valor):
        """Busca libros por título, autor o categoría."""
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        """Muestra una lista de todos los libros prestados a un usuario."""
        if id_usuario in self.usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            return usuario.libros_prestados
        else:
            print("Error: Usuario no encontrado.")
            return []


# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "9780061120084")
libro2 = Libro("1984", "George Orwell", "Ciencia ficción", "9780451524935")
libro3 = Libro("El señor de los anillos", "J.R.R. Tolkien", "Fantasía", "9780618260231")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Juan Cañar", "12345")
usuario2 = Usuario("María García", "67890")

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("12345", "9780061120084")
biblioteca.prestar_libro("67890", "9780451524935")

# Buscar libros
resultados = biblioteca.buscar_libros("autor", "Orwell")
for libro in resultados:
    print(libro)

# Listar libros prestados
libros_prestados = biblioteca.listar_libros_prestados("12345")
print("\nLibros prestados a Juan Cañar:")
for libro in libros_prestados:
    print(libro)

# Devolver libro
biblioteca.devolver_libro("12345", "9780061120084")

# Listar libros prestados después de la devolución
libros_prestados = biblioteca.listar_libros_prestados("12345")
print("\nLibros prestados a Juan Cañar después de la devolución:")
for libro in libros_prestados:
    print(libro)