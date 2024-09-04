import sqlite3

class EsrogimDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.row_query_string = '''id, size, clenleaness, chabad, reservedBy'''


    def table_info(self):
        conn = self._connect()
        cursor = conn.cursor()
        sql = '''PRAGMA table_info(esrogim)'''
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        table_info = {}
        for row in result:
            table_info[row[1]] = row[2]

        return table_info


    def create_table(self):
        conn = self._connect()
        cursor = conn.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS esrogim
                 (id INTEGER PRIMARY KEY, size INTEGER, clenleaness INTEGER, chabad INTEGER, reservedBy INTEGER, sold boolean DEFAULT false)'''
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def insert_esrog(self, size, cleanliness, chabad):
        conn = self._connect()
        cursor = conn.cursor()
        sql = '''INSERT INTO esrogim (size, clenleaness, chabad) VALUES (?, ?, ?)'''
        cursor.execute(sql, (size, cleanliness, chabad))
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.lastrowid

    def get_esrog_by_id(self, esrog_id):
        conn = self._connect()
        cursor = conn.cursor()
        sql = f'''SELECT {self.row_query_string} FROM esrogim WHERE id = ?'''
        cursor.execute(sql, (esrog_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    def update_esrog(self, esrog_id, size=None, clenleaness=None, chabad=None):
        conn = self._connect()
        cursor = conn.cursor()

        updates = []
        params = []

        if size is not None:
            updates.append('size = ?')
            params.append(size)
        if clenleaness is not None:
            updates.append('clenleaness = ?')
            params.append(clenleaness)
        if chabad is not None:
            updates.append('chabad = ?')
            params.append(chabad)

        if updates:
            sql = f'''UPDATE esrogim SET {', '.join(updates)} WHERE id = ?'''
            params.append(esrog_id)
            cursor.execute(sql, tuple(params))
            conn.commit()

        cursor.close()
        conn.close()

    def delete_esrog(self, esrog_id):
        conn = self._connect()
        cursor = conn.cursor()
        sql = '''DELETE FROM esrogim WHERE id = ?'''
        cursor.execute(sql, (esrog_id,))
        conn.commit()
        cursor.close()
        conn.close()

    def reserve_esrog(self, esrog_id: int, reserved_by: str) -> bool:
        print(locals())
        conn = self._connect()
        cursor = conn.cursor()
        sql = """UPDATE esrogim SET reservedBy = ? WHERE id = ? and reservedBy = '__not_reserved__'"""
        cursor.execute(sql, (reserved_by, esrog_id))
        conn.commit()
        cursor.close()
        conn.close()

        print(f"{cursor.rowcount = }")

        # check if update was successful
        return cursor.rowcount > 0

    def check_reserved(self, esrog_id: int):
        conn = self._connect()
        cursor = conn.cursor()
        sql = '''SELECT reservedBy FROM esrogim WHERE id = ?'''
        cursor.execute(sql, (esrog_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print(f"{result = }")
        return result

    def get_all_esrogim(self):
        conn = self._connect()
        cursor = conn.cursor()
        sql = f'''SELECT {self.row_query_string} FROM esrogim'''
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    
    def get_all_available_esrogim(self):
        conn = self._connect()
        cursor = conn.cursor()
        sql = f'''SELECT {self.row_query_string} FROM esrogim WHERE reservedBy = '__not_reserved__' and sold = false'''
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results



