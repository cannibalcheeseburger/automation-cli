# Automation-cli

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![HitCount](http://hits.dwyl.com/cannibalcheeseburger/automation-cli.svg)](http://hits.dwyl.com/cannibalcheeseburger/automation-cli)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)


CLI tool to automate some of my tasks .

Might be useful (to me).

## Commands

 - [Movie/TV search](#Movie)

## Installation

### Build from Source
Clone the repository and checkout to stable commit

```
git clone https://github.com/cannibalcheeseburger/automation-cli.git
cd automation-cli
git checkout <latest_version say: v0.0.x>
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
  -n, --netflix  Disable netflix
  -p, --prime    Disable amazon prime
  -h, --hotstar  Disable hotstar
  --help         Show this message and exit.
```