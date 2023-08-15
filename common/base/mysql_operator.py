import pymysql
from common.base.config import conf
from common.base import logger


class MySqlDataBase:
    # define none connection
    conn = None

    def __init__(self, database):
        """
        To initialize the database variables and connect database
        """
        self.host = conf.get(database, "host")
        self.user = conf.get(database, "user")
        self.password = conf.get(database, "password")
        self.db = conf.get(database, "database")
        self.port = int(conf.get(database, "port"))
        try:
            # step1: create connect
            self.conn = pymysql.connect(host=self.host,
                                        user=self.user,
                                        password=self.password,
                                        db=self.db,
                                        port=self.port)
            logger.info("connect database successfully")
        except Exception as e:
            logger.error("connect database failed")
            raise e
        # Step2: create cursor object
        self.cursor = self.conn.cursor()

    def close_db(self):
        """
        if the database is opened, close it
        :return:
        """
        if self.conn and self.cursor:
            self.cursor.close()
            self.conn.close()
            logger.info("close database successfully")

    def select_one(self, sql, params=None):
        """
        Query and return the first record
        :param sql: sql statement
        :param params: sql args
        :return:
        """
        result = None
        try:
            if "SELECT" in str(sql).upper():
                self.cursor.execute(sql, params)
                logger.info(sql)
                result = self.cursor.fetchone()
                logger.info("Single query successfully: {}".format(result))
        except Exception as e:
            logger.error("Query exception: ", e)
        return result

    def select_all(self, sql, params=()):
        """
        Query and return all records
        :param sql: sql statement
        :param params: sql args
        :return:
        """
        list_data = None
        try:
            if "SELECT" in str(sql).upper():
                self.cursor.execute(sql, params)
                list_data = self.cursor.fetchall()
                logger.info("Data number is: {}".format(len(list_data)))
                logger.info("Query successfully")
        except Exception as e:
            logger.error("Query exception: ", e)
        return len(list_data)

    def mysql_operate(self, sql, params=()):
        """
        insert/update/delete data
        :param sql: sql statement
        :param params: sql args
        :data_num: operate one data or multiple data (1 = one data, 2 = multiple data)
        :return:
        """
        if "INSERT" in str(sql).upper():
            return self._edit_sql(sql, params)
        elif "UPDATE" in str(sql).upper():
            return self._edit_sql(sql, params)
        elif "DELETE" in str(sql).upper():
            return self._edit_sql(sql, params)
        else:
            logger.info("The sql is not to insert/update/delete or invalid sql")

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
