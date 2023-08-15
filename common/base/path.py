import os

# Project root directory
Base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

# The path to the test case
case_dir = os.path.join(Base_path, 'test_cases')

# The path to the log
log_dir = os.path.join(Base_path, 'test_results/logs')

app_dir = os.path.join(Base_path, 'test_data/app_ui')
# The path to the report
report_dir = os.path.join(Base_path, 'test_results/reports')

# The path to the config file
conf_dir = os.path.join(Base_path, 'config')

# The path to the test screenshots
screenshot_dir = os.path.join(Base_path, 'test_results/screenshots')
