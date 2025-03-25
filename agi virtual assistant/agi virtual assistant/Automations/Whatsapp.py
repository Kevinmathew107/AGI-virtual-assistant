from datetime import datetime
from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep


def WhatsappMsg(name,message):
     
    startfile("C:\\Users\\maa\\OneDrive\\Desktop\\WhatsApp.lnk")

    sleep(8)

    click(x=132, y=153)

    sleep(4)

    write(name)

    sleep(4)

    click(x=207, y=239)

    sleep(4)

    click(x=757, y=989)

    sleep(4)

    write(message)

    press('enter')

def WhatsappCall(name):

    startfile("C:\\Users\\maa\\OneDrive\\Desktop\\WhatsApp.lnk")

    sleep(8)

    click(x=132, y=153)

    sleep(4)

    write(name)

    sleep(4)

    click(x=207, y=239)

    sleep(4)

    click(x=757, y=989)

    sleep(4)

    click(x=1776, y=89)

def WhatsappVideoCall(name):

    startfile("C:\\Users\\maa\\OneDrive\\Desktop\\WhatsApp.lnk")

    sleep(8)

    click(x=132, y=153)

    sleep(4)

    write(name)

    sleep(4)

    click(x=207, y=239)

    sleep(4)

    click(x=757, y=989)

    sleep(4)

    click(x=1717, y=93)

def WhatsappChat(name):

    startfile("C:\\Users\\maa\\OneDrive\\Desktop\\WhatsApp.lnk")

    sleep(8)

    click(x=132, y=153)

    sleep(4)

    write(name)

    sleep(4)

    click(x=207, y=239)

    sleep(4)

    click(x=757, y=989)

    sleep(4)

