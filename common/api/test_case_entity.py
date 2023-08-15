from common.base.csv_util import read_csv


class TestCaseEntity:
    module = None
    case_no = None
    case_name = None
    url = None
    method = None
    headers = None
    params = None
    request_payload = None
    http_code = None
    response = None
    validations = None
    variables = None
    response_header_validations = None
    response_header_variables = None

    def read_file_to_test_case(self, file_path):
        """
        read csv file and convert data to test case type
        :param file_path: file relative path
        :return:
        """
        test_case_list = []
        file_data = read_csv(file_path)
        for data in file_data:
            test_case_entity = TestCaseEntity()
            test_case_entity.module = data['Module']
            test_case_entity.case_no = data['CaseNo']
            test_case_entity.case_name = data['CaseName']
            test_case_entity.url = data['Url']
            test_case_entity.method = data['Method']
            test_case_entity.headers = data['Headers']
            test_case_entity.params = data['Params']
            test_case_entity.request_payload = data['RequestPayload']
            test_case_entity.http_code = data['HttpCode']
            test_case_entity.response = data['Response']
            test_case_entity.validations = data['Validations']
            test_case_entity.variables = data['Variables']
            test_case_entity.response_header_validations = data['ResponseHeaderValidations']
            test_case_entity.response_header_variables = data['ResponseHeaderVariables']
            test_case_list.append(test_case_entity)
        return test_case_list
