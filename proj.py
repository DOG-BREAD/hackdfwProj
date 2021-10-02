# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    with open("myfile1.txt", "w+") as file:
        while True:
            file.write(str(getTemperatureMoniter()))        # writes a string to a file
            file.write(str(getHumidityMoniter()))
            file.write(str(getInventoryCount()))
            file.write(str(getLocation()))
            file.write(str(copylogs()))
            file.write(str(fileuploader()))
            file.write(str(encryption()))
            
def getTemperatureMoniter():
    temp = input("Gathering current temperature");
    print("current temperature" + temp)
    return temp

def getHumidityMoniter():
    temp = input("Gathering current temperature");
    print("current temperature" + temp)
    return temp
def getInventoryCount():
    temp = input("Gathering current temperature");
    print("current temperature" + temp)
    return temp
    
def getLocation():
    temp = input("Gathering current temperature");
    print("current temperature" + temp)
    return temp
def copylogs():
    temp = input("Gathering current temperature");
    print("current temperature" + temp)
    return temp

def fileuploader():
    temp = input("Gathering current temperature");
    print("current temperature" + temp)
    return 
def encryption():
    temp = input("Gathering current temperature");
    print("current temperature" + temp)
    return temp