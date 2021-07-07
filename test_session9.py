##########################################
#############  Imports ###################
##########################################
from session9 import *
import pytest
from io import StringIO
import sys

##########################################
#########  To Capture Output  ############
##########################################
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


##########################################
############  Question 1 #################
##########################################


def test_profile_nt_cnt():
    a = profile_nt()
    assert a['count'] == 10000, "Number of profiles must be 10000!"


def test_profile_nt_bt_cnt():
    a = profile_nt()
    assert a['common_bt_cnt'] <= a['count'], "Max blood type count exceeds number of profiles!"


def test_profile_nt_max_avg():
    a = profile_nt()
    assert [True if a['max_year'] > a['avg_year'] else (True if a['max_mnt'] > a['avg_mnt'] else(
        True if a['max_day'] > a['avg_day'] else False))], "How can the max age be less than the average age!"


def test_profile_nt_out():
    a = profile_nt()
    assert len(a.keys()) >= 8, 'Insufficient number of outputs in your code!'


def test_profile_nt_neg():
    a = profile_nt()
    assert sum(number < 0 for number in [a['max_year'], a['max_mnt'], a['max_day'],
               a['avg_year'], a['avg_mnt'], a['avg_day']]) == 0, "Year/Month/Day cannot be negative"


def test_profile_nt_prnt_time():
    with Capturing() as output:
        profile_nt()
    assert any(["Time" in o for o in output]
               ), "How will you compare the time with the dictionary approach???"


def test_profile_nt_doc():
    assert profile_nt.__doc__, "Your function must have a docstring"


##########################################
############  Question 2 #################
##########################################

def test_profile_dict_cnt():
    a = profile_dict()
    assert a['count'] == 10000, "Number of profiles must be 10000!"


def test_profile_dict_bt_cnt():
    a = profile_dict()
    assert a['common_bt_cnt'] <= a['count'], "Max blood type count exceeds number of profiles!"


def test_profile_dict_max_avg():
    a = profile_dict()
    assert [True if a['max_year'] > a['avg_year'] else (True if a['max_mnt'] > a['avg_mnt'] else(
        True if a['max_day'] > a['avg_day'] else False))], "How can the max age be less than the average age!"


def test_profile_dict_out():
    a = profile_dict()
    assert len(a.keys()) >= 8, 'Insufficient number of outputs in your code!'


def test_profile_dict_neg():
    a = profile_dict()
    assert sum(number < 0 for number in [a['max_year'], a['max_mnt'], a['max_day'],
               a['avg_year'], a['avg_mnt'], a['avg_day']]) == 0, "Year/Month/Day cannot be negative"


def test_profile_dict_prnt_time():
    with Capturing() as output:
        profile_dict()
    assert any(["Time" in o for o in output]
               ), "How will you compare the time with the named tuple approach???"


def test_profile_dict_doc():
    assert profile_dict.__doc__, "Your function must have a docstring"


##########################################
############  Question 3 #################
##########################################
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def test_company_fn_cnt():
    a = company_fn()
    assert a['cmp_cnt'] == 100, "Number of companies must be 100!"


def test_company_fn_high_low():
    a = company_fn()
    assert a['stock_high'] >= a['stock_low'], "Stock High cannot be less than Stock Low"


def test_company_fn_high_open():
    a = company_fn()
    assert a['stock_high'] >= a['stock_open'], "Stock High cannot be less than Stock Open"


def test_company_fn_high_close():
    a = company_fn()
    assert a['stock_high'] >= a['stock_close'], "Stock High cannot be less than Stock Close"


def test_company_fn_var():
    a = company_fn()
    assert a['stock_high'] < 100 * a['stock_low'], "Stock cannot vary too much"


def test_company_fn_out():
    a = company_fn()
    assert len(a.keys()) >= 5, 'Insufficient number of outputs in your code!'


def test_company_fn_doc():
    a = company_fn()
    assert company_fn.__doc__, "Your function must have a docstring"


def test_company_fn_prnt_open():
    with Capturing() as output:
        company_fn()
    assert any(["Stock open" in o for o in output]
               ), "You must report the Stock Open"


def test_company_fn_prnt_high():
    with Capturing() as output:
        company_fn()
    assert any(["Stock high" in o for o in output]
               ), "You must report the Stock High"


def test_company_fn_prnt_end():
    with Capturing() as output:
        company_fn()
    assert any(["Stock close" in o for o in output]
               ), "You must report the Stock End"
