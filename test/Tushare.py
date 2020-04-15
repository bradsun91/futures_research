## set up the API
!pip install tushare
import tushare as ts
print(f"current version --> {ts.__version__}")
token = "8ef5ec61cdd848715c57c11d58dd71da1271f76b2420d2bac8aef123"

## import sample data from local
import os
#os.listdir()
import pandas as pd
futures_info = pd.read_excel("商品期货信息汇总.xlsx")
futures_info
## remove other columns for now
pd.Series(futures_info.columns)
drop_ind = [1,2,3,10, 14, 15, 19, 20, 21, 22, 23]
left = futures_info.columns[drop_ind]
## This dataframe showed me the content for each category of data
futures_info = futures_info.drop(columns = left)
## 查看交易所信息
futures_info['交易所'].unique()
## 查看交易商品名称
futures_info['品种'].unique()

## connect API
print("接口：\tfut_basic\n描述:\t获取期货合约列表数据")
print("可选参数：")
print("\texchange\t|\tCFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心")
print("\tfut_type\t|\t合约类型 (1->普通合约; 2->主力与连续合约 默认取全部)")
pro = ts.pro_api(token)
future_contract_DCE = pro.fut_basic(exchange='DCE', fut_type='1', fields='ts_code,symbol,name,list_date,delist_date')
## print out Futures Contract Data
print("|合约代码|交易标识|中文简称|上市日期|最后交易日期|")
print(future_contract_DCE)
