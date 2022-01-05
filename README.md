
## Environment Setup

<p align="center">
    <img src="flowchart.png"  style="width:570px;"/>
</p>


1. Need to install [Anaconda Navigator](https://www.anaconda.com/products/individual-b) and [Python>=3.9](https://www.python.org/downloads/release/python-3810/) beforehand. And then, open the terminal and download `bisCrawler` repository by using `git clone`. About how to use git and Github, please have a look at this [Tutorial for Beginners](https://www.youtube.com/watch?v=RvnM6EEwp1I). 

```
git clone  git@github.com:davidycliao/scottish.git
```

2. Copy the commands below and paste them into the terminal:

```
# Change the directory by typing `cd` command once `scottish` repository is downloaded.
cd scotish

# Create the enviroment by using conda and name the enviroment `Scottish`.
conda create -n scottish python=3.9
```

## Instruction

1. Activate the pre-named enviroment. Alternatively, the environment for `scotish` can be opened via [Anaconda Navigator](https://www.anaconda.com/products/individual-b)

```
conda activate Scottish 
```

2. Install the dependencies from `requirements.txt` using `pip` methond.

```
pip install -r requirements.txt   
```

3. Call `Scottish` Moduel in Jupyter Notebook: 

Time periods for selectionsw include: `Session 1`, `Session 2`, `Session 3`, `Session 4`, `Session 5`, `Current Session` and `All Sessions`.


```
from Scottish import scottish_scraper 
```

```
scottish_scraper(session='Session 1')
```


