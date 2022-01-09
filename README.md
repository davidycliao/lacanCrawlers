
## lacanCrawler: An Automation Webcrawler for Extracting Text Data from Parliarmnets

An automation web crawling framework for retrieving for parliarmentay questions and textual statements from the three parliaments from United Kingdom and National Diet of Japan based on Selenium and Chrome browser.

## Structure of the Module (lacanCrawler)

```
bamberg.lacan/
    └── LACAN/           ┌─ House of the Commons
        ├── england.py╶──└─ House of the Lord
        ├── scotlan.py
        ├── nirland.py
        └── japan.py  
```

## Environment Setup

### Step 1: Download `lacanCrawler`

- Before downloading the module, the installation of  [Anaconda Navigator](https://www.anaconda.com/products/individual-b) and [Python>=3.9](https://www.python.org/downloads/release/python-3810/) are required beforehand. The module is hosted on my Github private repository [`davidycliao/lacanCrawler`](https://github.com/davidycliao/lacanCrawler). Please email me to have you accessed as maintainer. Once having access to the repo, you can open the terminal and download `bamberg.lacan` repository by using `git clone`. 

About how to use git and Github, please have a look at this [Tutorial for Beginners](https://www.youtube.com/watch?v=RvnM6EEwp1I). 

```
git clone  git@github.com:davidycliao/lacanCrawler.git
```

- Copy the commands below and paste them into the terminal:

Change the directory by typing `cd` command once `lacanCrawler` repository is downloaded.

```
cd bamberg.lacan
```

- Create the enviroment by using conda and name the enviroment `lacanCrawler`.

```
conda create -n lacan python=3.9
```

### Step 2: Instruction for the Installation of the Required Dependencies

- Activate the pre-named enviroment. Alternatively, the environment for `lacanCrawler` can be opened via [Anaconda Navigator](https://www.anaconda.com/products/individual-b)

```
conda activate lacanCrawler 
```

- Install required modules from `requirements.txt` using `pip` methond.

```
pip install -r requirements.txt   
```

