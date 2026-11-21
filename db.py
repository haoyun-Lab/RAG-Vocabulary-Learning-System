import pymysql
from pymysql.err import OperationalError

class QueryRecordDB:
    def __init__(self, host, user, password, db_name):
        self.conn = pymysql.connect(
            host=host, user=user, password=password, database=db_name,
            charset="utf8mb4"
        )
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS vocab_query (
            id INT PRIMARY KEY AUTO_INCREMENT,
            word VARCHAR(100),
            query_time DATETIME,
            result TEXT
        )
        """
        self.cursor.execute(sql)
        self.conn.commit()

    def insert_record(self, word: str, result: str):
        sql = "INSERT INTO vocab_query(word, query_time, result) VALUES (%, NOW(), %)"
        self.cursor.execute(sql, (word, result))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
