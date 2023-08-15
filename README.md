## Framework Purpose ：

* Create an easy-to-use, extensible automated testing framework based python.

## Framework Description

* This framework supports API automated testing, Web UI automated testing, and App UI automated testing
* This framework consists of the following tools:
  * pytest: a unit testing framework for python
  * pytest-xdist: a plugin for pytest, which can execute test cases in multiple processes at the same time
  * allure-pytest: used to generate test reports
  * assertpy: a rich assertion library that supports pytest
  * requests: http request framework
  * Appium: Automated testing framework for mobile
  * selenium: web ui automated testing framework
  * JPype1: used to execute java code
  * PyMySQL: used to manipulate MySQL databases

## Framework Structure

* common: public module
* config: config file
* page_objects: locator, pages function
* test_cases: web_ui api app_ui
* test_data: web_ui api app_ui
* test_results: logs, reports, screenshots

### GET STARTED:

1. install from requirements: pip install -r requirements.txt
2. run testcase from command(clean old reports): pytest .\test_cases\ --alluredir=test_results/reports/allure-results --clean-alluredir
3. run testcase from command: pytest .\test_cases\ --alluredir=test_results/reports/allure-results
4. copy environment.properties to report: copy .\config\allure\environment.properties .\test_results\reports\allure-results\
5. copy categories.json to report: copy .\config\allure\categories.json .\test_results\reports\allure-results\
6. check allure report: allure serve .\test_results\reports\allure-results\
7. performance test:command :python startJmeter.py [jmx name] [num_threads] [ramp_time] [duration] [remark][thread_group_name]

### Tips:

1. One-click import of third-party libraries to requirements.text: pip freeze > requirements.txt
2. One-click import of third-party dependencies: pip install -r requirements.txt


