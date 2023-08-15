import psycopg2

from common.base.config import conf
from common.base import logger


class PostGreHelper:
    conn = None

    def __init__(self, database):
        """
        To initialize the database variables and connect database
        """
        self.database = conf.get(database, "database")
        self.user = conf.get(database, "user")
        self.password = conf.get(database, "password")
        self.host = conf.get(database, "host")
        self.port = conf.get(database, "port")
        self.result = None
        try:
            self.conn = psycopg2.connect(database=self.database,
                                         user=self.user,
                                         password=self.password,
                                         host=self.host,
                                         port=self.port)
            logger.info("connect database successfully")
        except Exception as e:
            logger.error("connect database failed")
            raise e
        self.cursor = self.conn.cursor()

    def disconn(self):
        """
        if the database is opened, close it
        :return:
        """
        if self.conn and self.cursor:
            self.cursor.close()
            self.conn.close()
        logger.info("close database successfully")

    def execute_sql_params(self, sql, params):
        try:
            # execute
            self.cursor.execute(sql, params)
            logger.info("execute sql successfully!")
        except psycopg2.Error as e:
            print(f"execute：{sql}，error, error message：{e}")

    def execute_method(self, sql, params=None, method_name=None):
        # execute_sql_params
        self.execute_sql_params(sql, params)
        if method_name is not None:
            # fetchone
            if "find_one" == method_name:
                self.result = self.cursor.fetchone()
            # fetchall
            elif "find_all" == method_name:
                self.result = self.cursor.fetchall()
        # close the connection
        self.disconn()

    def find_one(self, sql, params=None):
        """
        Query and return the first record
        :param sql: sql statement
        :param params: sql args
        :return:
        """
        try:
            self.execute_method(sql, params=params, method_name="find_one")
            logger.info("Single query successfully!")
        except Exception as e:
            logger.error("Query exception: ", e)
        return self.result

    def find_all(self, sql, params=None):
        """
        Query and return all records
        :param sql: sql statement
        :param params: sql args
        :return:
        """
        try:
            self.execute_method(sql, params=params, method_name="find_all")
            logger.info("Query successful!")
        except Exception as e:
            logger.error("Query exception: ", e)
        return self.result

    def postgre_operate(self, sql, params=(), data_num=None):
        """
        insert/update/delete data
        :param sql: sql statement
        :param params: sql args
        :data_num: operate one data or multiple data
        :return:
        """
        if data_num >= 1:
            if "INSERT" in str(sql).upper():
                return self._edit_sql(sql, params)
            elif "UPDATE" in str(sql).upper():
                return self._edit_sql(sql, params)
            elif "DELETE" in str(sql).upper():
                return self._edit_sql(sql, params)
            else:
                logger.info("The sql is not to insert/update/delete")
        else:
            logger.info("no data to operate")

    def _edit_sql(self, sql, params=()):
        """
        execute multiple sql
        :param sql: sql statement
        :param params: sql args
        :return:
        """
        count = 0
        try:
            count = self.cursor.executemany(sql, params)
            self.conn.commit()
            logger.info("Execute sql successfully")
        except Exception as e:
            logger.exception("fail to execute sql")
            raise e
        return count
