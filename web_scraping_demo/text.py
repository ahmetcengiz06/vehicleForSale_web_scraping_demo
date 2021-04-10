import requests
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup
from openpyxl import Workbook

carsModel=[]
carsYear =[]
carsKm=[]
carsColor=[]
carsPrice=[]

for i in range(1,50):
    url="https://www.arabam.com/ikinci-el/otomobil/volkswagen-passat-1-6-tdi-bluemotion-comfortline?take=50&page="+str(i)
    result=requests.get(url)
    src=result.content
    soup = BeautifulSoup(src,'lxml')
    for x in soup.select('tr td:nth-child(2)'):
        carModel = x.get_text().strip()
        if carModel!='Model':
         carsModel.append(carModel)
    for x in soup.select('tr td:nth-child(4)'):
        carYear = x.get_text().strip()
        if carYear!='Yıl':
         carsYear.append(carYear)
    for x in soup.select('tr td:nth-child(5)'):
        carKm= x.get_text().strip()
        if carKm!='Kilometre':
         carsKm.append(carKm)
    for x in soup.select('tr td:nth-child(6) a'):
        carColor=x.get_text().strip()
        if carColor!='Renk':
          carsColor.append(carColor)
    for x in soup.select('tr td:nth-child(7) .listing-price'):
        carPrice=x.get_text().strip()
        if carPrice!='Fiyat':
            carsPrice.append(carPrice)


arrCarsModel= np.array(carsModel)
arrCarsYear= np.array(carsYear)
arrCarsKm=np.array(carsKm)
arrCarsColor=np.array(carsColor)
arrCarsPrice=np.array(carsPrice)

data={'Model':arrCarsModel,
    'Year':arrCarsYear,
    'Km':arrCarsKm,
    'Color':arrCarsColor,
    'Price':arrCarsPrice
}

df=pd.DataFrame(data)

df.to_excel("cars.xlsx")

print(df)