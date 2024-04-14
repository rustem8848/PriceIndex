#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from modeled_data.initial_dataset import InitialDataset
from modeled_data.statistic_data import StatisticData
from modeled_data.ml_model import MLModel

class WebsiteDataset:
    def __init__(self):
        self.__initial_df = ''
        self.__ml = ''
        self.__index_statistics = ''
        self.__ml_scores = ''
        self.__inflation_indexes = ''
        self.__confidence_intervals = ''
    
    def get_final_dataset(self):
        self.__get_initial_dataset()
        self.__get_statistic_data()
        self.__build_model()
        self.__get_ML_data()
        final_dataset = [
            self.__index_statistics,
            self.__ml_scores,
            self.__inflation_indexes,
            self.__confidence_intervals
        ]
        return final_dataset

    def __get_initial_dataset(self):
        url = "https://rosstat.gov.ru/storage/mediabank/ipc_mes_02-2024.xlsx"
        initial_dataset = InitialDataset(url)
        self.__initial_df = initial_dataset.get_df()
    
    def __get_statistic_data(self):
        statistic_data = StatisticData(self.__initial_df)
        self.__index_statistics = statistic_data.get_statistic_data()

    def __build_model(self):
        self.__ml = MLModel(self.__initial_df)
        self.__ml.build_model()

    def __get_ML_data(self):
        self.__inflation_indexes = self.__ml.get_all_series_with_predictions()
        self.__ml_scores = self.__ml.get_scores()
        self.__confidence_intervals = self.__ml.get_confidence_intervals()