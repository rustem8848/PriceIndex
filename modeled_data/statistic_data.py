#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

class StatisticData:
    def __init__(self, df):
        self.__df = df
        self.__extremum_index = 0
        self.__columns_count = len(self.__df.columns)

    def get_statistic_data(self):
        return [self.__get_max(), self.__get_min(), self.__get_average()]

    def __get_max(self):
        extremum_value = np.nanmax(self.__df.to_numpy())
        self.__extremum_index = np.nanargmax(self.__df.values)
        return [extremum_value, self.__get_column(), self.__get_row()]

    def __get_min(self):
        extremum_value = np.nanmin(self.__df.to_numpy())
        self.__extremum_index = np.nanargmin(self.__df.values)
        return [extremum_value, self.__get_column(), self.__get_row()]

    def __get_column(self):
        column_index = self.__extremum_index % self.__columns_count
        column = self.__df.columns[column_index]
        return column

    def __get_row(self):
        rowIndex = self.__extremum_index // self.__columns_count
        row = self.__df.index[rowIndex] + 1
        return row

    def __get_average(self):
        mean = np.nanmean(self.__df.to_numpy())
        mean = round(mean, 2)
        return mean