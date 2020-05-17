import click
import webbrowser
@click.command()


@click.option('-n','--netflix',is_flag = True,default = True,help="Disable netflix")
@click.option('-p','--prime',is_flag = True,default = True,help="Disable amazon prime")
@click.option('-h','--hotstar',is_flag = True,default = True,help="Disable hotstar")
@click.argument('title',nargs =-1)

def movie(title,n,p,h):
    """ Command line tool to automate some stuff
    """   
    search = " ".join(title)
    netflix = "https://www.netflix.com/search?q=" + search
    prime = "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=" + search +"&ie=UTF8"
    hotstar = "https://www.hotstar.com/in/search?q="+search+"&utm_source=gwa"

    if n == True:
        webbrowser.open(netflix)
    if p == True:
        webbrowser.open_new_tab(prime)
    if h == True:
        webbrowser.open_new_tab(hotstar)


if __name__=="__main__":
    movie()   