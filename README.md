
# lacanCrawler: An Automation Webcrawler for Extracting Parliament Data (Private)

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)


An automation web crawling framework for scraping parliamentary data from United Kingdom and National Diet of Japan based on Selenium.

###### the repository is only visible to LACAN research team.


## The Structure of `lacanCrawlers`

```
bamberg.lacan/
    └── LACAN/           ┌─ House of the Commons
        ├── england.py╶──└─ House of the Lord
        ├── scotlan.py
        ├── nirland.py
        └── japan.py  
```

## ENVIROMENT 

### Step 1: Download `lacanCrawler`

- Before downloading the module, the installation of  [Anaconda Navigator](https://www.anaconda.com/products/individual-b) and [Python>=3.9](https://www.python.org/downloads/release/python-3810/) are required beforehand.  About how to use git and Github, please have a look at this [Tutorial for Beginners](https://www.youtube.com/watch?v=RvnM6EEwp1I). 

```
# clone the lacanCrawlers repository
git clone  git@github.com:davidycliao/lacanCrawlers.git

# change the directory by typing `cd` command once `lacanCrawlers` repository is downloaded.
cd lacanCrawlers

# create the enviroment by using conda and name the enviroment `lacanCrawlers`.
conda create -n lacanCrawlers python=3.9

# Activate the pre-named enviroment.

conda activate lacanCrawlers 
```


### Step 2: Instruction for the Installation of the Required Dependencies

```
# install required modules from `requirements.txt` using `pip` methond.

pip install -r requirements.txt   
```

## USAGE

### UK Parliament

The UK Parliament has two Houses, the House of Commons and the House of Lord. 

```
from LACAN import england as en
```

### The Scottish Parliament

```
from LACAN import scotland as sc
```


