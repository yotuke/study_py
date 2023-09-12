"""
    python3 基本数据类型
        1.Number # 一旦初始化不可修改
            int
            float
            bool: 可参与数值计算，True代表1，False代表0
            complex
            数值计算：
                浮点数除法：  2 /  4
                整数除法：   2 // 4
                乘方：      2 ** 5
        2.String #  一旦初始化不可修改, 可看成一种特殊的Tuple
            String有两种截取方式：前面截取和后面截取
                语法：str[开始下标：截止下标]
                tips：字符串初始化后不可修改其中的某一个字符，即String是不可变的
        3.List 最常用
            list = [1, 2, 3, 4, 5]
        4.Tuple # 一旦初始化不可修改
            tuple = (1, 2, 3, 4, 5)
            tuple[1]
*****************************
        5.Set（集合）：一种无序、可变的数据类型，用于存储唯一的元素，集合中的元素唯一
            set01 = {1, 2 ,3 ,4, 5}
            set02 = set(1234)   #{1, 2, 3 ,4 ,5}
            set03 = set() # 空元组
        6.Dictionary（字典）：一种映射类型，用{}标识，是无序的key：value集合，key必须是不变类型（Number， String， Tuple）
            dict = { } # 空字典
"""


def fundamental_data_type():
    list = [1, 2, 3, 4, 5]
    print(type(list))

    tuple = (1, 2, 3, 4, 5)
    print(type(tuple))

    set01 = {1, 2, 3, 4, 4, 5}
    set02 = set([tuple])
    print(set01)
    print(set02)

    dict = {'name': 'apple', 'gender': 'male', 'age': 23}
    print(dict)


if __name__ == "__main__":
    fundamental_data_type()
