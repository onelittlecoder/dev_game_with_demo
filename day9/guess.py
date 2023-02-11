import random
people=[i  for i in '''
爸爸
猪八戒
熊大
灰姑娘
奥特曼
怪兽
大象
小鸟
乐迪
哪吒
刘备
'''.split("\n") if len(i)>0]

where=[i  for i in '''
飞机上
床底下
房顶上
厕所里
海底
垃圾桶里
月球上
松树上
梦中
沙发上
厨房里
'''.split("\n") if len(i)>0]

do_what=[i  for i in '''
玩玩具
上学
上厕所
打篮球
吃火锅
看电影
看书
喝水
跳绳
跳水
游泳
'''.split("\n") if len(i)>0]

array=[people,where,do_what]
def getRandom():
    return random.randint(0,10)
def generate():
    result=[]
    for i in range(3):
        n=getRandom()
        result.append(array[i][n])
    print(" ".join(result))
if __name__=="__main__":
    for i in range(50):
        print("===========================")
        generate()