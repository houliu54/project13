import os

import pytest

if __name__ == '__main__':
    pytest.main(['-v','-s','./testpytest/test_pytest.py','--alluredir=./report/json', '--clean-alluredir'])
    os.system('allure generate ./report/json -o ./report/html --clean')