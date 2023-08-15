import pytest

if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_cases/web_ui", "--alluredir=test_results/reports/web_ui/allure-results"])