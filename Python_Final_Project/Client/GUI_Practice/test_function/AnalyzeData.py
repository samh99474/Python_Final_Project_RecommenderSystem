import re


class AnalyzeData:

    def if_data(self, data_raw, data_find):
        #查看 data中是否有 指定的字串
        result = re.search('{}'.format(data_find), data_raw)
        return result

    def catch_data_front(self, data_raw, range_back) :
        #抓取 指定字串前面的 所有data
        data_analysed = re.findall('(.*)(?={})'.format(range_back), data_raw)
        return data_analysed

    def catch_data_mid(self, data_raw, range_front, range_back) :
        #抓取 兩個指定字串中間的 所有data
        #(?<=)  //前面的string
        #(?=)  //後面的srting
        #(?<=)()(?=)  //"抓取"在這兩個string之間的"character"
        data_analysed = re.findall('(?<={})(.*)(?={})'.format(range_front, range_back), data_raw)

        return data_analysed

    def catch_data_back(self, data_raw, range_front) :
        #抓取 指定字串後面的 所有data
        data_analysed = re.findall('(?<={})(.*)'.format(range_front), data_raw)

        return data_analysed

"""
result_find = AnalyzeData()
test = "[VIP] Peter buys Computer for $666"

#print(result_find.if_data(test, "VIP"))
if result_find.if_data(test, "VIP") :
    
    name = AnalyzeData().catch_data_mid(test, "\[VIP] ", "\ buys")
    print("name : {}".format(name))

    price = AnalyzeData().catch_data_back(test, "\$")
    print("price : {}".format(price))
"""


