from typing import Optional

import pandas as pd
from pathlib import Path

from pandas import DataFrame


# 1.查看数据，了解数据结构
def perceive_data() -> Optional[DataFrame]:
    """
    查看并理解数据
    :return:
    """
    # 1.加载csv文件数据
    csv_path = Path('./dataset/superstore_dataset2011-2015.csv')
    if not csv_path.exists():
        print("文件不存在")
        return None

    # 2.文件存在（该CSV文件编码为ISO-8859-1）
    df = pd.read_csv(csv_path,encoding="ISO-8859-1")
    # 显示显示所有列
    pd.set_option('display.max_columns',None)
    # 设置列宽
    pd.set_option('display.max_colwidth', None)


    # 输出头几个row
    print("行结构如下：")
    print(df.head())
    # 输出每列类型
    print("每列类型如下：")
    print(df.dtypes)
    # 查看行列数(51290行, 24列)
    print("\n行列数的如下：")
    print(df.shape)
    # 查看每一列的缺失值
    print("\n查看每一列的缺失值：")
    # isna = isNaN（为NaN就是True，不是就为False） sum()求NaN的总数
    print(df.isna().sum())
    print("\n查看每一列的缺失值：")
    print(df.isnull().sum())

    # 查看是否有重复的数据
    print('\n查看是否有重复的数据：')
    print(df.duplicated().sum())

    # 查看数值列的统计 describe()方法自动统计数值列，生成常用统计量: 包括计数、均值、标准差、最小值、四分位数、最大值等
    print("\n查看数值列的统计：")
    print(df.describe())

    return df

date_frame = perceive_data()

# 数据清洗
def clean_dataset(df:DataFrame):
    """
    经过之前的查看，我们发现数据集出现了以下问题：
    1.Order Date/Ship Date 是object类型，但是我们要的datetime类型
    2.Postal Code 出现了 >80%缺省值，所以要丢弃

    :param df: DataFrame
    :return:
    """
    # 1.删除Postal_Code列（由于我们统计数据不需要它）
    # axis = 1 表示删除列，axis = 0 表示删除行，inplace表示直接在源数据集上进行修改不返回新的
    df.drop(['Postal Code'],axis=1,inplace=True)

    # 2.修改Order Date和Ship Date的类型为datetime
    df['Order Date'] = df['Order Date'].astype('datetime64[ns]')
    df['Ship Date'] = df['Ship Date'].astype('datetime64[ns]')
    pass


# 清洗数据
clean_dataset(date_frame)