#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TableContent():
    def __init__(self):
        self.reliability_data = []

    def prepare_table_content(self, dataset):
        self.reliability_data = dataset[1][1]
        header = ['Начальная дата периода',
                  'Конечная дата периода', 
                  'Оценка MAE', 
                  'Оценка RMSE']
        self.reliability_data.insert(0, header)