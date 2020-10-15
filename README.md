# 虛擬貨幣定期定額投資計畫

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ClarkChiu/MAX-Exchange-Periodic-Crypto-Investment-Plan.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ClarkChiu/MAX-Exchange-Periodic-Crypto-Investment-Plan/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ClarkChiu/MAX-Exchange-Periodic-Crypto-Investment-Plan.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ClarkChiu/MAX-Exchange-Periodic-Crypto-Investment-Plan/alerts/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)


## 當一個好 HODLer，不好嗎？

![Hodl Meaning foto](https://en.bitcoinwiki.org/upload/en/images/thumb/d/db/HODLing.jpg/400px-HODLing.jpg)

圖片來源：[BitcoinWiki](https://en.bitcoinwiki.org/)



## 簡介

你也想成為虛擬貨幣定期定額的 HODL 囤幣族嗎，來來來，趕緊使用此專案定期定額在 [MAX - 數位資產交易所](https://max.maicoin.com/) 購買虛擬貨幣，給你一個美夢。



## MAX 交易所 API 設定及取得方式

請參見 [MAX 交易所 API 文件](https://max.maicoin.com/documents/api) 



## 使用說明

1. git clone https://github.com/ClarkChiu/MAX-Exchange-Periodic-Crypto-Investment-Plan
2. cd MAX-Exchange-Periodic-Crypto-Investment-Plan/
3. git submodule init
4. git submodule update
5. python3 -m venv .venv
6. source .venv/bin/activate
7. pip install -r requirements.txt
8. cp .env-sample .env
9. vim .env
10. python max_invest_bot/bot.py



## 使用說明（文字版本）

1. 假設您擁有一個可執行 Python3 之環境（可能是您家中永不關機的電腦、Google Cloud Platform (GCP)、Amazon Web Services (AWS) 或是較進階的 GitHub Actions）

2. 設定好 .env 檔案（請參考 [.env-sample](https://github.com/ClarkChiu/MAX-Exchange-Periodic-Crypto-Investment-Plan/blob/master/.env-sample)）

3. 使用 Cron 定期呼叫本專案之程式（請注意需切換至專案路徑），例如每隔 3 天執行之 crontab 設定如下（可使用 [Crontab.guru](https://crontab.guru/) 服務幫您做好正確的設定）

   `0 0 */3 * * cd /home/clark/MAX-Exchange-Periodic-Crypto-Investment-Plan/; ./.venv/bin/python ./max_invest_bot/bot.py`
   
   

## 程式流程

1. 程式執行時讀取您所設定在 .env 中的相關設定
2. 執行下單動作



## .env 設定說明

1. API_KEY：MAX 交易所提供之金鑰
2. SECRET_KEY：MAX 交易所提供之金鑰
3. PAIR：目標交易對（例如：ethusdt）
4. AMOUNT：單次下單數量（例如：0.05）



單次下單數量有最小限制，請見  [MAX 下單限制](https://max.maicoin.com/docs/limits)



## 聲明

1. 世界上任何正當投資都具有投資風險，此一風險可能使本金發生虧損，投資人須自負盈虧。
2. 本人與 MAX 交易所無任何關聯，此專案單純為推廣虛擬貨幣以及 HODL，相同之程式邏輯亦可套用於任何虛擬貨幣交易所。 
