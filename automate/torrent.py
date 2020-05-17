import webbrowser
import imdb
import click
import re
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

vpns=[  
    "https://1337x.to/search/%s %s/1/",
    "https://thepiratebay.org/search.php?q=%s %s",
    "https://torrentz2.eu/search?f=%s %s",
    "https://www.limetorrents.info/search/all/%s %s/",
    ]
novpns=[
        "https://proxyof.com/kickasstorrents-proxy-unblock/",
        "https://piratebay-proxylist.net/?utm_source=expired&referral=thepiratetpb.eu"
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
    else:
        pass
    logging.debug("End of script")

#TODO
"""
1. add non vpn sites.
2. automate searching  using selenium
"""

if __name__ == "__main__":
    torrent()