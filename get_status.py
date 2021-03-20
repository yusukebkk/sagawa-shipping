import eel
import os
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import sys

# Chromeを起動する関数



def set_driver(headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    #return Chrome(executable_path=os.getcwd() + "/" + driver_path, options=options)
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)

#logの処理
def add_log(message):
    with open("log.txt", mode='a') as f:
        f.write(message+"\n")


# main処理
def main(path):
    # driverを起動
    driver = set_driver(False)
    try:
        df = pd.read_excel(path,dtype={1: str,2:str})
        eel.view_log_js("ファイルの読み込みが完了しました")
    except:
        eel.view_log_js("ファイルの読み込みに失敗しました")
        driver.quit()
        return 1

        
    #データの長さを取得
    data_length = len(df.index)
    print(data_length)
    #10件ずつ分けたら何回取得が必要か
    get_data_times = (data_length-1)//10 +1
    #10件ずつ処理を行う
    for i in range (get_data_times):
        driver.get("https://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp")
        time.sleep(5)
        data = df.iloc[i*10:i*10+10,1].tolist()
        #値の入力
        for j in range (len(data)):
            xpath = "//input[@tabindex="+str(j+1)+"]"
            driver.find_element_by_xpath(xpath).send_keys(data[j])

        #送信
        driver.find_element_by_id("main:toiStart").click()
        time.sleep(5)
        #結果取得
        elements = driver.find_elements_by_xpath('//td[@colspan=3]')
        count = 0
        #データの更新
        for element in elements:
            count += 1
            eel.view_log_js(f"{i*10+count}件目が完了しました。")
            df.iat[i*10+count-1,2]=element.text
    
    
    #エクセルへの出力
    df.to_excel(path,index=False)
    eel.view_log_js("ファイルの出力が完了しました")
    #ドライバーを閉じる
    driver.quit()


        
            

            

 



    
    
 

#直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
