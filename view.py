'''
全体制御用 ステートフルな状態にする。このファイルでインスタンス化する。
item_masterもこちらで登録する。
'''

from os import system
import eel
import pandas as pd
from idna import valid_contextj
import desktop
import csv
import possystem as pos


app_name="html"
end_point="index.html"
size=(700,600)
df = pd.read_csv(r"item2.csv",encoding="Shift-JIS")

'''
マスタ登録
'''
items_in=[]
with open("item2.csv","r",encoding="Shift-JIS") as lists:
        header=next(csv.reader(lists))
        for list in csv.reader(lists):
            items_in.append(list)

item_masters=[]    
for item_in in items_in:
    item_masters.append(pos.Item(*item_in))
# item_mastersにはitemクラスが１つずつ入っている状態

'''
「カートに入れる」処理
'''
order=pos.Order(item_masters)
alltotal=0
subtotal=0

@eel.expose
def add_order_list(item_code,item_amount):
    # print(order.item_masters)
    item_infos= order.add_order_list(item_code)
    if item_infos:
        global alltotal
        global subtotal
        alltotal+=int(item_infos[2])*int(item_amount)
        subtotal=int(item_infos[2])*int(item_amount)
        return f"商品コード{item_infos[0]}、商品名{item_infos[1]}、商品価格{int(item_infos[2]):,}円、{item_amount}個をカートに入れました。小計:{subtotal:,}円 合計:{alltotal:,}円です。"
    else :
        return f"[エラー] 商品コード{item_code}が見つかりませんでした。"

'''
買物終了時の処理
'''
@eel.expose
def fin_shop():
    return f"お買上金額は、{alltotal:,}円です。\n支払金額スペースに金額を入力した後、「支払」ボタンを押してください。"


'''
金額支払時の処理
'''
@eel.expose
def cul_shop(depo_money):
    change_money=int(depo_money)-int(alltotal) 
    return f"お買上金額:{int(alltotal):,}円 お支払金額:{int(depo_money):,}円 お釣り:{int(change_money):,}円です。ご購入ありがとうございました。"

desktop.start(app_name,end_point,size)

# if __name__ == "__main__":
#     main()
