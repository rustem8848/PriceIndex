#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pandas as pd

class InitialDataset:
    def __init__(self, url):
        self.__url = url
        self.__file_name = ''

    def get_df(self):
        self.__download_file()
        return self.__convert_to_df()

    def __download_file(self):
        self.__file_name = self.__url.split('/')[-1]
        with requests.get(self.__url, stream=True) as r:
            r.raise_for_status()
            with open(self.__file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

    def __convert_to_df(self):        
        excel_columns = 'B:AI'
        sheet_name = '01'
        df = pd.read_excel(
            self.__file_name,
            sheet_name=sheet_name,
            usecols=excel_columns,
            nrows=12,
            skiprows=[0, 1, 2, 4],
            header=0
        )
        return df