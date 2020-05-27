from bs4 import BeautifulSoup
import requests
import re
database_url = {
    "ranfor": "https://bourse.tgju.org/markets/stock/40505767672724777",
    "saba": "https://bourse.tgju.org/markets/stock/45392752356003555",
    "seshahed": "https://bourse.tgju.org/markets/stock/63481599728522324",
    "vesobhan": "https://bourse.tgju.org/markets/stock/43283802997035462",
    "khagostar": "https://bourse.tgju.org/markets/stock/48990026850202503",
    "shesta": "https://bourse.tgju.org/markets/stock/2400322364771558",
    "tepco": "https://bourse.tgju.org/markets/stock/54509759694064219",
    "folad": "https://bourse.tgju.org/markets/stock/46348559193224090",

}


def stock(url):
    soup = BeautifulSoup(url.text, 'html.parser')

    name_namad = soup.find(name="h1", class_="title").getText()
    print("\nEsm namad              : ", name_namad)

    akharin_gheymat = soup.find_all(name="span", class_="value")  # .getText()
    akharin_gheymat = akharin_gheymat[3].getText()
    akharin_gheymat = re.sub(r'\s+', '', akharin_gheymat)
    darsad_akharin_gheymat = akharin_gheymat[-4:]
    akharin_gheymat = akharin_gheymat[:-4:]
    print("Akharin gheymat        : ", akharin_gheymat)
    print("Darsad akharin gheymat : ", darsad_akharin_gheymat, '%')

    gheymat_payani = soup.find_all(name="span", class_="value")  # .getText()
    gheymat_payani = gheymat_payani[4].getText()
    gheymat_payani = re.sub(r'\s+', '', gheymat_payani)
    darsad_gheymat_payani = gheymat_payani[-4:]
    gheymat_payani = gheymat_payani[:-4:]
    print("Gheymat payani         : ", gheymat_payani)
    print("Darsad gheymat payani  : ", darsad_gheymat_payani, '%')

    vazeeat_namad = soup.find_all(name="span", class_="value")  # .getText()
    vazeeat_namad = vazeeat_namad[2].getText()
    print("Vazeeat namad          : ", vazeeat_namad)

    eps = soup.find_all(name="td", class_="text-right")  # .getText()
    eps = eps[11].getText()
    print("Eps                    : ", eps)


y = 'y'
while y == 'y':
    print('''List saham ha :D\n
    ranfor
    saba
    seshahed
    vesobhan
    khagostar
    shesta
    tepco
    folad
    ''')
    geting = input("\nSahame khod ra vared konid : ")
    if geting in database_url:
        url = requests.get(database_url[geting])
        stock(url)
    else:
        print("\nSaham shoma dar database nist \nYa nam saham ra eshtebah mizanid :D ")
    y = input("\nBaraye entekhab dobare [y] : ")
if y != 'y':
    print("\nMovafagh bashi :D ")
else:
    pass
