# Importa as imagens do SINtegre do ONS para ser inserido nos produtos do Planejamento Energético 
from selenium import webdriver
import io 
import urllib
from PIL import Image
from io import BytesIO
import time
from selenium.webdriver.chrome.options import Options

# configura o driver para não abrir na tela, i.e, headless
options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)

# instrui o driver a ir no primeiro mapa e fazer o login 
driver.get ("https://sintegre.ons.org.br/sites/9/38/Documents/images/operacao_integrada/meteorologia/oshad_50_sm.gif")
driver.find_element_by_id("username").send_keys("jose_cpfl")
driver.find_element_by_id ("password").send_keys("bbAA4433!!")
driver.find_element_by_name("submit.Signin").click()

# tira a primeira foto da página e a recorta 
png = driver.get_screenshot_as_png() # saves screenshot of entire page
im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
size = [185, 0, 630.5, 575] #left, top, right, botton  #size = [295, 0, 740.5, 575] #left, top, right, botton

#salva na rede
im = im.crop((size[0], size[1], size[2], size[3])) # defines crop points
im.save("U:\\Planejamento\\Boletim Semanal\\Preciptação\\01.gif") # saves new cropped image, precipitação no últimos 10 dias 
time.sleep(3.5)

for numero in range(1, 10):

    if numero != 9: # rainfall forecast D1 to D8
        driver.get ("https://sintegre.ons.org.br/sites/9/38/Documents/images/operacao_integrada/meteorologia/eta/shad50_"+ str(numero) + ".gif")
        png = driver.get_screenshot_as_png() # saves screenshot of entire page  
        im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
        im = im.crop((size[0], size[1], size[2], size[3])) # defines crop points
        im.save("U:\\Planejamento\\Boletim Semanal\\Preciptação\\0" + str(numero + 1) + ".gif") # saves new cropped image

    else: # rainfall forecast D9
        driver.get ("https://sintegre.ons.org.br/sites/9/38/Documents/images/operacao_integrada/meteorologia/eta/shad50_"+ str(numero) + ".gif")
        png = driver.get_screenshot_as_png() # saves screenshot of entire page  
        im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
        im = im.crop((size[0], size[1], size[2], size[3])) # defines crop points
        im.save("U:\\Planejamento\\Boletim Semanal\\Preciptação\\" + str(numero + 1) + ".gif") # saves new cropped image

    time.sleep(3.5)

driver.quit()

# fim, todas as imagens foram salvas com sucesso no servidor 