from domain.BaseDatos import BaseDeDatos

class CRUD(BaseDeDatos):
    def crearInfoPersona(self, nombre, apellido, email, cel):
        sql = "INSERT INTO informacionpersonas (nombre, apellido, email, cel) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellido, email, cel)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def getInfoPersona(self):
        self.cursor.execute("SELECT * FROM informacionpersonas")
        return self.cursor.fetchall()

    def actualizarInfoPersona(self, id_persona, nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_cel):
        sql = "UPDATE informacionpersonas SET nombre = %s, apellido = %s, email = %s, cel = %s WHERE id = %s"
        valores = (nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_cel, id_persona)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminarInfoPersona(self, id_persona):
        sql = "DELETE FROM informacionpersonas WHERE id = %s"
        valores = (id_persona)
        self.cursor.execute(sql, valores)
        self.conexion.commit()