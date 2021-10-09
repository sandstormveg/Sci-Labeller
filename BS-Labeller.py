import anvil.server

anvil.server.connect("KH4GFFNW5Z2VJRB3JUPRGWQF-KUJRYIF2QC5JWKKT")
from bs4 import *
import requests


@anvil.server.callable
def sendURL(enterProduct):
    # chemical name
    url = 'https://www.google.com/search?q=' + 'what is the main chemical in ' + enterProduct + '?'
    request_result = requests.get(url)
    soup = BeautifulSoup(request_result.text, 'html.parser')
    info = soup.findAll('div', class_='BNeawe s3v9rd AP7Wnd')
    chemin = []
    cheminfo = []

    try:
        for txt in info:
            cheminfo.append(txt.get_text())
        try:
            chemin.append(cheminfo[1][0:cheminfo[1].index(' ', cheminfo[1].index(' ') + 1, cheminfo[1].index(' ') + 2)])
        except ValueError:
            chemin = cheminfo[1:]
            print(chemin[1])

    except IndexError:
        print('No chemical name available')
        cheminfo = (enterProduct)

    # product images
    html_page = requests.get("https://en.wikipedia.org/wiki/" + enterProduct)
    imgsoup = BeautifulSoup(html_page.text, 'html.parser')
    prodimg = []
    images = []
    sentimg = []
    for img in imgsoup.findAll('img'):
        images.append(img.get('src'))
    for img in images:
        if 'icon' in str(img).lower():
            pass
        elif 'logo' in str(img).lower():
            pass
        elif 'featured' in str(img).lower():
            pass
        elif 'speaker' in str(img).lower():
            pass
        elif 'box' in str(img).lower():
            pass
        elif 'check' in str(img).lower():
            pass
        elif 'nfpa' in str(img).lower():
            pass
        elif 'mark' in str(img).lower():
            pass
        elif 'shackle' in str(img).lower():
            pass
        elif 'support' in str(img).lower():
            pass
        elif 'symbol_category_class' in str(img).lower():
            pass
        elif 'question_book' in str(img).lower():
            pass
        elif str(enterProduct) in str(img).lower():
            sentimg.append(img)
        else:
            prodimg.append(img)
    if len(sentimg) >= 4:
        sentimg = sentimg[0:]
    else:
        try:
            sentimg.append(prodimg[0])
            sentimg.append(prodimg[1])
            sentimg.append(prodimg[2])
            sentimg.append(prodimg[3])
        except Exception:
            sentimg.append(images[3])
            sentimg.append(images[4])
            print('no more images')

            # a couple of product factoids
    cinfo = []
    factoids = []
    sentfacts = []
    try:
        for info in imgsoup.findAll('p'):
            cinfo.append(info.get_text())
            str(info).strip('')
        for info in cinfo:
            if info == '':
                print('empty devils')
                continue
            elif 'see text' in str(info).lower():
                pass
            elif '{' in str(info).lower():
                pass
            elif info == '\n':
                pass
            else:
                factoids.append(str(info).strip('\n'))
        if len(factoids) >= 2:
            sentfacts = factoids[0:]
        else:
            factoids.append(cinfo[2])
            factoids.append(cinfo[3])
            sentfacts = factoids[0:]

    except Exception:
        print(Exception)
        print('No data available')

    # print(sentfacts)
    # return values to anchor
    return sentimg, sentfacts, chemin


anvil.server.wait_forever()