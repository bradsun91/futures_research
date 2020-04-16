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
daily_columns = "合约代码|交易日期|昨日收盘价|昨日结算价|开盘价|最高价|最低价|收盘价|结算价|收盘价-昨日结算价|结算价-昨日结算价|成交量|成交金额（万)|持仓量|持仓量变化".split("|")
for c in daily_columns: print("", c, end = "|")
futures_daily

print(">>>>>>>>>>>>> 获取每日成交持仓排名")
print("接口：\tfut_holding\n描述:\t获取每日成交持仓排名数据")
print("\ttrade_date\t|\t交易日期")
print("\tsymbol\t\t|\t合约或产品代码\t[注：（trade_date/symbol至少输入一个参数）]")
print("\texchange\t|\tCFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心")
print("\tstart_date\t|\t开始日期")
print("\tend_date\t|\t结束日期")
futures_hold = pro.fut_holding(trade_date = '20191231', symbol = "B")
print(f"共有{len(futures_hold)}条数据")
hold_columns = "交易日期|Symbol|期货公司会员简称|成交量|成交量变化|持买仓量|持买仓量变化|持卖仓量|持卖仓量变化".split("|")
for c in hold_columns: print("", c, end = " |")
futures_hold.head()

print(">>>>>>>>>>>>> 获取仓单日报")
print("接口：\tfut_wsr\n描述:\t获取仓单日报数据，了解各仓库/厂库的仓单变化")
print("\ttrade_date\t|\t交易日期")
print("\tsymbol\t\t|\t合约或产品代码")
print("\texchange\t|\tCFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心")
futures_wsr = pro.fut_wsr(trade_date ="20200214", exchange = "DCE")#symbol = "ZN")
wsr_columns = "交易日期|产品代码|产品名称|仓库名称|昨日仓单量|今日仓单量|增减量|单位".split("|")
for c in wsr_columns: print("", c, end = " |")
futures_wsr

print(">>>>>>>>>>>>> 获取结算参数")
print("接口：\tfut_settle\n描述:\t获取每日结算参数数据，包括交易和交割费率等")
print("\ttrade_date\t|\t交易日期")
print("\tts_code\t\t|\t合约代码")
print("\texchange\t|\tCFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心")
futures_settle = pro.fut_settle(trade_date = "20200213", exchange = "SHFE")
settle_columns = "合约代码|交易日期|结算价|交易手续费率|交易手续费|交割手续费率|买套保交易保证金率|卖套保交易保证金率|买投机保证金率|卖投机保证金率"
settle_columns = settle_columns.split("|")
for c in settle_columns: print("",c, end = " |") 
futures_settle

print(">>>>>>>>>>>>> 获取南华期货指数日线行情")
print("接口：\tindex_daily\n描述:\t获取南华指数每日行情，指数行情也可以通过通用行情接口获取数据．[https://tushare.pro/document/2?doc_id=109]")
print("\ttrade_date\t|\t交易日期")
print("\tts_code\t\t|\t合约代码")
futures_index_daily = pro.index_daily(ts_code = "CU.NH", start_date='20200101', end_date='20201201')
ind_dai_columns = "TS指数代码，交易日期，收盘点位，开盘点位，最高点位，最低点位，昨日收盘点，涨跌点，涨跌幅，成交量，成交额（千）".split("，")
for i in ind_dai_columns: print("", i, end = " |")
futures_index_daily

print(">>>>>>>>>>>>> 获取期货主力与连续合约")
print("接口：\tfut_mapping\n描述:\t获取期货主力（或连续）合约与月合约映射数据")
print("\ttrade_date\t|\t交易日期")
print("\tts_code\t\t|\t合约代码")
futures_mapping = pro.fut_mapping(ts_code = "TF.CFX")
mapping_columns = "连续合约代码。起始日期。期货合约代码".split("。")
for i in mapping_columns: print("", i, end = " |")
futures_mapping

print(">>>>>>>>>>>>> 获取期货主要品种交易周报")
print("接口：\tfut_weekly_detail\n描述:\t获取期货交易所主要品种每周交易统计信息，数据从2010年3月开始")
print("\tweek\t\t|\t周期（每年第几周，e.g. 202001 表示2020第1周）")
print("\tprd\t\t|\t期货品种（支持多品种输入，逗号分隔）")
print("\tstart_week\t|\t开始周期")
print("\tend_week\t|\t结束周期")
print("\texchange\t|\tCFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心")
print("\tfields\t\t|\t提取的字段，e.g. fields='prd,name,vol'")
all_columns = "exchange|prd|name|vol|vol_yoy|amount|amount_yoy|cumvol|cumvol_yoy|cumamt|cumamt_yoy|open_interest|interest_wow|mc_close|close_wow|week|week_date".split("|")
print("可选择输出：")
for c in range(len(all_columns)): print(f"{c}:{all_columns[c]}", end = " |")
futures_weekly_detail = pro.fut_weekly_detail(prd = "CU", start_week = "202001", end_week = "202003", fields = all_columns[:5])
futures_weekly_detail
