'''
Created on 2019年4月16日

@author: Administrator
'''
'''
User=[(22,'朱帅杰'),
      (21,'王'),
      (91,'India'),
      (55,'Brail'),
      (81,'Japan'),]
country_code={country:code for code,country in User}
print(country_code)
'''
'''
fruits=['red','yellow','black','blue','apple']

print(sorted(fruits,key = len))
'''

from dateutil.parser import parse
time = '20190702222135'
a = parse(time)# 根据字符串本身的格式进行转换
print(a)

# time.strftime('%Y-%m-%d-%H-%M')''




