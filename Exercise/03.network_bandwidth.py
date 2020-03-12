# 网络带宽计算
bandwidth=input('请输入您的网络带宽,单位为M\r\n')
print('你输入的网络带宽为 ',bandwidth,'M')
bandwidth=int(bandwidth)
if bandwidth<=0:
    print('请输入正数值')
    exit()
print('经过计算得到，您的网络带宽为：',bandwidth/8)