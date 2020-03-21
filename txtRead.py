#!/usr/local/bin/python3
import csv
foundCnt = 0
searchStr = input("What are we looking for?")
# dataCct = list(dataReader)
with open('pers_acct.csv', 'rt') as f:
    dataReader = csv.reader(f, delimiter=',')
    for row in dataReader:
        if len(row) > 3 and searchStr == row[1]:
            foundCnt = foundCnt + 1
# print(dataCct[1000][1]," ",dataCct[1000][2])
# print(dataCct[1001][1]," ",dataCct[1001][2])
# print(dataCct[1002][1]," ",dataCct[1002][2])
# print(dataCct[1003][1]," ",dataCct[1003][2])
#print("length of list is [ ", len(dataCct), " ]")

print("there are  [ ", foundCnt, " ] Payroll entries")


