#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import re

DIR                = "C:\"                            # 文件目录
fileNameList       = [] 
FileTypeList       = [".xml", ".tpl"]                 # 文件类型匹配列表
FileNameFilterList = []                               # 文件名中匹配列表
FindStrList        = ['Enhanced Rack Optimization']   # 文件内容匹配列表

def isFolderExist(dir):
    if (os.path.exists(dir)):
        return True;
    else:
        return False;

def isFileNameContainStr(fileNameFilterStrList, filename):
    if len(fileNameFilterStrList) == 0:
        return True
    for filterStr in fileNameFilterStrList:
        if filterStr in filename:
            return True
    return False

def isFileNameContainType(typeList, filename):
    if len(typeList) == 0:
        return True;
    for type in typeList:
        if os.path.splitext(filename)[1] == type:
            return True
    return False

def listFile(path, fileNameFilterList, typeList):
    if not isFolderExist(path):
        return False;
    for filename in os.listdir(path):
        if os.path.isdir(path + "\\" + filename):
            listFile(path + "\\" + filename, FileNameFilterList, typeList)
        if os.path.isfile(path + "\\" + filename):
            if False == isFileNameContainStr(fileNameFilterList, filename):
                continue
            if isFileNameContainType(typeList, filename):
                fileNameList.append(path + "\\" + filename);
                continue
    return True;

def findFromFile(filename, strlist):
    file = open(filename)
    count = 0;
    for line in file:
        #if '$' in line:
        #    continue        
        count = count+1
        isContained = True
        for str in strlist:
            if str not in line:
                isContained = False
                break;
        if isContained == True:
            print filename, count , line
    file.close()

def findFromDir(strlist):
    for name in fileNameList:
        findFromFile(name, strlist)

if __name__ == "__main__":
    if not listFile(DIR, FileNameFilterList, FileTypeList):
        print "FILE PATH ERROR"
        sys.exit()
    print "File Number: %d" % len(fileNameList)
    findFromDir(FindStrList)
    print "FIND END"
