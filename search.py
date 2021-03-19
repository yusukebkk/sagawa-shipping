import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(file_name,word):
    # 検索対象取得
    df=pd.read_csv(file_name)
    source=list(df["name"])

    # 検索
    if word in source:
        print(f"『{word}』はあります")
        log_message = f"『{word}』はあります\n"
    else:
        print(f"『{word}』はありません")
        log_message = f"『{word}』はありません\n"
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1#
        source.append(word)
        print(f"『{word}』が追加されました")
        log_message += f"『{word}』が追加されました\n"
            

            

        
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./source.csv",encoding="utf_8-sig")
    print(log_message)
    return log_message
