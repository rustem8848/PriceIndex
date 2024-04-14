#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TextContent():
    def __init__(self):
        self.__dataset = ''
        self.max_value_message = ''
        self.min_value_message = ''
        self.average_message = ''
        self.accuracy_message = ''

    def prepare_text_content(self, dataset):
        self.__dataset = dataset
        self.__get_max_value_message()
        self.__get_min_value_message()
        self.__get_average_message()
        self.__get_accuracy_message()
        
    def __get_max_value_message(self):
        max_value = self.__dataset[0][0]
        self.max_value_message = (
            f'''Максимальное значение ИПЦ было на 
            {max_value[1]}-{str(max_value[2]).zfill(2)}  {max_value[0]}%'''
        )

    def __get_min_value_message(self):
        min_value = self.__dataset[0][1]
        self.min_value_message = (
            f'''Минимальное значение ИПЦ было на 
            {min_value[1]}-{str(min_value[2]).zfill(2)}  {min_value[0]}%'''
        )

    def __get_average_message(self):
        average = self.__dataset[0][2]
        self.average_message = (
            f'''Среднее значение ИПЦ в наблюдаемом периоде {average}%'''
        )

    def __get_accuracy_message(self):
        accuracy = self.__dataset[1][0]
        self.accuracy_message = (
            f'''Индексы точности модели на тестовых данных mae: 
            {round(accuracy[0],2)}; rmse: {round(accuracy[1],2)}'''
        )