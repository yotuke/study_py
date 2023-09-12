"""
迭代器
    迭代是python最强大的功能之一，是访问集合的一种方式
    迭代器是一个对象，可以记住遍历位置的对象
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问结束
    迭代只能往前迭代不能后退
    迭代器有两个基本方法：iter()【创建】next()【迭代】
    字符串，列表，元组都可以用于创建迭代器
生成器
    使用了 yield 的函数被称为生成器 generator
    生成器的返回值是一个迭代器对象
    当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回

"""


# 迭代器实例
# list = [1, 2, 3, 4, 5]
# it = iter(list)  # 创建 list 的迭代器对象
# print(next(it))


# 如何创建一个迭代器类：把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
class MyIter:
    def __iter__(self):
        self.index = 1
        return self
        pass

    def __next__(self):
        if self.index <= 10:
            temp = self.index
            self.index = self.index + 1
            return temp
        else:
            raise StopIteration  # StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况
        pass

    pass


if __name__ == "__main__":
    myiter = iter(MyIter())
    for i in myiter:
        print(i)
