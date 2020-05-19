import webbrowser
import imdb
import click
import re
import logging
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

vpns=[  
    "https://1337x.to/search/%s %s/1/",
    "https://thepiratebay.org/search.php?q=%s %s",
    "https://torrentz2.eu/search?f=%s %s",
    "https://www.limetorrents.info/search/all/%s %s/",
    ]
novpns=[
        "https://boatairproxy.org/search.php?q=%s %s",
     #   "https://tpbpiratez.org/search.php?q=%s %s",
     #   "https://x1337x.se/%s %s/1/"
      # "https://proxyof.com/kickasstorrents-proxy-unblock/",
        #"https://piratebay-proxylist.net/?utm_source=expired&referral=thepiratetpb.eu"  #FOR LATER USE 
        ]


@click.command()
@click.option('-v','--vpn',is_flag=True,default = False,help="Only use if you are using a vpn")
@click.option('-f','--force',is_flag=True,default = False ,help="Force to search the given title as is(imdb api will not be refenced to correct title)")
@click.option('-t','--tv',is_flag=True,default = False,help="To search only for tv series(skips searching yts.am")
@click.option('-c','--count',type = int,default = 6,help="Restricts the number of tabs to given number")
@click.argument('title',nargs = -1)

def torrent(title,vpn,force,count,tv):
    """Command line utility to find torrents
    """
    logging.debug("Starting Script")
    counter = 0

    title = " ".join(title)
    year = ""
    reg = re.compile(r's\d\de\d\d')
    ep = reg.search(title.lower())
    # checks if epsode details have been passed and assigns tv as true
    if ep:
        ep = ep.group()
        tv = True
        title = title.replace(ep,"")

    if not force:
        
        ia = imdb.IMDb()
        movie_obj = ia.search_movie(title)
        for mov in movie_obj:
            el = ia.get_movie(mov.movieID)
            title = el.get('title')
            year = str(el.get('year'))
            click.clear()
            click.echo("Title: "+title)
            click.echo("Year: "+year)
            click.echo("PLOT:\n"+el.get('plot')[0])
            choice = input("\nIs this it?(ENTER for yes/n for next)").lower()
            if choice == 'n':
                click.clear()
                continue
            break    
        
        if not tv:
            webbrowser.open('https://yst.am/movie/'+title.replace(" ","-").lower()+"-"+year) # searches yts.am as it wont work for tv and without force
            logging.debug("Opening browser tab for %s " % ('https://yst.am/movie/'+title.replace(" ","-").lower()+"-"+year))
            counter = counter + 1
        
        elif vpn:
            webbrowser.open("https://eztv.io/search/"+title.replace(" ","-")+"-"+ep)  # searches eztv for series if vpn is connected
            logging.debug("Opening browser tab for %s " % ("https://eztv.io/search/"+title.replace(" ","-")+"-"+ep))
            counter = counter + 1
    # vpn sites
    if vpn:  
        for url in vpns:   
            if counter < count:
                if tv:
                    webbrowser.open(url % (title, ep)) #seaches every link that needs vpn
                    logging.debug("Opening browser tab for %s " % url % (title, ep))
                else:
                    webbrowser.open(url % (title, year)) #seaches every link that needs vpn
                    logging.debug("Opening browser tab for %s " % url % (title, year))
                counter = counter + 1
   
   
   # non vpn sites
    for url in novpns:
        if counter < count:
            if tv:
                webbrowser.open(url % (title, ep)) #seaches every link that doesnt needs vpn
                logging.debug("Opening browser tab for %s " % url % (title, ep))
            else:
                webbrowser.open(url % (title, year)) #seaches every link that doesnt needs vpn
                logging.debug("Opening browser tab for %s " % url % (title, year))
            counter = counter + 1

    # kickass proxy 
    logging.debug("OPENING KICKASS PROXY......")
    browser1 = webdriver.Chrome("/media/cannibalcheeseburger/2C009EE8009EB872/GITHUB/MERE_WALE/automation-cli/webdriver/lin/chromedriver") #### CHANGE THIS FUCKING PATH TO YOUR NEED
    browser1.get("https://proxyof.com/kickasstorrents-proxy-unblock/")
    wait = WebDriverWait(browser1,600)
    proxy9 = browser1.find_element_by_css_selector("#post-157 > div > strong > a:nth-child(3)")
    proxy9.click()
    input_box = browser1.find_element_by_id('contentSearch')
    if tv:
        input_box.send_keys(title+" "+ep+Keys.ENTER)
        wait = WebDriverWait(browser1,400)
        button = browser1.find_element_by_css_selector("#wrapperInner > div.mainpart > table > tbody > tr > td > div.tabs > ul > li:nth-child(4) > a")
    else:
        input_box.send_keys(title+" "+year+Keys.ENTER)
        wait = WebDriverWait(browser1,400)
        button = browser1.find_element_by_css_selector("#wrapperInner > div.mainpart > table > tbody > tr > td > div.tabs > ul > li:nth-child(2) > a")
    wait = WebDriverWait(browser1,200)
    button.click()
    counter = counter+1

    click.pause()

    logging.debug("End of script")

#TODO
"""
## ADD MORE NON VPN SITES
## AUTOMATE 'EM
"""

if __name__ == "__main__":
    torrent()