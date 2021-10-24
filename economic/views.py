#启动为e：win/echosite -config=config.yml start-all

from django.shortcuts import render
from django.http import FileResponse
from economic.sum_method import *
from economic.models import *
import xlwt
import json
from decimal import Decimal

import re
import economic.models
from django.shortcuts import HttpResponse
# Create your views here.
def main(request):#首页
    id='about'
    return render(request, 'Tempo Bootstrap Template - Index.html',{'id':id})
def pro_main(request):#首页
    id='about'
    return render(request, 'main.html',{'id':id})

def download_list(request):#下载分类
    return render(request,"download_list.html")

def download(request,list):#下载列表
    first_data=mulu(list)
    # print(list)
    return render(request, 'download.html', {'data1': first_data,'data2':list})

def download_temp(request,down,list):#下载链接
    if down == 'month':
        objt = GjtjDataMonth
    elif down == 'ji':
        objt = GjtjDataJi
    else:
        objt = GjtjDataYear
    datas = objt.objects.filter(number=str(list))
    print(datas)
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    # 写入excel
    # 参数对应 行, 列, 值
    worksheet.write(0, 0, label='name')
    worksheet.write(0, 1, label='month')
    worksheet.write(0, 2, label='data')
    if down == 'year':
        for data in range(len(datas)):
            datas[data].month=2018-data
    for data in range(len(datas)):
        worksheet.write(1 + data, 0, label=datas[data].name)
        worksheet.write(1 + data, 1, label=datas[data].month)
        worksheet.write(1 + data, 2, label=datas[data].data)

    # 保存
    workbook.save('static/file/' + 'data' + '.xls')

    file = open('static/file/' + 'data' + '.xls', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="' + 'data' + '.xls"'
    return response

def mulu(request):  #返回目录列表
    first_data=[];
    second_data=[];
    if request=='month':
        objt=GjtjNameMonth
    elif request=='ji':
        objt=GjtjNameJi
    else:
        objt=GjtjNameYear
    name=objt.objects.filter(pre_number='A')
    for i in range(len(name)):
        first_data.append([[name[i].name,name[i].if_gen,name[i].number]])
        if name[i].if_gen=='1':
            name2=objt.objects.filter(pre_number=name[i].number)
            tmp=[]
            for j in name2:
                if j.if_gen=='1':
                    tmp_2=[]
                    name3=objt.objects.filter(pre_number=j.number)
                    for k in name3:
                        tmp_2.append([k.name,k.if_gen,k.number])
                    tmp.append([[j.name,j.if_gen,j.number],tmp_2])
                else:
                    tmp.append([[j.name,j.if_gen,j.number],[]])
            first_data[i].append(tmp)
        else:
            first_data[i].append([])
    # print(first_data)
    return first_data

def analysis_list(request):
    return render(request,"analysis_list.html")


def analysis(request,list):
    if request.method == "POST":
        check_box_list = request.POST.getlist('check_box_list')
        if check_box_list:
            print(check_box_list)
        name_list=get_method_name();
        return render(request, 'analysis_method_html.html', {'name': name_list,'check_list':check_box_list,'month_list':list})
    else:
        if list == 'month':
            objt = GjtjConnameMonth
        elif list == 'ji':
            objt = GjtjConnameJi
        else:
            objt = GjtjConnameYear
        first_data = mulu(list)
        name_test=objt.objects.values()
        for first_list in first_data:
            if first_list[0][1] == 1:
                first_list[0].append([])
            else:
                tmp_list = [];
                for ii in name_test:
                    if ii['number']==first_list[0][2]:
                        tmp_list.append([ii['name'],ii['con_number']])
                first_list[0].append(tmp_list)
            for second_list in first_list[1]:
                if second_list[0][1] == 1:
                    second_list[0].append([])
                else:
                    tmp_list = [];
                    for ii in name_test:
                        if ii['number'] == second_list[0][2]:
                            tmp_list.append([ii['name'],ii['con_number']])
                    second_list[0].append(tmp_list)

                for third_list in second_list[1]:
                    if third_list[1] == 1:
                        third_list.append([])
                    else:
                        tmp_list = [];
                        for ii in name_test:
                            if ii['number'] == third_list[2]:
                                tmp_list.append([ii['name'],ii['con_number']])
                        third_list.append(tmp_list)
        return render(request, 'analysis.html',{'data1': first_data,'data2':list})
def if_num_right(list,number):
    num_list={0:1,1:2,2:2,3:2,4:1,5:1,6:1,7:2,8:0,9:0}
    result=num_list[number]
    list=analysis_split("'","'",list)
    if result==0 and len(list)!=0:
        return True
    else:
        if result==len(list):
            return True
        else:
            return False

def analysis_method_list(request,list,data_list,method):   #list是month，data_list是数据的number，method是分析方法
    if if_num_right(data_list,int(method)):
        para=[]
        if request.method == "POST":
            dd=request.POST.getlist('sel_value')
            para=dd
        #获取数据
        tmp_list=analysis_split("'","'",data_list)
        # print(tmp_list)
        switch={'0':common,'1':one_regression,'2':mul_regression,'3':pierxun,'4':qq_chart,'5':normal_ratio,'6':sort_show,'7':pipei_mum,'8':gongxian,'9':zhuchengfen}
        objt={'month':GjtjDataMonth,'ji':GjtjDataJi,'year':GjtjDataYear}
        objt_name = {'month': GjtjConnameMonth, 'ji': GjtjConnameJi, 'year': GjtjConnameYear}
        data=[]
        name=[]
        for i in tmp_list:
            name_search=dict()
            name_search['number']=i[0]
            name_search['con_number']=i[1]
            get_name = objt_name[list].objects.filter(**name_search)
            for j in get_name:
                name.append(j.name)

            tmp_data=[]
            search=dict()
            search['number']=i[0]
            search['concrete_id']=str(int(i[1])+1)
            get_data=objt[list].objects.filter(**search)
            for j in get_data:
                tmp_data.append([j.month,j.data])
            data.append(tmp_data)
        print(data)
        if list=='year':
            data=error_year_shuju(list,data)
        result,data_show_scatter,data_show_line,is_category_value,choose,chart_canshu=switch[method](data,para,name)
        if request.method == "POST":
            for i in range(len(choose)):
                choose[i].append(para[i])
        # print(data_show_scatter)
        print(name)
        return render(request, 'analysis_result.html',{'result':result,'is_category_value':json.dumps(is_category_value),'data_show_scatter':data_show_scatter,'data_show_line':data_show_line,'choose':choose,'chart_canshu':chart_canshu})
    else:
        name_list = get_method_name();
        return render(request, 'analysis_method_html.html',
                      {'name': name_list, 'check_list': data_list, 'month_list': list,'if_warn':1})
def error_year_shuju(a,n):
    if a== 'year':
        result=[]
        print(n)
        for data in range(len(n)):
            tmp=[]
            for data1 in range(len(n[0])):
                print(n[data][data1][1])
                tmp.append([str(2018-data1),n[data][data1][1]])
            result.append(tmp)
    return result
def analysis_split(start_str, end_str, html):
    result=[]
    final_result=[]
    while True:
        start = html.find(start_str)
        if start >= 0:
            start += len(start_str)
            end = html.find(end_str, start)
            if end >= 0:
                result.append(html[start:end].strip())
            html=html[end+1:]
        else:
            break
    print(result)
    for i in result:
        start = i.find('&')
        final_result.append([i[0:start],i[start+1:]])
    return final_result
def get_method_name():
    total=[];
    total.append(['常规数据',0,"包括一些基本的统计结果(请选择一个数据)"])
    total.append(['一次线性回归',1,"两个数据的线性回归（请选择两个数据）"])
    total.append(['一元多次回归',2,"（选择两个数据）"])
    total.append(['皮尔逊系数',3,"(选择两个数据)"])
    total.append(['QQ图',4,"(选择一个数据)"])
    total.append(['正太比例数据',5,"选择一个数据，看哪些数据在该标准差的外面,展示的是异常值"])
    total.append(['正序排列',6,"展示正序排列，偏度和峰度"])
    total.append(['寻找最优匹配时差',7,'选择两个数据'])
    total.append(['找出每个对应的贡献度',8,'选择多个数据'])
    total.append(['主成分分析',9,'选择多个数据，返回的是转换之后的数据'])
    return total
# def chart(request,id=None):
#     if not id:
#         id ='A010101'
#     g_name=getname()
#     instance = globals()[id]
#     datas = instance.objects.all()
#     # print(datas)
#     chart_data=[]
#     tmp={}
#     for i in datas:
#         if i.name==datas[0].name:
#             tmp['data']=Decimal(i.data)
#             # tmp.month=int(i.month)
#
#             chart_data.append(tmp.copy())
#     return render(request, 'charts.html', {'data': g_name,'chart_data':chart_data})



