import click
import webbrowser
@click.command()


@click.option('-n','--nonetflix',is_flag = True,default = True,help="Disable netflix")
@click.option('-p','--noprime',is_flag = True,default = True,help="Disable amazon prime")
@click.option('-h','--nohotstar',is_flag = True,default = True,help="Disable hotstar")
@click.argument('title',nargs =-1)

def movie(title,nonetflix,noprime,nohotstar):
    """ Command line tool to automate searching movie/TV series title
    """   
    search = " ".join(title)
    netflix = "https://www.netflix.com/search?q=" + search
    prime = "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=" + search +"&ie=UTF8"
    hotstar = "https://www.hotstar.com/in/search?q="+search+"&utm_source=gwa"

    if nonetflix == True:
        webbrowser.open(netflix)
    if noprime == True:
        webbrowser.open_new_tab(prime)
    if nohotstar == True:
        webbrowser.open_new_tab(hotstar)


if __name__=="__main__":
    movie()   