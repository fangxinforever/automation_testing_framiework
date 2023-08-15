import pytest
from common.base import logger


@pytest.mark.usefixtures("mysql_init")
class TestMySql():

    def test_add_one_data(self, mysql_init):
        """
        add one data in the database
        :return:
        """
        mysql_init.mysql_operate(
            sql="insert into city (Name, CountryCode, District, Population) values (%s,%s,%s,%s)",
            params=[('Linda', 'CHN', 'SC', '10000')])
        select_one_data = mysql_init.select_one(sql="SELECT * FROM city where name = %s", params=('Linda'))
        if select_one_data:
            logger.info("insert successfully: {}".format(select_one_data))
        else:
            logger.error("fail to insert data")

    def test_get_data(self, mysql_init):
        """
        get one data from mysql
        :return:
        """
        select_one_data = mysql_init.select_one(sql="SELECT population FROM city where name = %s", params=('Linda'))
        logger.info(select_one_data[0])

    def test_update_data(self, mysql_init):
        """
        update data in the database
        :return:
        """
        mysql_init.mysql_operate(sql="update city set population = 1780001 where name = %s", params=[('Linda')])
        select_one_data = mysql_init.select_one(sql="SELECT population FROM city where name = %s", params=('Linda'))
        logger.info(select_one_data[0])

    def test_add_multi_data(self, mysql_init):
        """
        add multiple data in the database
        :return:
        """
        values_to_insert = [('Linda1', 'CHN', 'SC', '10000'), ('Linda2', 'CHN', 'SC', '20000')]
        query = "insert into city (Name, CountryCode, District, Population) values (%s, %s, %s, %s)"
        mysql_init.mysql_operate(sql=query, params=values_to_insert)
        select_multi_data = mysql_init.select_all('SELECT * FROM city where name like %s"%%"', params=('Linda'))
        if select_multi_data >= 2:
            logger.info("insert multiple data successfully. New Data has {}".format(select_multi_data))
        else:
            logger.error("fail to insert multiple data")

    def test_delete_one_data(self, mysql_init):
        """
        delete one data in the database
        :return:
        """
        mysql_init.mysql_operate(sql='delete FROM city where name = %s', params=[('Linda')])
        if not mysql_init.select_one('SELECT * FROM city where name = "%s"', params=('Linda')):
            logger.info("delete successfully")
        else:
            logger.error("fail to delete data")

    def test_delete_all_data(self, mysql_init):
        """
        delete all data in the database
        :return:
        """
        mysql_init.mysql_operate(sql='delete FROM city where name like %s"%%"', params=[('Linda')])
        if not mysql_init.select_all('SELECT * FROM city where name like %s"%%"', params=('Linda')):
            logger.info("delete successfully")
        else:
            logger.error("fail to delete data")
