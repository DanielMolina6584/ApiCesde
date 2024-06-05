from domain.BaseDatos import BaseDeDatos


class Crud(BaseDeDatos):
    def crearUsuario(self, nombre, apellido, correo, password):
        sql = "INSERT INTO usuarios (nombre, apellido, correo, contraseña) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellido, correo, password)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def getUsuario(self, correo):
        query = "SELECT * FROM usuarios WHERE correo = %s"
        self.cursor.execute(query, (correo,))
        usuario = self.cursor.fetchone()
        if usuario:
            keys = ['id', 'nombre', 'apellido', 'correo', 'contraseña', 'imagen']
            return dict(zip(keys, usuario))
        return None

    def getEjercicios(self):
        self.cursor.execute("SELECT * FROM ejercicios")
        rows = self.cursor.fetchall()
        column_names = self.cursor.column_names
        ejercicios = [dict(zip(column_names, row)) for row in rows]
        return ejercicios

    def getEjerciciosByType(self, ejercicio_type):
        query = "SELECT * FROM ejercicios WHERE type = %s"
        self.cursor.execute(query, (ejercicio_type,))
        rows = self.cursor.fetchall()
        column_names = self.cursor.column_names
        ejercicios = [dict(zip(column_names, row)) for row in rows]
        return ejercicios

    def crearEjercicio(self, ejercicio, descripcion, repeticiones, series, tipo, imagen=None):
        sql = "INSERT INTO ejercicios (ejercicio, descripcion, repeticiones, series, type, imagen) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (ejercicio, descripcion, repeticiones, series, tipo, imagen)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminarEjercicio(self, ejercicio_id):
        sql = "DELETE FROM ejercicios WHERE id = %s"
        self.cursor.execute(sql, (ejercicio_id,))
        self.conexion.commit()

    def actualizarEjercicio(self, id, ejercicio, descripcion, repeticiones, series, tipo, imagen=None):
        sql = "UPDATE ejercicios SET ejercicio=%s, descripcion=%s, repeticiones=%s, series=%s, type=%s, imagen=%s WHERE id=%s"
        valores = (ejercicio, descripcion, repeticiones, series, tipo, imagen, id)
        self.cursor.execute(sql, valores)
        self.conexion.commit()