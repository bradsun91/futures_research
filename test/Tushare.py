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
print(">>>>>>>>>>>>> 获取期货合约信息表")
print("接口：\tfut_basic\n描述:\t获取期货合约列表数据")
print("可选参数：")
print("\texchange\t|\tCFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心")
print("\tfut_type\t|\t合约类型 (1->普通合约; 2->主力与连续合约 默认取全部)")
pro = ts.pro_api(token)
futures_contract_DCE = pro.fut_basic(exchange='DCE', fut_type='1', fields='ts_code,symbol,name,list_date,delist_date')
## print out Futures Contract Data
print("\t|合约代码|交易标识|中文简称|上市日期|最后交易日期|")
print(futures_contract_DCE)

print(">>>>>>>>>>>>> 获取期货交易日历")
print("接口：\ttrade_cal\n描述:\t获取各大期货交易所交易日历数据")
print("可选参数：")
print("\texchange\t|\tCFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心")
print("\tstart_date\t|\t开始日期")
print("\tend_date\t|\t结束日期")
print("\tis_open\t\t|\t是否交易【0->休市; 1->交易】")
pro = ts.pro_api(token)
futures_trade_cal_DCE = pro.trade_cal(exchange = "DCE")
print("\t|交易所|日历日期|是否交易|")
print(futures_trade_cal_DCE)

print(">>>>>>>>>>>>> 获取期货日线行情")
print("接口：\tfut_daily\n描述:\t获取期货日线行情数据")
print("可选参数：")
print("\ttrade_date\t|\t交易日期")
print("\tts_code\t\t|\t合约代码")
print("\texchange\t|\tCFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心")
print("\tstart_date\t|\t开始日期")
print("\tend_date\t|\t结束日期")
pro = ts.pro_api(token)
futures_daily = pro.fut_daily(ts_code = "CU1811.SHF", start_date = "20180101", end_date = "20191231")
print("\t合约代码 | 交易日期 | 昨日收盘价 | 昨日结算价 | 开盘价 | 最高价 | 最低价|")
print(futures_daily)
print("   收盘价 | 结算价 | 收盘价-昨日结算价 | 结算价-昨日结算价 | 成交量 | 成交金额（万元）| 持仓量 | 持仓量变化 ")
