# coding:utf-8

"""
超市收银系统，模拟人人乐或华润万家的收银系统，具有会员积分功能，收费功能等
流程如下：
1. 输入会员卡号
2. 输入条码（商品类型）如白菜.苹果等及数量（斤或个）如2斤，显示相应的价格如：白菜 2斤 2.99元/斤，苹果 3斤5.99元/斤，
3. 输出每个商品各类的价值，如苹果15元，
4. 汇总应收款项，已付款项，找零款项，如应收43块，已收50块，找零7块，积分，
5. 下一位客户

数据流方式：每个商品有固定的条形码，使用dict数据类型
条形码-->商品名
商品名-->价格
商品名-->数量

界面：

会员名
-----------------
商品	单价	数量	总计
商品1	单价1	数量1	总计1
商品2	单价2	数量2	总计2
...
商品n	单价n	数量n	总计n
总计					xxxx						    
-----------------
已收：xxx
应收：xxx
找零：xxx



解决思路：定义3个类，超市（提供商品与价格）、售货员（计费与收费）、会员（挑选商品与付费）

"""

# 定义超市类，
# 具有属性值：商品与价格
# 具有方法：
class supermarket(object):
	def __init__(self):
		self.barcode_goods={
			"001":("apple","斤",5.99),
			"002":("banana","斤",3.99),
			"003":("watermelon","斤",1.98),
			"004":("cabbage","斤",1.99),
			"005":("meat","斤",32.99),
			"006":("ricce","斤",2.99)
			}


# 定义会员类
# 具有属性值：积分integral
# 具有方法：挑选、付款、获取积分		
class member (object):
	def __init__(self,integral):
		self.integral=0
		self.goods=[]
	
	def select(self):
		selectGood=input("Please select goods")
		
		while 
		self.goods.append(selectGood)
	
	def getIntegral(self):
		return self.integral
		
	def payment(self):
		pass
		
		
		
# 定义售货员类，
# 具有属性值：积分integral
# 具有方法：计费、收费
class salesperson(object):
	# 计费
	def chargeing(self):
		pass
	
	# 收费
	def charge(self):
		pass




		
	