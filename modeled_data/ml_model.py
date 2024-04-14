#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from datetime import datetime

class MLModel:
    def __init__(self, df):
        self.__df = df
        self.__series = ''
        self.__train = ''
        self.__test = ''
        self.__trained_model = ''
        self.__new_predictions = ''

    def build_model(self):
        self.__convert_to_series()
        self.__split_data()
        order = (1, 0, 1)
        seasonal_order = (1, 1, 1, 12)
        model = sm.tsa.SARIMAX(
            self.__train, order=order, seasonal_order=seasonal_order
        )
        self.__trained_model = model.fit(disp=False)

    def get_scores(self):
        return self.__calculate_accuracy(), self.__calculate_reliability_score()

    def get_all_series_with_predictions(self):
        self.__predict_data()
        return self.__add_predictions_to_series()

    def get_confidence_intervals(self):
        mean_ci_lower = self.__new_predictions['mean_ci_lower'].tolist()
        mean_ci_upper = self.__new_predictions['mean_ci_upper'].tolist()
        return [mean_ci_lower, mean_ci_upper]

    def __convert_to_series(self):
        transposed_df = self.__df.transpose()
        series = transposed_df.stack()
        new_index = series.index.map(
            lambda x: datetime.strptime(f'{x[0]}-{x[1]+1}', '%Y-%m')
        )
        series.index = new_index
        series.index.freq = 'MS'
        self.__series = series

    def __split_data(self):
        self.__train, self.__test = train_test_split(
            self.__series, test_size=0.2, shuffle=False
        )

    def __calculate_accuracy(self):
        test_predictions = self.__trained_model.predict(
            start=self.__test.index[0],
            end=self.__test.index[-1],
            dynamic=True
        )
        mae = mean_absolute_error(self.__test, test_predictions)
        rmse = np.sqrt(mean_squared_error(self.__test, test_predictions))
        return [mae, rmse]

    def __calculate_reliability_score(self):
        retro_scores = []
        for i in range(0, 5):
            start_index = len(self.__train) - 24 * (i + 1) - 1
            end_index = len(self.__train) - 24 * i - 1
            test_predictions = self.__trained_model.predict(
                start=start_index,
                end=end_index,
                dynamic=True
            )
            true_value = self.__train[start_index:end_index + 1]
            mae = mean_absolute_error(true_value, test_predictions)
            rmse = np.sqrt(mean_squared_error(true_value, test_predictions))
            retro_scores.append(
                [true_value.index[0].strftime('%Y-%m'),
                 true_value.index[-1].strftime('%Y-%m'),
                 round(mae, 2), round(rmse, 2)]
            )
        return retro_scores

    def __predict_data(self):
        start_index = self.__test.index[-1] + pd.DateOffset(months=1)
        end_index = start_index + pd.DateOffset(months=5)
        self.__new_predictions = self.__trained_model.get_prediction(
            start=start_index,
            end=end_index
        ).summary_frame(alpha=0.05)

    def __add_predictions_to_series(self):
        new_series = self.__new_predictions['mean']
        final_series = pd.concat([self.__series, new_series])
        final_series.rename(lambda x: x.strftime('%Y-%m'), inplace=True)
        final_series = final_series.apply(lambda x: round(x, 2))
        return final_series