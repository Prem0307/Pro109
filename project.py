import pandas as pd
import csv
import statistics

df=pd.read_csv("SP.csv")

data_list=df["math score"].to_list()


datas_mean=statistics.mean(data_list)


datas_median=statistics.median(data_list)


datas_mode=statistics.mode(data_list)

print("Mean,Median and mode of data is {}, {}, {}".format(datas_mean,datas_median,datas_mode))


datas_stdev=statistics.stdev(data_list)

print("Standard Deviation of data is "+str(datas_stdev))


first_std_deviation_start,first_std_deviation_end=datas_mean-datas_stdev,datas_mean+datas_stdev

second_std_deviation_start,second_std_deviation_end=datas_mean-(2*datas_stdev),datas_mean+(2*datas_stdev)

third_std_deviation_start,third_std_deviation_end=datas_mean-(2*datas_stdev),datas_mean+(3*datas_stdev)

thin_1_std_deviation=[result for result in data_list if result > first_std_deviation_start and result < first_std_deviation_end]
print("{} % of data lies betwwen 1 standard deviation".format(len(thin_1_std_deviation)*100.00/len(data_list)))
thin_2_std_deviation=[result for result in data_list if result > second_std_deviation_start and result < second_std_deviation_end]
print("{} % of data lies betwwen 2 standard deviation".format(len(thin_2_std_deviation)*100.00/len(data_list)))
thin_3_std_deviation=[result for result in data_list if result > third_std_deviation_start and result < third_std_deviation_end]
print("{} % of data lies betwwen 3 standard deviation".format(len(thin_3_std_deviation)*100.00/len(data_list)))