from numpy import *
import numpy as np
from sklearn import linear_model
import numpy
from scipy.optimize import leastsq
import pylab
from scipy import stats
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import operator

from pandas import Series,DataFrame
outputfile="d:/a.xls"
def isString(obj):
     try:
         obj.lower() + obj.title() + obj + ""
     except:
         return False
     else:
         return True

list1=[11,5,43,1,26,68,98]
list2=[11,23,-1,35,76,48,44]
list23=[32,77,45,45,26,43,54]
def first(data,name):
    result=[]
    for l in range(len(data)):
        data[l]=[x[1] for x in data[l]]
        # print(l)
        # counts=np.bincount(l)
        l1=sort(data[l])
        len_l=len(data[l])
        result.append([name[l]])
        # result.append([['长度',len(l)],['最大值',max(l)],['平均值',mean(l)],['最小值',min(l)],['方差',np.var(l)],['标准差',np.std(l,ddof=1)],['中值',np.median(l)],['1/4值',l1[len_l//4]],['3/4值',l1[len_l-len_l//4]]])
        result.append(['数据数量','最大值','平均值','最小值','方差','标准差','中值','1/4值','3/4值'])
        result.append([len(data[l]),max(data[l]),mean(data[l]),min(data[l]),np.var(data[l]),np.std,np.median(data[l]),l1[len_l//4],l1[len_l-len_l//4]])
    # print(result)
    return result

def second(l1,l2):
    model = linear_model.LinearRegression()
    list_1=[]
    list_2=[]
    for i in l1:
        list_1.append([i])
    for i in l2:
        list_2.append([i])
    model.fit(list_1,list_2 )
    l=[]
    for i in range(len(l1)):
        l.append([l1[i],l1[i]*model.coef_[0][0]+model.intercept_[0]])
    result=[]
    result.append(['截距','斜率','残差'])
    result.append([model.intercept_[0],model.coef_[0][0],np.mean((model.predict(list_1) - list_2) ** 2)])
    return result,l

def third(arrayX, arrayY,X):
    if len(arrayY) == 0:
        return [0, 0, 0]
    x = numpy.array(arrayX)
    y = numpy.array(arrayY)
    z = numpy.polyfit(x, y, X)
    p = numpy.poly1d(z)
    r=''
    for i in range(len(z)):
       r=r+str(z[len(z)-i-1])+"x^"+str(i)+"# "
    l = []
    for i in range(len(arrayX)):
        tmp=0;
        for j in range(len(z)):
            tmp=tmp+arrayX[i]**j*z[len(z)-j-1]
        l.append([arrayX[i], tmp])
    return [['方程'],[r]],l
def forth(l1,l2,max_period):
    period=0;
    error=100000;
    for i in range(max_period):
        model = linear_model.LinearRegression()
        list_1 = []
        list_2 = []
        for j in range(i,len(l1)):
            list_1.append([l1[j]])
        for j in range(0,len(l2)-i):
            list_2.append([l2[j]])
        model.fit(list_1, list_2)
        tmp_c=np.mean((model.predict(list_1) - list_2) ** 2)
        if tmp_c<error:
            error=tmp_c;
            period=i
    for i in range(max_period):
        model = linear_model.LinearRegression()
        list_1 = []
        list_2 = []
        for j in range(i,len(l2)):
            list_1.append([l2[j]])
        for j in range(0,len(l1)-i):
            list_2.append([l1[j]])
        model.fit(list_1, list_2)
        tmp_c=np.mean((model.predict(list_1) - list_2) ** 2)
        if tmp_c<error:
            error=tmp_c;
            period=i
    return [['偏移时间'],[period]]
def fifth(l,n):
    X = np.array(l)
    if isString(n):
        pca = PCA(n_components=n)
    else:
        pca = PCA(n)
    pca.fit(X)
    result=[[]]
    low_d = pca.transform(X)  # 降低维度
    for i in range(n):
        result[0].append('第' + str(i + 1) + '个')
    for j in range(len(low_d)):
        result.append(low_d[j].tolist())

    print(result)
    return result
def sixth(l,name):
    X = np.array(l)
    pca = PCA()  # 保留所有成分
    pca.fit(X)
    result=[[],[]]
    tmp=pca.explained_variance_ratio_
    for i in range(len(tmp)):
        result[0].append(name[i])
        result[1].append(tmp[i])
    # print(pca.explained_variance_ratio_)
    return result
def seventh(l):
    index = np.argsort(l[0], 0)[:, 1]
    tmp_data=[]
    x=[]
    y=[]
    for i in index:
        x.append(l[0][i][0])
        y.append(l[0][i][1])
    tmp_data.append(x)
    tmp_data.append(y)
    tmp_l=[]
    for i in l[0]:
        tmp_l.append(i[1])
    # foreset=sorted(l)
    skew = stats.skew(tmp_l)  # 求偏度
    kurtosis = stats.kurtosis(tmp_l)  # 求峰度
    result=[]
    result.append(['偏度','峰度'])
    result.append([skew,kurtosis])
    return result,tmp_data
def eighth(l,n):
    kmeans = KMeans(n_clusters=n)  # n_clusters:number of cluster
    new_list = [[n[i] for n in l] for i in range(len(l[0]))]
    print(new_list)
    x=np.array(new_list)
    print(x)
    kmeans.fit(x)
    print(kmeans.labels_)
def ninth(data,n):
    tmp_month=[]
    tmp_data=[]
    for i in data[0]:
        tmp_month.append(i[0])
        tmp_data.append(i[1])
    m=mean(tmp_data)
    s=np.std(tmp_data)
    leng=len(tmp_data)
    tmp_num=0
    n=double(n)
    data_show=[]
    x=[]
    y=[]
    for i in range(len(tmp_data)):
        # print(tmp_data[i])
        if tmp_data[i]<m+n*s and tmp_data[i]>m-n*s:
            tmp_num=tmp_num+1
        else:
            x.append(tmp_month[i])
            y.append(tmp_data[i])
    data_show.append(x)
    data_show.append(y)
    return [['在标准差内的比例'],[tmp_num/leng]],data_show
def tenth(l,name):
    t=[]
    for i in l:
        t.append([])
    for i in range(len(l[0])):
        tmp=[]
        for j in range(len(l)):
            t[j].append(l[j][i][1])
        # a=pd.Series(tmp)
        # t.append(tmp)
    for i in range(len(l)):
        tmp=0
        for j in range(len(t[i])):
            if t[i][j-tmp]==-1000:
                for k in range(len(l)):
                   del t[k][j-tmp]
                tmp=tmp+1
    # print(t)
    # x = np.vstack(t)
    r = np.corrcoef(t)
    print(r)
    result=[['皮尔逊系数']]
    tmp=[]
    for i in name:
        tmp.append(i)
    result.append(tmp)
    for i in range(len(r)):
        tmp=r[i].tolist()
        result.append(tmp)
        result[2+i].append(name[i])
    print(result)
    return result

def qu_chong(l,default):
    result=[]
    for j in range(len(l)):
        result.append([])
    for i in range(len(l[0])):
        ifn=1
        for j in range(len(l)):
            if l[j][i][1]==default:
                ifn=0
        if ifn==1:
            for j in range(len(l)):
                result[j].append(l[j][i][1])
    return result
def clean_first(l1,l2,default):
    if len(l1)!=len(l2):
        return "两列表不相等"
    else:
        c_f_list1 = []
        c_f_list2 = []
        for i in range(len(l1)):
            if l1[i][1]==default or l2[i][1]==default:
                continue
            else:
                c_f_list1.append(l1[i][1])
                c_f_list2.append(l2[i][1])
        return c_f_list1,c_f_list2
def clean_second(l):
    tmp_list=[]
    tmp_max=max(l)
    tmp_min=min(l)
    tmp_inter=tmp_max-tmp_min
    for i in l:
        tmp_list.append((i-tmp_min)/(tmp_inter))
    return tmp_list
def clean_third(l):
    mean_l=mean(l)
    std_l=std(l)
    for i in range(len(l)):
        l[i]=(l[i]-mean_l)/std_l
    return l
def clean_forth(l):
    mean_l=mean(l)
    sf=0
    for i in l:
        sf=sf+abs(i-mean_l)
    sf=sf/len(l)
    for i in range(len(l)):
        l[i]=(l[i]-mean_l)/sf
    return l

def first_11(l,para):
    sorted_ = np.sort(l)
    yvals = np.arange(len(sorted_)) / float(len(sorted_))
    if para==[]:
        x_label = stats.norm.ppf(yvals)  # 对目标累计分布函数值求标准正太分布累计分布函数的逆
    elif para==['lognormal']:
        x_label = stats.lognorm.ppf(yvals,.7)
    else:
        x_label = stats.norm.ppf(yvals)
    print(para)
    return x_label[1:],sorted_[1:]

def dele_none(l):
    # print(l)
    for i in range(len(l)):
        tmp_num=0
        for j in range(len(l[i])):
            if l[i][j-tmp_num][1]==-1000.0:
                del l[i][j-tmp_num]
                tmp_num=tmp_num+1
    # print(l)
    return l

# if __name__ == '__main__':
#     l=[[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
#     l=[]
#     l.append(list1)
#     l.append(list2)
#     l.append(list23)
#     print(first_11(list1))
#         # print(f"growth = {growth}, maxSale = {maxSale}")


