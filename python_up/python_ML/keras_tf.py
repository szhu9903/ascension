from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D

layer = [
    # 卷积层 filters:卷积核数目(输出的维度)
    Conv2D(filters=6, kernel_size=(5, 5), activation='relu', input_shape=(28, 28, 1)),
    # 池化层
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(filters=16, kernel_size=(5, 5), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    # 扁平化 在Lenet5中称为卷积，实际上这一层是一维向量，和全连接一样
    Flatten(),    # 输出维度120
    Dense(120, activation='relu'),
    # 全连接层 输出参数84个
    Dense(84, activation='relu'),
    # 输出层 用softmax激活函数计算分类概率
    Dense(10, activation='softmax')
]

# 创建模型
model = Sequential(layer)
#保存模型
# model.save('test_model.h5')
# 查看模型结构
print(model.summary())
