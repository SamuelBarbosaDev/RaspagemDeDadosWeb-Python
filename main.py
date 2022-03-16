




#Como? extraí dados da web.
from selenium import webdriver as wb

browse = wb.Firefox()
numero = 1

browse.get(
"""https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic"""
)

for i in range(12):
    numero += 1

    ano = browse.find_element_by_xpath(
f"""//*[@id="parent-fieldname-text"]/table[2]/tbody/tr[1]/td[10]/b"""
    ).text

    taxa = browse.find_element_by_xpath(
f"""//*[@id="parent-fieldname-text"]/table[2]/tbody/tr[{numero}]/td[10]"""
    ).text

    mes = browse.find_element_by_xpath(
f"""//*[@id="parent-fieldname-text"]/table[2]/tbody/tr[{numero}]/td[1]/b"""
    ).text

    print("-"*100)
    print(f"Taxa selic em {ano}")
    print(f"{mes} : {taxa}")