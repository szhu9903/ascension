
import pandas as pd
import numpy as np


# pd 逐行、逐列、逐个操作数据 map、apply、applymap
class pdApply(object):
    def __init__(self):
        self.pd_data = self.generate_data()

    # 生成测试数据
    def generate_data(self):
        boolean = [True, False]
        gender = ["MAN", "WOMAN"]
        color = ["black", "blue", "yellow"]
        data = pd.DataFrame({
            "height": np.random.randint(160, 190, 100),
            "weight": np.random.randint(80, 160, 100),
            "smoker": [boolean[i] for i in np.random.randint(0, 2, 100)],
            "gender": [gender[i] for i in np.random.randint(0, 2, 100)],
            "age": np.random.randint(20, 80, 100),
            "color": [color[i] for i in np.random.randint(0, len(color), 100)]
        })
        return data

    def serice_map(self):
        # 字典映射方式
        self.pd_data["color_ch"] = self.pd_data["color"].map({"yellow":"黄", "black":"黑", "blue":"蓝"})
        # 函数方式
        self.pd_data["gender_ch"] = self.pd_data["gender"].map(lambda x:'男' if x == 'MAN' else '女')
        # 生成汇总行
        self.pd_data.loc[100] = {
            "height": self.pd_data["height"].mean(),
            "weight": self.pd_data["weight"].mean(),
            "age": self.pd_data["age"].mean(),
        }

        return self.pd_data


if __name__ == '__main__':

    pd_data = pdApply()
    print(pd_data.serice_map())