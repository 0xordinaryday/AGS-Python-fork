import pandas as pd
import json
import requests


def getgroupsandheadings(fpindex, version):
    """ Gets groupandheadings json data file from AGS gitlab repo
    Parameters:
    fpindex (str): fpath to the index file on the repo
    version (str): the version of the AGS4 release to be checked
    Returns:
    A dataframe of the groupandheadings dict
    """
    indexfile = requests.get(fpindex)
    data = json.loads(indexfile.text)
    files = data['files']
    for file in files:
        if version in file.values():
            fpath = file['groupsandheadings']
            df_groupsandheadings = pd.read_json(fpath, convert_dates=True)
            return df_groupsandheadings

indexfilepath = 'https://gitlab.com/AGS-DFWG-Web/ASG4/-/raw/298-create-an-index-file/ags-index-example.json'
dictversion = '4.1.0'
print(getgroupsandheadings(indexfilepath, dictversion))
