import pymysql

class Database:
    @staticmethod
    def connect():
        return pymysql.connect(host="phonebook-mysql", user="dev", password="dev", database="crud_flask", charset='utf8mb4')


class EstudanteDAO:
    def read(self):
        query = "SELECT * FROM Estudantes ORDER BY nome ASC"

        with Database.connect() as con:
            cursor = con.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        
    def read_by_id(self, id):
        query = "SELECT * FROM Estudantes WHERE id = %s"
        values = (id,)

        with Database.connect() as con:
            cursor = con.cursor()
            cursor.execute(query, values)
            return cursor.fetchall()

    def insert(self, data):
        query = "INSERT INTO Estudantes (nome, email, matricula, curso, senha, administrador, foto_perfil) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (data['nome'], data['email'], data['matricula'], data['curso'], data['senha'], data['administrador'], data['foto_perfil'])

        with Database.connect() as con:
            cursor = con.cursor()
            try:
                cursor.execute(query, values)
                con.commit()
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao inserir estudante: {e}")
                return False

    def update(self, id, data):
        query = "UPDATE Estudantes SET nome = %s, email = %s, matricula = %s, curso = %s, senha = %s, administrador = %s, foto_perfil = %s WHERE id = %s"
        values = (data['nome'], data['email'], data['matricula'], data['curso'], data['senha'], data['administrador'], data['foto_perfil'], id)

        with Database.connect() as con:
            cursor = con.cursor()
            try:
                cursor.execute(query, values)
                con.commit()
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao atualizar estudante: {e}")
                return False

    def delete(self, id):
        query = "DELETE FROM Estudantes WHERE id = %s"
        values = (id,)

        with Database.connect() as con:
            cursor = con.cursor()
            try:
                cursor.execute(query, values)
                con.commit()
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao deletar estudante: {e}")
                return False

class AvaliacaoDAO:
    def read(self):
        query = "SELECT * FROM Avaliacoes ORDER BY id ASC"

        with Database.connect() as con:
            cursor = con.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def read_by_id(self, id):
        query = "SELECT * FROM Avaliacoes WHERE id = %s"
        values = (id,)

        with Database.connect() as con:
            cursor = con.cursor()
            cursor.execute(query, values)
            return cursor.fetchall()

    def insert(self, data):
        query = "INSERT INTO Avaliacoes (estudante_id, turma_id, avaliacao) VALUES (%s, %s, %s)"
        values = (data['estudante_id'], data['turma_id'], data['avaliacao'])

        with Database.connect() as con:
            cursor = con.cursor()
            try:
                cursor.execute(query, values)
                con.commit()
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao inserir avaliação: {e}")
                return False

    def update(self, id, data):
        query = "UPDATE Avaliacoes SET estudante_id = %s, turma_id = %s, avaliacao = %s WHERE id = %s"
        values = (data['estudante_id'], data['turma_id'], data['avaliacao'], id)

        with Database.connect() as con:
            cursor = con.cursor()
            try:
                cursor.execute(query, values)
                con.commit()
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao atualizar avaliação: {e}")
                return False

    def delete(self, id):
        query = "DELETE FROM Avaliacoes WHERE id = %s"
        values = (id,)

        with Database.connect() as con:
            cursor = con.cursor()
            try:
                cursor.execute(query, values)
                con.commit()
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao deletar avaliação: {e}")
                return False

class DenunciaDAO:
    def read(self):
        query = "SELECT * FROM Denuncias ORDER BY id ASC"

        with Database.connect() as con:
            cursor = con.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def read_by_id(self, id):
        query = "SELECT * FROM Denuncias WHERE id = %s"
        values = (id,)

        with Database.connect() as con:
            cursor = con.cursor()
            cursor.execute(query, values)
            return cursor.fetchall()

    def insert(self, data):
        query = "INSERT INTO Denuncias (estudante_id, avaliacao_id, denuncia) VALUES (%s, %s, %s)"
        values = (data['estudante_id'], data['avaliacao_id'], data['denuncia'])

        with Database.connect() as con:
            cursor = con.cursor()
            try:
                cursor.execute(query, values)
                con.commit()
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao inserir denúncia: {e}")
                return False

    def update(self, id, data):
        query = "UPDATE Denuncias SET estudante_id = %s, avaliacao_id = %s, denuncia = %s WHERE id = %s"
        values = (data['estudante_id'], data['avaliacao_id'], data['denuncia'], id)

        with Database.connect() as con:
            cursor = con.cursor()
            try:
                cursor.execute(query, values)
                con.commit()
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao atualizar denúncia: {e}")
                return False

    def delete(self, id):
        query = "DELETE FROM Denuncias WHERE id = %s"
        values = (id,)

        with Database.connect() as con:
            cursor = con.cursor()
            try:
                cursor.execute(query, values)
                con.commit()
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao deletar denúncia: {e}")
                return False


"""
    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute(
                    "SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)",
                           (data['name'], data['phone'], data['address'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s",
                           (data['name'], data['phone'], data['address'], id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
"""