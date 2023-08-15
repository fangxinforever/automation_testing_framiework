from common.base import mysql_operator
from common.base import postgre_operation
import pytest


@pytest.fixture(scope="module")
def mysql_init():
    """
    sql setup: connect
    :return:
    """
    # setup: connect to database

    my_database = mysql_operator.MySqlDataBase(database="db_dev")
    yield my_database
    # teardown: close database
    my_database.close_db()


@pytest.fixture(scope="module")
def postgre_init():
    """
    postgre init: postgre DB connect
    :return:
    """
    # setup: connect to database

    pg_helper = postgre_operation.PostGreHelper(database="postgre_dev")
    yield pg_helper
    # teardown: close database
    pg_helper.disconn()
