
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

salt = 'salesd'
serializer = Serializer(salt, expires_in=600)

info = {'username':'朱帅杰','age':2}

# 加密
res = serializer.dumps(info)
token = res.decode()
print(token)

res = serializer.loads(token)
print(res)