from random import random 
from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure , curdoc

p = figure(x_range = (0,100) , y_range = (0 , 100))
result = p.text(x = [] , y = [] , text_color =[])
dataSource = result.data_source

button = Button(label = 'ثبت')

def clickOnSubmit():
    new_data = dict()
    new_data['x'] = dataSource.data['x'] + [random() * 70 + 15]
    new_dat['y'] = dataSource.data['y'] + [random() * 70 + 15]
    new_data['text'] = dataSource.data['text'] + [str(random())]
    dataSource.data = new_data


button.on_click(clickOnSubmit)

curdoc().add_root(column(button , p))
