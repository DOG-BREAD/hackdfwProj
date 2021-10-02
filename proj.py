# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def main():
    with open("writes.txt", "w+") as file:

        with open('reads.txt', "r+") as reads:
            contents = reads.read()
            while True:

        # writes a string to a file
                file.write(str(getTemperatureMoniter()))
                file.write(str(getHumidityMoniter()))
                file.write(str(getInventoryCount()))
                file.write(str(getLocation()))
                file.write(str(copylogs()))
                file.write(str(fileuploader()))
                file.write(str(encryption()))


def getTemperatureMoniter():
    temp = input("Gathering current temperature")
    print("current temperature" + temp)
    return temp


def getHumidityMoniter():
    humidity = input("Humidity %")
    print("current temperature" + humidity)
    return humidity


def getInventoryCount():
    inventory = input("Gathering current temperature")
    print("current temperature" + inventory)
    return inventory


def getLocation():
    location = input("Gathering current temperature")
    print("current temperature" + location)
    return location


def copylogs():
    copy = input("Gathering current temperature")
    return


def fileuploader():
    temp = input("Gathering current temperature")
    print("current temperature" + temp)
    return


def encryption():
    temp = input("Gathering current temperature")
    print("current temperature" + temp)
    return temp
