import pytest


@pytest.mark.usefixtures("postgre_init")
class TestPostgre():

    def test_add_data(self, postgre_init):
        """
        add data in the database
        :return:
        """
        values_to_insert = [
            ('Beryl_Autotest10', 'Beryl_Autotest10@epam.com', 'Ll123456#', '', '', '2022-11-23 05:40:57.000',
             '2022-11-24 05:40:57.000', False, '0')]
        print(len(values_to_insert))
        query = "insert into dev.user (user_name, email_address, password, creator, modifier, gmt_create, gmt_modify, locked, deleted) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        postgre_init.postgre_operate(sql=query, params=values_to_insert, data_num=len(values_to_insert))
