import sys
# Prepend path so that AGS4.py is loaded from project file
# instead of current installation
sys.path.insert(0, '../')

from python_ags4 import AGS4, __version__
import toml


def test_version():
    pyproject = toml.load('../pyproject.toml')

    assert __version__ == pyproject['tool']['poetry']['version']


def test_AGS4_to_dict():
    tables, headings = AGS4.AGS4_to_dict('test_data.ags')

    assert tables['PROJ']['PROJ_ID'][2] == '123456'


def test_AGS4_to_dataframe():
    tables, headings = AGS4.AGS4_to_dataframe('test_data.ags')

    assert tables['LOCA'].loc[2, 'LOCA_ID'] == 'Location_1'


def test_convert_to_numeric():
    tables, headings = AGS4.AGS4_to_dataframe('test_data.ags')
    LOCA = AGS4.convert_to_numeric(tables['LOCA'])

    assert LOCA.loc[0, 'LOCA_NATE'] == 100000.01
    assert LOCA.loc[2, 'LOCA_NATN'] == 5000000.20
    assert LOCA.loc[3, 'LOCA_FDEP'] == 50.44


def test_dataframe_to_AGS4():
    tables, headings = AGS4.AGS4_to_dataframe('test_data.ags')

    AGS4.dataframe_to_AGS4(tables, headings, 'test.out')
    AGS4.dataframe_to_AGS4(tables, {}, 'test.out')


def test_convert_to_text():
    tables, headings = AGS4.AGS4_to_dataframe('test_data.ags')
    LOCA_num = AGS4.convert_to_numeric(tables['LOCA'])

    LOCA_txt = AGS4.convert_to_text(LOCA_num, 'DICT.ags')

    assert LOCA_txt.loc[0, 'LOCA_NATE'] == "100000.01"
    assert LOCA_txt.loc[2, 'LOCA_NATN'] == "5000000.20"
    assert LOCA_txt.loc[3, 'LOCA_FDEP'] == "50.44"