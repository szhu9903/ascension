
#使用python的list列表，实现堆栈
# Stack() 创建堆栈
# push(item) 向栈顶插入项
# pop() 返回栈顶的项，并从堆栈中删除该项
# clear() 清空堆栈
# empty() 判断堆栈是否为空
# size() 返回堆栈中项的个数
# top() 返回栈顶的项

class Stack():

	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)
	
	def pop(self):
		return self.items.pop()

	def clear(self):
		del  self.items[:]

	def empty(self):
		return self.size() == 0

	def size(self):
		return len(self.items)

	def top(self):
		return self.items[self.size()-1]