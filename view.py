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
# orders=[]
# for item_master in item_masters:
#     orders.append(pos.Order(item_master))
# ordersにはOrderクラスが１つずつ入っている状態

order=pos.Order(item_masters)

@eel.expose
def add_order_list(item_code):
  
    item_infos= order.add_order_list(item_code)
    return f"商品コード{item_infos[0]}、商品名{item_infos[1]}、商品価格{item_infos[2]}円をカートに入れました"

    

desktop.start(app_name,end_point,size)

# if __name__ == "__main__":
#     main()
