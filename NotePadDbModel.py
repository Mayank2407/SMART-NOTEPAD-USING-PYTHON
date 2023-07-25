from cx_Oracle import *
from traceback import *


class Db_Model:
    def __init__(self):
        self.file_dict = {}
        self.db_status = True
        self.conn = None
        self.cur = None  # currsor ki help se queries execute karwaate hai
        try:
            self.conn = connect("c##mojo/123@127.0.0.1/orcl")
            print("connected successfully")
            self.cur = self.conn.cursor()
        except DatabaseError:
            self.db_status = False
            print("DB Error:", format_exc())

    def get_db_status(self):
        return self.db_status

    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
        print("Disconnectd successfully from the db")

    def add_file(self, file_name, file_path, file_owner, file_pwd):
        self.file_dict[file_name] = (file_path, file_owner, file_pwd)
        print("File added:", self.file_dict[file_name])

    def get_file_path(self, file_name):
        file_path, file_owner, file_pwd = self.file_dict[file_name]
        return file_path

    def add_file_to_db(self, file_name, file_path, file_owner, file_pwd):
        self.cur.execute("select max(file_id) from securemyfiles")
        last_file_id = self.cur.fetchone()
        next_file_id = 1
        if last_file_id is not None:
            next_file_id = last_file_id[0] + 1
        self.cur.execute("insert into securemyfiles values(:1,:2,:3,:4,:5)",
                         (next_file_id, file_name, file_path, file_owner, file_pwd))
        self.conn.commit()
        return "file successfully added to the database"

    def load_files_from_db(self):
        self.cur.execute("select file_name,file_path,file_owner,file_pwd from securemyfiles")
        record_added = False
        for file_name, file_path, file_owner, file_pwd in self.cur:
            self.file_dict[file_name] = (file_path, file_owner, file_pwd)
            record_added = True
        if record_added == True:
            return "Files populated from db "
        else:
            return "No Files present in your db"

    def remove_file_from_db(self, file_name):
        self.cur.execute("delete from securemyfiles where file_name=1", (file_name,))
        if self.cur.rowcount == 0:
            return "File not present in DB"
        else:
            self.file_dict.pop(file_name)
            self.conn.commit()
            return "File deleted from db"

    def is_secure_file(self, file_name):
        return file_name in self.file_dict

    def get_file_pwd(self, file_name):
        file_path, file_owner, file_pwd = self.file_dict[file_name]
        return file_pwd

    def get_file_count(self):
        return len(self.file_dict)
