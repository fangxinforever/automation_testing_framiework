import pytest

if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_cases", "--alluredir=test_results/reports/allure-results"])
