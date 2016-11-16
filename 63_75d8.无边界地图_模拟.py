#!/usr/bin/python
# coding: utf-8

# 跑了 1 分钟 结构式 800+ 次迭代

# 维基百科:生命游戏 https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# 题目地址: http://www.qlcoder.com/task/75d8

# 生命游戏是一个经典的在二维地图上模拟生物演化的简单的小游戏。
# 在一个无边界的地图上，黄色代表生命体，灰色代表空地。初始状态如下图所示。

# 他的规则非常简单。 在每次演化中:

# 如果一个生命体周围少于2生命体，那么该生命体会因为人口缺少而在下一轮死去，这个格子变成了空地。
# 如果一个生命体周围大于3个生命体，那么该生命体会因为人口的过度拥挤，资源匮乏，而在下一轮死去。这个格子变成空地。
# 如果一个生命体周围有2-3个生命体，那么该生命体能在下一轮继续活下去。
# 如果一个空地周围有3个生命体，那么该空地在下一轮会繁殖出新的生命体。
# 为了方便大家理解，在迭代了1轮之后，地图变成如下所示:

# 在一个无边界的地图上，一个生命游戏的起始状态如上图所示（初始有5个生命体，剩下的都是空地），
# 我想知道在接下来的无数次演化中，人口最多的时候，有多少个人口，最早发生在哪次迭代。
# 答案格式:"a-b"(迭代次数-人口数）。 在第1次迭代后，人口数变成6，那么提交的答案可以是 "1-6"。

SIZE = 8


class Tail:
    '''
    组成地图的最小单位，8x8
    '''

    def __init__(self, x, y, map, data=None):
        self.map = map
        self.block_x = x
        self.block_y = y

        num = 0
        if data is None:
            data = [[0 for i in range(SIZE)] for j in range(SIZE)]
        else:
            for a in range(SIZE):
                for b in range(SIZE):
                    num += data[a][b]

        self.data = data
        self.num = num

    def __repr__(self):
        data = self.data
        return '\n{}_{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
            self.block_x, self.block_y,
            self.data[0], self.data[1], self.data[2], self.data[3],
            self.data[4], self.data[5], self.data[6], self.data[7])

    def neighber(self, block_offset_x, block_offset_y):
        return self.map.get(self.block_x + block_offset_x, self.block_y + block_offset_y)

    def get(self, x, y):
        if x // SIZE == 0 and y // SIZE == 0:
            return self.data[y][x]
        else:
            tartail = self.neighber(x // SIZE, y // SIZE)
            if tartail:
                return tartail.data[y % SIZE][x % SIZE]
            else:
                return 0

    def calc_one(self, x, y):
        temp = self.get(x - 1, y - 1) + self.get(x - 1, y) + self.get(x - 1, y + 1) + \
            self.get(x, y - 1) + self.get(x, y + 1) + \
            self.get(x + 1, y - 1) + self.get(x + 1, y) + \
            self.get(x + 1, y + 1)

        # print('{}, {} = {} -- {}'.format(x, y, self.get(x, y), temp))
        if temp < 2 or temp > 3:
            return 0, temp
        elif 3 == temp:
            return 1, temp
        else:
            return self.get(x, y), temp

    def calc_to_cache(self):
        '''
        计算生命的存亡变化并放入缓存
        '''
        cache = [[0 for i in range(SIZE)] for j in range(SIZE)]
        num = 0
        data = self.data
        for x in range(SIZE):
            for y in range(SIZE):
                result, temp = self.calc_one(x, y)

                if result != data[y][x]:
                    print('{} {} {} {}'.format(x, y, result, temp))

                cache[y][x] = result
                num += result

        self.cache = cache
        self.cachenum = num

    def check_empty_neighber(self):
        '检查是否影响了邻近的空地块'
        def check(block_offset_x, block_offset_y):
            if self.neighber(block_offset_x, block_offset_y) is None:
                for i in range(SIZE):
                    x = y = i
                    if block_offset_x == 1:
                        x = SIZE
                    elif block_offset_x == -1:
                        x = -1
                    if block_offset_y == 1:
                        y = SIZE
                    elif block_offset_y == -1:
                        y = -1
                    result, temp = self.calc_one(x, y)
                    if result:
                        print('于{}, {}处诞生了生命，{}'.format(x, y, temp))
                        self.map.append(self.block_x + block_offset_x,
                                        self.block_y + block_offset_y)
                        break

        check(-1, 0)
        check(1, 0)
        check(0, -1)
        check(0, 1)

    def apply_cache(self):
        '应用缓存'
        self.data = self.cache
        self.num = self.cachenum
        self.cache = None


class Map():
    '''
    地图。
    地图支持负坐标。支持自动扩容。支持查找地块
    '''

    def __init__(self):
        self.tails = {}

    def put(self, t):
        key = '{}_{}'.format(t.block_x, t.block_y)
        self.tails[key] = t
        # print('加入了地块\n{}'.format(t))

    def get(self, x, y):
        return self.tails.get('{}_{}'.format(x, y))

    def delete(self, t):
        key = '{}_{}'.format(t.block_x, t.block_y)
        del self.tails[key]

    def append(self, x, y):
        '追加一些空地块'
        tail = Tail(x, y, self)
        self.put(tail)
        self.to_append.append(tail)
        print('追加空地块{}, {}'.format(tail.block_x, tail.block_y))

    def calc(self):

        # print(self.tails)
        # print('!!!!!!!!!!!!!!!!!!!!!!!!!')

        self.to_append = []
        items = [x for x in self.tails.items()]
        for (k, tail) in items:
            tail.calc_to_cache()
            tail.check_empty_neighber()

        for tail in self.to_append:
            tail.calc_to_cache()

        num = 0
        length = 0
        items = [x for x in self.tails.items()]
        for (k, tail) in items:
            tail.apply_cache()
            # print('处理地块{},{}，生命数{}'.format(tail.block_x, tail.block_y, tail.num))
            if tail.num == 0:
                self.delete(tail)
                # print('删除了该地块')
            else:
                length += 1
                num += tail.num
        print('length = {}'.format(length))
        return num, length

data = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

m = Map()
t = Tail(0, 0, m, data)

m.put(t)

maxnum = 0
maxtime = 0
for i in range(1, 9999):
    print('===================================')
    num, length = m.calc()
    print('第{}轮计算完成：{}个生命，{}个地块'.format(i, num, length))
    if num > maxnum:
        print('创造了新纪录！{}'.format(num))
        maxnum = num
        maxtime = i
    else:
        print('当前记录是{}轮创造的{}'.format(maxtime, maxnum))
