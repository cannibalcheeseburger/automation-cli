import webbrowser
import imdb
import click

vpns=[  
    "https://1337x.to/search/%s %s/1/",
    "https://thepiratebay.org/search.php?q=%s %s",
    ""
    ]
#novpns={}

count = 0

@click.command()
@click.option('-v','--vpn',is_flag=True,default = False,help="Only use if you are using a vpn")
@click.option('-f','--force',is_flag=True,default = False ,help="Force to search the given title as is(imdb api will not be refenced to correct title)")
@click.option('-t','--tv',is_flag=True,default = False,help="To search only for tv series(skips searching yts.am")
@click.option('-c','--count',type = int,help="Restricts the number of tabs to given number")
@click.argument('title',nargs = -1)

def torrent(title,vpn,force):
    """Command line utility to find torrents
    """
    kind = ""
    year = ""
    if not force:
        
        ia = imdb.IMDb()
        movie_obj = ia.search_movie(title)
        for mov in movie_obj:
            el = ia.get_movie(mov.movieID)
            title = el.get('title')
            year = str(el.get('year'))
            click.echo("Title: "+title)
            click.echo("Year: "+year)
            click.echo("PLOT:\n"+el.get('plot')[0])
            choice = input("Is this it?(ENTER for yes/n for next)").lower()
            if choice == 'n':
                click.clear()
                continue
            break    

        if not tv:
            webbrowser.open('https://yst.am/movie/'+title.replace(" ","-").lower()+"-"+year) # searches yts.am as it wont work for tv and without force

    if vpn:  
        for url in vpns:   
            webbrowser.open(url % (title, year)) #seaches every link that needs vpn
        
    else:
        pass

if __name__ == "__main__":
    torrent()