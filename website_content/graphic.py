#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import Range1d

class Graphic():
    def __init__(self):
        self.script = ''
        self.div = ''
        self.__plot = ''
        self.__x = []
        self.__y = []
        self.__x_subset = []
        self.__y_subset = []
        self.__y_lower = []
        self.__y_upper = []

    def prepare_graphic(self, dataset):
        self.__get_xy(dataset)
        self.__prepapre_diagramm_area()
        self.__draw_main_line()
        self.__draw_prediction_line()
        self.__draw_confidence_area()
        self.script, self.div = components(self.__plot)

    def __get_xy(self, dataset):
        graphic_dataset = dataset[2]
        confidence_intervals = dataset[3]
        self.__x = graphic_dataset.index.to_list()[-24:]
        self.__y = graphic_dataset.to_list()[-24:]
        self.__x_subset = self.__x[-6:]
        self.__y_subset = self.__y[-6:]
        self.__y_lower = confidence_intervals[0]
        self.__y_upper = confidence_intervals[1]

    def __prepapre_diagramm_area(self):
        y_range = Range1d(start=99, end=102)
        self.__plot = figure(
            title='Предсказание ИПЦ',
            x_axis_label='месяцы',
            y_axis_label='ИПЦ',
            width=1200,
            x_range=self.__x,
            y_range=y_range
        )

    def __draw_main_line(self):
        self.__plot.line(
            self.__x, self.__y,
            legend_label='Ретроданные',
            line_width=2
        )

    def __draw_prediction_line(self):
        self.__plot.line(
            self.__x_subset, self.__y_subset,
            legend_label='Предсказание',
            line_width=2, line_color='red'
        )

    def __draw_confidence_area(self):
        self.__plot.varea(
            x=self.__x_subset, 
            y1=self.__y_lower, y2=self.__y_upper,
            legend_label='Доверительный интервал',
            fill_color='red', fill_alpha=0.2
        )