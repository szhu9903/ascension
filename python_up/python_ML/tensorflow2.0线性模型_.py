import tensorflow as tf


X = tf.constant([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0]])
Y = tf.constant([[10.0],
                 [20.0]])

# 创建模型
class Linear(tf.keras.Model):
    def __init__(self):
        super(Linear, self).__init__()
        self.dense = tf.keras.layers.Dense(
            units = 1,
            activation = None,
            kernel_initializer = tf.zeros_initializer(),
            bias_initializer = tf.zeros_initializer()
        )

    def __call__(self, input):
        output = self.dense(input)
        return output
# 初始化模型
model = Linear()
# 创建梯度下降的优化器,学习速率0.01
optimizer = tf.optimizers.SGD(learning_rate=0.01)

for i in range(101):
    with tf.GradientTape() as tape:
        y_prae = model(X)
        # 获得损失函数 (10^2 + 20^2) / 2    250
        loss = tf.reduce_mean(tf.square(y_prae - Y))
    # 更新训练参数,
    grads = tape.gradient(loss, model.variables) # 计算loss 关于自变量variiable的导数
    # 自动根据梯度更新导数
    optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))
print(model.variables)

