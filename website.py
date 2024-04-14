#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from website_content.text_content import TextContent
from website_content.table_content import TableContent
from website_content.graphic import Graphic
from data_for_website import WebsiteDataset

app = Flask(__name__)

@app.route('/')
def index():
    show_content = False
    text_content = TextContent()
    table_content = TableContent()
    graphic = Graphic()
    
    if 'show_content' in request.args:
        show_content = True
        
        website_dataset = WebsiteDataset()
        final_dataset = website_dataset.get_final_dataset()
        text_content.prepare_text_content(final_dataset)
        table_content.prepare_table_content(final_dataset)
        graphic.prepare_graphic(final_dataset)

    return render_template(
        'index.html',
        show_content=show_content,
        script=graphic.script,
        div=graphic.div,
        max_value=text_content.max_value_message,
        min_value=text_content.min_value_message,
        average=text_content.average_message,
        accuracy=text_content.accuracy_message,
        table_data=table_content.reliability_data
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0')