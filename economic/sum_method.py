from economic.defff import *
#first是用来计算common
#dele_none去除列表中的空值
#clean_first去掉两个列表都没有的部分
#second一次回归d

def common(data,para,name):
    # print(data)
    data = dele_none(data)
    data_show=[]
    for i in data:
        tmp_x = []
        tmp_y = []
        for j in i:
            tmp_x.append(j[0])
            if j[1]!=-1000.0:
                tmp_y.append(j[1])
            else:
                tmp_y.append('')
        tmp_y=Reverse(tmp_y)
        tmp_x=Reverse(tmp_x)
        data_show.append([tmp_x,tmp_y])

    result =first(data,name)
    return result,data_show,[[]],'category',[[]],[['选择数据散点图']]

def Reverse(lst):
    return [ele for ele in reversed(lst)]

def one_regression(data,para,name):
    data1,data2=clean_first(data[0],data[1],-1000.0)
    # print(data1)
    result,re_line=second(data1,data2)
    data=two_duo(data1,data2)
    return result,[['',data]],re_line,'value',[[]],[['二维坐标图，横轴为选择第一列数据，纵轴为第二列数据']]

def two_duo(d1,d2):
    d=[]
    for i in range(len(d1)):
        d.append([d1[i],d2[i]])
    return d

def mul_regression(data,para,name):
    data1, data2 = clean_first(data[0], data[1], -1000.0)
    # print(data1)
    if para:
        result, re_line = third(data1, data2,int(para[0]))
    else:
        result, re_line = third(data1, data2,2)
    data = two_duo(data1, data2)
    re_line=sorted(re_line)
    return result, [['', data]], re_line, 'value',[['几次方',[1,2,3,4,5,6]]],[['二维坐标图，横轴为选择第一列数据，纵轴为第二列数据']]

def pierxun(data,para,name):
    data1, data2 = clean_first(data[0], data[1], -1000.0)
    result=tenth(data,name)
    data = two_duo(data1, data2)
    return result, [[]], [[]], 'value', [[]],[[]]

def qq_chart(data,para,name):
    data = dele_none(data)
    tmp_data=[]
    for i in data[0]:
        tmp_data.append(i[1])
    data=clean_second(tmp_data)
    x,y=first_11(data,para)
    min_y=min(x)
    max_y=max(x)
    data=two_duo(x, y)
    return [[]], [['', data]], [[min_y,min_y],[max_y,max_y]], 'value', [['什么分布',['lognormal','normal']]],[['正太分布数据与选中数据比较qq图']]

def normal_ratio(data,para,name):
    if len(para)==0:
        para.append(1)
    data=dele_none(data)
    result,data=ninth(data,para[0])
    return result, [data], [[]], 'category',[['几倍标准差',[0.5,1,2,3,4,5,6]]],[['数据展示图']]

def sort_show(data,para,name):
    data = dele_none(data)
    result,data=seventh(data)
    return result, [data], [[]], 'category', [[]],[['正序排列之后的图']]

def pipei_mum(data,para,name):
    data1, data2 = clean_first(data[0], data[1], -1000.0)
    result=forth(data1,data2,4)
    data = two_duo(data1, data2)
    return result, [['', data]], [[]], 'value', [[]],[['二维坐标图，横轴为选择第一列数据，纵轴为第二列数据']]

def gongxian(data,para,name):
    data=qu_chong(data,para)
    result=sixth(data,name)
    return result, [['', []]], [[]], 'value', [[]]

def zhuchengfen(data,para,name):
    if len(para)==0:
        para.append(2)
    data=qu_chong(data,-1000)
    result=fifth(data,int(para[0]))
    tmp_choose=[]
    for i in range(len(data)):
        tmp_choose.append(i+1)
    return result, [[[], []]], [[]], 'value', [['几组数据',tmp_choose]]