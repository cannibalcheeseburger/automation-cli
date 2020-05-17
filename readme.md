# Automation-cli

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![HitCount](http://hits.dwyl.com/cannibalcheeseburger/automation-cli.svg)](http://hits.dwyl.com/cannibalcheeseburger/automation-cli)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)


CLI tool to automate some of my tasks .

Might be useful (to me).

## Commands

 - [Torrent Finder](#Torrent)
 - [Movie/TV search](#Movie)

## Installation

### Build from Source
Clone the repository and checkout to stable commit

```
git clone https://github.com/cannibalcheeseburger/automation-cli.git
cd automation-cli
```
### Install Requirements

```
python3 -m pip install --user -r requirements.txt
```

### Setup

I would recommend doing it in a virtual environment .
```
pip install --editable .
```

# Commands 

## Torrent

This ultility searches for torrents in various sites to get the best torrent links.Script is at `/automate/torrent.py`

<b>IMPORTANT</b>: Connecting to a VPN is recommended as most of the sites would be blocked(to enable sites which can be accessed with vpn use `-v` switch). Other than that most of these sites might contain some questionable ads/graphics .Use at your own descretion.

USE : Just enter title of torrent to be searched along with options.

Use `--help` option with command to get details about all other options.

```
(env) D:\GITHUB\MERE WALE\automation-cli>torrent --help
Usage: torrent [OPTIONS] [TITLE]...

  Command line utility to find torrents

Options:
  -v, --vpn            Only use if you are using a vpn
  -f, --force          Force to search the given title as is(imdb api will not   
                       be refenced to correct title)

  -t, --tv             To search only for tv series(skips searching yts.am       
  -c, --count INTEGER  Restricts the number of tabs to given number
  --help               Show this message and exit.
```

EXAMPLE :
```
(env) D:\GITHUB\MERE WALE\automation-cli>torrent -v -c 4  scoob
Title: Scoob!
Year: 2020
PLOT:
Scooby and the gang face their most challenging mystery ever: a plot to unleash the ghost dog Cerberus upon the world. As they race to stop this dogpocalypse, the gang discovers that Scooby has an epic destiny greater than anyone imagined.
Is this it?(ENTER for yes/n for next)

2020-05-18 05:21:15,703 - DEBUG - Opening browser tab for https://yst.am/movie/scoob!-2020
2020-05-18 05:21:15,770 - DEBUG - Opening browser tab for https://1337x.to/search/Scoob! 2020/1/
2020-05-18 05:21:15,863 - DEBUG - Opening browser tab for https://thepiratebay.org/search.php?q=Scoob! 2020
2020-05-18 05:21:16,013 - DEBUG - Opening browser tab for https://torrentz2.eu/search?f=Scoob! 2020
2020-05-18 05:21:16,118 - DEBUG - Opening browser tab for https://www.limetorrents.info/search/all/Scoob! 2020/
2020-05-18 05:21:16,124 - DEBUG - End of script
```

OPTIONAL :
To disable debug loggings just add following line to `/automate/torrent.py`

```python
logging.disable(logging.CRITICAL)
```

## Movie

This script takes the title of movie or tv series you want to search on all of streaming platforms provided in the script `/automate/movie.py` .

I have added Netflix ,Amazon prime and Hotstar but you can add more.

It is pretty simple script, you just need to pass the title as argument.

<b>Important:</b> You must be logged in on these services in your browser for it to work.

Use `--help` option with `movie` command to see all the options and usage

`TITLE` : title of the movie/series to be searched.

Every site will be opened in its own  browser tab.

```
D:\GITHUB\MERE WALE\automation-cli>movie --help
Usage: movie [OPTIONS] [TITLE]...

  Command line tool to automate some stuff

Options:
  -n, --nonetflix  Disable netflix
  -p, --noprime    Disable amazon prime
  -h, --nohotstar  Disable hotstar
  --help         Show this message and exit.
```