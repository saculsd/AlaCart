import requests
import os
from bs4 import BeautifulSoup


def request(ausgabe):
    with requests.Session() as c:

        url = "https://iss-mahlsdorf-berlin.de/iserv/app/login"
        username = "lucas.buehring-uhle"
        password = "5530123098lol"

        c.get(url)
        login_data = dict(_username=username, _password=password)
        c.post(
            url,
            data=login_data,
            headers={"Referer": "https://iss-mahlsdorf-berlin.de/iserv/app/login"})
        page_data = c.get(
            "https://iss-mahlsdorf-berlin.de/iserv/infodisplay/show/5")
        page = page_data.text

    def link_download(download_url, endung):
        r = c.get(download_url)
        plan = open("./bilder/plan" + str(endung) + ".jpg", "wb")
        plan.write(r.content)
        plan.close()

    ##

    file = open("home.html", "w", encoding="utf8")
    file.write(page)
    file.close

    timer = 0
    link1 = None
    link2 = None
    link3 = None
    link1_full = None
    link2_full = None
    link3_full = None

    with open("home.html", encoding="utf8") as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
    infobildschirm = soup.find_all("div", class_="infodisplay-widget-content")
    for infobilschirm_ in infobildschirm:
        link_name = infobilschirm_.img
        # links = (link_name.get('src'))
        # link = (link_name.split())

        if timer == 0:
            link1 = link_name

        if timer == 1:
            link2 = link_name

        if timer == 2:
            link3 = link_name
            timer = 0
            break

        timer += 1

    if link1 == None:
        if ausgabe == True:
            print("ACHTUNG LNIK1 = NONE(Leer)")
    else:
        link1_full = "https://iss-mahlsdorf-berlin.de" + str(link1)
        link1_full = link1_full.replace("<", "")
        link1_full = link1_full.replace('img class="" src="', "")
        link1_full = link1_full.replace('"/>', "")
        link1_full = link1_full.replace('img class="hidden" src="', "")
        if ausgabe == True:
            print(link1_full)

    if link2 == None:
        if ausgabe == True:
            print("ACHTUNG LNIK2 = NONE(Leer)")
    else:
        link2_full = "https://iss-mahlsdorf-berlin.de" + str(link2)
        link2_full = link2_full.replace("<", "")
        link2_full = link2_full.replace('img class="" src="', "")
        link2_full = link2_full.replace('"/>', "")
        link2_full = link2_full.replace('img class="hidden" src="', "")
        if ausgabe == True:
            print(link2_full)

    if link3 == None:
        if ausgabe == True:
            print("ACHTUNG LNIK3 = NONE(Leer)")
    else:
        link3_full = "https://iss-mahlsdorf-berlin.de" + str(link3)
        link3_full = link3_full.replace("<", "")
        link3_full = link3_full.replace('img class="" src="', "")
        link3_full = link3_full.replace('"/>', "")
        link3_full = link3_full.replace('img class="hidden" src="', "")
        if ausgabe == True:
            print(link3_full)
            return (link3_full)

    ##

    if link1 != None:
        link_download(link1_full, "_link1")

    if link2 != None:
        link_download(link2_full, "_link2")
    if link3 != None:
        link_download(link3_full, "_link3")

    if link1 != None:
        extra_link1 = link1_full

        extra_link1 = extra_link1.replace("14/1", "14/2")
        link_download(extra_link1, "_extra1")
        extra_link1 = extra_link1.replace("14/2", "14/3")
        link_download(extra_link1, "_extra2")
        extra_link1 = extra_link1.replace("14/3", "14/4")
        link_download(extra_link1, "_extra3")
        extra_link1 = extra_link1.replace("14/4", "14/5")
        link_download(extra_link1, "_extra4")

        bild1_größe = os.path.getsize("./bilder/plan_extra1.jpg")
        bild2_größe = os.path.getsize("./bilder/plan_extra2.jpg")
        bild3_größe = os.path.getsize("./bilder/plan_extra3.jpg")
        bild4_größe = os.path.getsize("./bilder/plan_extra4.jpg")

        if bild1_größe > 30000:
            request.post_bild1 = False
        else:
            request.post_bild1 = True

        if bild2_größe > 30000:
            request.post_bild2 = False
        else:
            request.post_bild2 = True

        if bild3_größe > 30000:
            request.post_bild3 = False
        else:
            request.post_bild3 = True

        if bild4_größe > 30000:
            request.post_bild4 = False
        else:
            request.post_bild4 = True





