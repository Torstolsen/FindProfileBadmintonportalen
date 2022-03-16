from fileinput import close
from lib2to3.pgen2 import driver
from msilib.schema import Error
from re import search
from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
import PySimpleGUI as sg
def søkefunksjon():
    global values
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Dette programmet finner ut hvilke turneringer du har deltatt på')],
                [sg.Text('Skriv inn Klubb'), sg.InputText()],
                [sg.Text('Spillernavn (Fornavn og Etternavn)'), sg.InputText()],
                [sg.Button('Søk'), sg.Button('Avbryt')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event and values != "":
            break
    main()
def main():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.badmintonportalen.no/NBF/Ranglister/")

    search = driver.find_element(By.ID,"TextBoxName")
    send_nøkkel = search.send_keys(values[0])
    search.send_keys(Keys.RETURN)
    n = 1
    try:
        while EC.alert_is_present():
        # switch_to.alert for switching to alert and accept
            alert = driver.switch_to.alert
            alert.accept()
            search.clear()
            send_nøkkel_hehe = search.send_keys(values[0][:-n])
            search.send_keys(Keys.RETURN)
            n = n + 1
    except:
        pass

    try:
        main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "RankingListGrid"))
        )
        link = driver.find_element(By.PARTIAL_LINK_TEXT, values[1])
        link.click()
        main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "playerprofilerankingpointstable"))
        )
        profilvisning = driver.find_element(By.LINK_TEXT, 'Vis spillerprofil')
        profilvisning.click()
        main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'GridView'))
        )
        main = driver.find_element(By.CLASS_NAME, 'showplayerprofile')
        sg.popup(main.text)

    except NoSuchElementException:
        damesøk = driver.find_element(By.LINK_TEXT, 'DS')
        damesøk.click()
        main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "RankingListGrid"))
        )
        link = driver.find_element(By.PARTIAL_LINK_TEXT, values[1])
        link.click()
        main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "playerprofilerankingpointstable"))
        )
        profilvisning = driver.find_element(By.LINK_TEXT, 'Vis spillerprofil')
        profilvisning.click()
        main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'GridView'))
        )
        main = driver.find_element(By.CLASS_NAME, 'showplayerprofile')
        sg.popup(main.text)
    søkefunksjon()
søkefunksjon()