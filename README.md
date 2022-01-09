
<p align="center">
    <img src="flowchart.png"  style="width:570px;"/>
</p>


## Environment Setup

### Download the LACAN module 

1. Before downloading the module, the installation of  [Anaconda Navigator](https://www.anaconda.com/products/individual-b) and [Python>=3.9](https://www.python.org/downloads/release/python-3810/) are required beforehand. The module is hosted on my Github private repository [`davidycliao`](https://github.com/davidycliao/bamberg.lacan). Please email me to have you accessed as maintainer. Once you have access to the repo, you can open the terminal and download `bamberg.lacan` repository by using `git clone`. 

###### About how to use git and Github, please have a look at this [Tutorial for Beginners](https://www.youtube.com/watch?v=RvnM6EEwp1I). 

```
git clone  git@github.com:davidycliao/bamberg.lacan.git
```

2. Copy the commands below and paste them into the terminal:

```
# Change the directory by typing `cd` command once `bamberg.lacan` repository is downloaded.
cd bamberg.lacan

# Create the enviroment by using conda and name the enviroment `lacan`.
conda create -n lacan python=3.9
```

## Instruction for the Installation of the Required Dependencies

1. Activate the pre-named enviroment. Alternatively, the environment for `bamberg.lacan` can be opened via [Anaconda Navigator](https://www.anaconda.com/products/individual-b)

```
conda activate lacan 
```

2. Install required modules from `requirements.txt` using `pip` methond.

```
pip install -r requirements.txt   
```