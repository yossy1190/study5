'''
クラスを記述する。

'''
import csv
import datetime
from imghdr import what
from pathlib import Path
import eel

### 商品クラス
class Item:

    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price

### オーダークラス
class Order:
    # item_mastersの中には、CSVで読み込んだ、code,name,priceが入る
    def __init__(self,item_masters):
        self.item_order_list=[]
        self.item_amount_list=[]
        self.item_masters=item_masters
        self.subtotal=0
        self.alltotal=0
        self.change_money=0
        self.pay_money=0
        self.change_money=0

    def add_order_list(self,item_code):
            for item_master in self.item_masters:
                # print(item_master.item_code,item_code)
                if int(item_code) == int(item_master.item_code):
                    return item_master.item_code,item_master.item_name,item_master.price    
            return None
                
                
            
    
    '''機能追加用メソッド  
    def fin_shop(self):
        
        self.pay_money=int(input(f"お会計は{int(self.alltotal):,}円です。預け入れ金額を入力してください(円不要)。>>>"))
        self.change_money=self.pay_money-int(self.alltotal)
        print(f"お支払いありがとうございます。お釣りは{self.change_money:,}円です。本日はご来店ありがとうございました!")
       
    '''
    '''機能追加用メソッド
    def print_receipt(self):
        payment_date=datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        
        with open("receipt.txt","w",encoding="utf-8") as f:
            f.write(f"来店日時:{payment_date}\n")
            l=len(self.item_order_list)
            for i in range(l):
                f.write(f"商品コード:{self.item_order_list[i]},商品名:{self.item_masters[i].item_name},価格:{self.item_masters[i].price}円,個数{self.item_amount_list[i]}個\n")
            f.write(f"合計金額:{int(self.alltotal):,}円\nお預かり金額:{int(self.pay_money):,}円\n")
            f.write(f"お釣り:{int(self.change_money):,}円\n")
            f.write("本日はご来店ありがとうございました！")
    '''   
