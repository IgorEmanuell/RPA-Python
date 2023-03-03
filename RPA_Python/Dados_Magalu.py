from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pandas as pd

navegador = webdriver.Chrome()
navegador.get('https://www.magazineluiza.com.br/')

navegador.find_element(By.ID, 'input-search').send_keys('geladeira')
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.sleep(10)

listaDataFrame = []

listaProdutos = navegador.find_elements(By.CLASS_NAME, 'BCSuy')


for item in listaProdutos:
    nomeProduto = ''
    precoProduto = ''
    urlProduto = ''

    if nomeProduto == '':
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, 'enkhKW').text
        except Exception:
            pass
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, 'sc-kOjCZu').text
        except Exception:
            pass
# -----------------------------------------------------------------------------------

    if precoProduto == '':        
        try:
            precoProduto = item.find_element(By.CLASS_NAME, 'kPMBBS').text
        except Exception:
            pass
    elif precoProduto == '':

        try:
            precoProduto = item.find_element(By.CLASS_NAME, 'sc-ehkVkK').text
        except Exception:
            pass
    elif precoProduto == '':

        try:
            precoProduto = item.find_element(By.CLASS_NAME, 'jDmBN').text
        except Exception:
            pass
    elif precoProduto == '':

        try:
            precoProduto = item.find_element(By.CLASS_NAME, 'sc-kDvujY').text
        except Exception:
            pass
    else:
        precoProduto = '0'
# --------------------------------------------------------------------------

    if urlProduto == '':

        try:
            urlProduto = item.find_element(By.TAG_NAME, 'a').get_attribute('href')  
        except Exception:
            pass

    else:
        urlProduto = '-'

    print(nomeProduto, '-', precoProduto)
    print(urlProduto)

    dadosLinha = nomeProduto + ';' + precoProduto + ';' + urlProduto 
    listaDataFrame.append(dadosLinha)

arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
arquivoExcel.save()

dataFrame = pd.DataFrame(listaDataFrame, columns=['Descrição;Preço;Url'])

arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)
arquivoExcel.save()
