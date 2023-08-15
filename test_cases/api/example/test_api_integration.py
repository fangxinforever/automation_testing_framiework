import pytest
from common.api.test_case_entity import TestCaseEntity
from common.api.requstsLib import Request
test_case_entity = TestCaseEntity()


class TestIntegration:

    @pytest.mark.parametrize('data',
                             test_case_entity.read_file_to_test_case("test_data/api/example/testAPIIntergration.csv"))
    def test_scenario_001(self, data):
        Request().send_request(data)
