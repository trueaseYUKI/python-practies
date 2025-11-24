from typing import Optional

import pandas as pd
from pathlib import Path

from pandas import DataFrame


# 1.查看数据，了解数据结构
def load_data() -> Optional[DataFrame]:
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



    # 查看数值列的统计 describe()方法自动统计数值列，生成常用统计量: 包括计数、均值、标准差、最小值、四分位数、最大值等
    #print("\n查看数值列的统计：")
    #print(df.describe())

    return df


# 数据清洗
def clean_dataset(df:DataFrame) -> Optional[DataFrame]:
    """
    经过之前的查看，我们发现数据集出现了以下问题：
    1.Order Date/Ship Date 是object类型，但是我们要的datetime类型
    2.Postal Code 出现了 >80%缺省值，所以要丢弃

    :param df: DataFrame
    :return:
    """

    if df is None: return None

    # 输出头几个row
    #print("行结构如下：")
    #print(f"\n{df.head()}")
    # 1.先查看下一共有多少行
    columns, rows= df.shape

    print(f'\n列：{rows}，行：{columns}\n')

    # 输出每列类型
    print("\n每列类型如下：")
    print(df.dtypes)

    # 3.修改Order Date和Ship Date的类型为datetime
    # 以下转换会对错误格式直接抛出异常
    # df['Order Date'] = df['Order Date'].astype('datetime64[ns]')
    df['Order Date'] = pd.to_datetime(df['Order Date'],errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'],errors='coerce')




    # 2.检查是否有存在空（NaN、Null）
    nan_count = df.isna().sum()
    null_count = df.isnull().sum()


    # 如果有70%的列都为NaN或Null就直接删除该列
    for columns_name,count in nan_count.items():
        if count > (columns * 0.70):
            if columns_name in df.columns:
                # axis = 1 表示删除列，axis = 0 表示删除行，inplace表示直接在源数据集上进行修改不返回新的
                df.drop([columns_name], axis=1, inplace=True)
        else:
            # 使用向前填充的方式，使用前一个非空的值来填充
            df[columns_name] = df[columns_name].ffill()

    for columns_name,count in null_count.items():
        if count > (columns * 0.70):
            if columns_name in df.columns:
                # 防止重复删除
                df.drop([columns_name], axis=1, inplace=True)
        else:
            # 使用向前填充的方式，使用前一个非空的值来填充
            df[columns_name] = df[columns_name].ffill()



    print("\n(清洗后)每列类型如下：")
    print(df.dtypes)
    # 发现订单、产品同时重复的项目
    # 就是相同的订单，但是有买了相同的产品，那么就是一定是一个重复行
    grouped = df.groupby(['Order ID','Product ID']).size()
    # 找出分组中数量大于1的，就是重复的
    duplicate_combinations = grouped[grouped > 1]
    # print(f"\n重复订单的行数：\n{duplicate_combinations}")
    # 删除重复的购买订单
    # keep='first' 'first': 保留第一次出现的记录，删除后续重复记录 'last': 保留最后一次出现的记录 False: 删除所有重复记录（包括第一次出现的）
    df.drop_duplicates(['Order ID','Product ID'],keep='first',inplace=True)

    abnormal_date_count  = df[df['Order Date'] > df['Ship Date']].size
    if abnormal_date_count > 0:
        print('\n存在下单日期 > 发货日期的：')
        # 如果日期不正常的列小于0.01，那么我们就删除
        if abnormal_date_count < (rows * 0.01):
            df.drop(df[df['Order Date'] > df['Ship Date']].index,inplace=True)
        # 如果日期不正常的列大于0.01，那么我们就交换发货和下单日期
        else:
            # 找出所有 Order Date > Ship Date 的记录（通过 mask 筛选）
            mask = df['Order Date'] > df['Ship Date']
            # df.loc[]: pandas 的标签定位器，用于按标签选择数据
            # 将这些记录中的 Order Date 和 Ship Date 两列的值进行交换
            df.loc[mask, ['Order Date', 'Ship Date']] = df.loc[mask, ['Ship Date', 'Order Date']].values
            print("已调换异常日期")


    return df





def primary_analyzed_data(df:DataFrame):
    """
    对超市数据进行一定的pandos分析
    :param df:
    :return:
    """
    if df is None: return

    print(f'\n{df.head()}')
    # 了解数据的规模
    print(f"\n数据的列和行数量：{df.shape}")  # (行数, 列数)
    print(f"\n数值型的数据统计：\n{df.describe()}")
    print(f"\n片段唯一值的确认：\n{df['Segment'].nunique()}")
    print(f"\n查看一共有多少种类的产品：\n{df['Category'].unique()}")

    # 数据完整性检查
    print(f"\n数据是否任然有空：\n{df.isna().sum()}")
    print(f"\n数据是否任然有重复：\n{df.duplicated().sum()}")
    print(f"\n数据销售值是否异常：\n{df[df['Sales'] < 0]}")


    # 按产品分类进行统计
    category_summary = df.groupby(['Category','Sub-Category'])[['Sales','Profit']].sum()
    print(f"\n按产品分类进行销售额、利润统计：\n{category_summary}")

    # 按地区和客户类型分类统计
    region_segment_summary = df.groupby(['Region','Segment'])['Sales'].sum()
    print(f"\n按地区分类进行销售额、利润统计：\n{region_segment_summary}")


    pass

# 加载数据
date_frame = load_data()
# 清洗数据
clean_date_frame = clean_dataset(date_frame)
# 初步分析
primary_analyzed_data(clean_date_frame)