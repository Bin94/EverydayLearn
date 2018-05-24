#https://github.com/Show-Me-the-Code/python/blob/master/Lyndon1994/0004.py
import os
import re

def stat(file):
    if os.path.exists(file):
        f = open(file, 'r')
        str = f.read()
        reObj = re.compile('\b?(\w+)\b?')
        words = reObj.findall(str)
        wordDict = dict()
        for word in words:
            if word.lower() in wordDict:
                wordDict[word.lower()] += 1
            else:
                wordDict[word] = 1
        for key,value in wordDict.items():
            print('%s:%s' % (key,value))
    else:
        print('File is not exist.')

if __name__ == '__main__':
    stat('test.txt')