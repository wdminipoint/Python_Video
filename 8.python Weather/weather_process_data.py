'''
pandas 处理数据的一个神器

1. 处理天气的形势
2. 算每列的平均值
'''
import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Funnel,Pie,Page

'''
处理天气形势的
'''


def col_type(str):
    if '晴' in str:
        return '晴'
    elif '云' in str:
        return '云'
    elif '霾' in str:
        return '霾'
    elif '雨' in str:
        return '雨'
    elif '雪' in str:
        return '雪'


def col_Wd(str):

    sp = str.split('/')

    return (int(sp[0].replace('℃', '')) + int(sp[1].replace('℃', ''))) / 2

def funnel_base(data):

    c = (
        Funnel()
        .add("2019 年天气统计", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="019 年天气统计"))
    )

    c.render('./weather_funnel.html')

def pie_radius(data):
    c = (
        Pie()
        .add(
            "",
            data,
            radius=["40%", "75%"],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2019年天气统计数据"),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_top="15%", pos_left="2%"
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    c.render('./weather_pie.html')

if __name__ == '__main__':

    df = pd.read_csv('./weather.csv', header=None, names=['c_1', 'c_2', 'c_3', 'c_4', 'c_5'])

    df['c_6'] = df['c_2'].map(col_type)

    df['c_7'] = df['c_3'].map(col_Wd)

    df_echart = pd.value_counts(df['c_6'])

    df_echart = df_echart.reset_index()

    df_echart =df_echart.values.tolist()

    funnel_base(df_echart)

    pie_radius(df_echart)
    print(df_echart)


