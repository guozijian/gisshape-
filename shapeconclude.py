from osgeo import  gdal
from osgeo import ogr

#这里是打开两个shape文件，一个文件统计，数据写入到另一个文件当中

filepath1 = "D:\\aaa\\bbb\\ccc.shp" #shape文件路径，根据实际情况更改即可
driver1 = ogr.GetDriverByName('ESRI Shapefile')
driver2 = ogr.GetDriverByName('ESRI Shapefile')#载入驱动
filepath2 = "D:\\aaa\\bbb\\ddd.shp"#shape文件路径，根据实际情况更改即可

dsshuju= driver1.Open(filepath1, 1)
dslinchang= driver2.Open(filepath2, 1)
#判断数据源是否为空
if dsshuju == None:
    print("打开文件【%s】失败！", filepath1 )

else:
    print("打开文件【%s】成功！", filepath1 )
if dslinchang== None:
    print("打开文件【%s】失败！", filepath1)

else:
    print("打开文件【%s】成功！", filepath1)
#获取数据源的shape数据层
shujulayer =dsshuju.GetLayer()
linchanglayer =dslinchang.GetLayer()
#获取shpe数据总数总数
totalcountlinchang= linchanglayer.GetFeatureCount()
totalcountshuju= shujulayer.GetFeatureCount()
totalforest =0.0

for i in range(0,totalcountlinchang):
    #获取某个数据层某一行数据
    featurelinchang = linchanglayer.GetFeature(i)
    # 获取某一行数据某一个数据属性
    linchangmianji = featurelinchang.GetField('面积')
    linchangname = featurelinchang.GetField('林场名')
#循环统计数据
    for k in range(0, totalcountlinchang):
        featurelinchangrepeat = linchanglayer.GetFeature(k)
        linchangrepeatname = featurelinchangrepeat.GetField('林场名')
        linchangrepeatmianji = featurelinchangrepeat.GetField('面积')
        if k!=i and linchangrepeatname ==linchangname:
            linchangmianji = linchangmianji + linchangrepeatmianji

    for j in range(0,totalcountshuju):
        featureshuju =  shujulayer.GetFeature(j)
        belongname =  featureshuju.GetField('林场名')
        if belongname!=None and belongname == linchangname:
            fugaimianji= featureshuju.GetField('面积')
            totalforest = totalforest + fugaimianji
    if linchangmianji!=0.0:
        fugairate = totalforest/linchangmianji
        fugaibaifen = str(fugairate*100)[:4]+ '%'
        if totalforest !=0.0:
            #为某个属性赋值
            featurelinchang.SetField('2019_FUGAI', fugaibaifen)
        else:
            featurelinchang.SetField('2019_FUGAI', '0.0%')

    else:
       featurelinchang.SetField('2019_FUGAI', '0.0%')
#属性赋值完后需要重新用setfeature方法更新属性被修改的那一行数据，来完成修改的提交。否则不能修改成功
    linchanglayer.SetFeature(featurelinchang)
    totalforest =0.0







