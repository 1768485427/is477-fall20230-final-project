# is477-fall20230-final-project: Wine Dataset Analysis
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10297836.svg)](https://doi.org/10.5281/zenodo.10297836)

# Overview
We chose the wine dataset from the UCI Machine Learning archive: https://archive.ics.uci.edu/datasets. This dataset results from a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determines the quantities of 13 constituents found in each of the three types of wines. 

The following are the 13 variables: 
1) Alcohol
2) Malic acid
3) Ash
4) Alcalinity of ash  
5) Magnesium
6) Total phenols
7) Flavanoids
8) Nonflavanoid phenols
9) Proanthocyanins
10) Color intensity
11) Hue
12) OD280/OD315 of diluted wines
13) Proline 

We conducted a summary statistics analysis for the dataset. There are 13 features, and we compute the average for every feature in the dataset. We then find values smaller than the average and equal to or larger than the average for each feature. The separated values are stored for further reference. 

# Contributions
**Yuchen Wang's contribution**: 
1. Create a new GitHub repository 
2. Write prepare_data.py
3. Wrtie profile.py,
4. write analysis.py 
5. Create the Dockerfile
6. Create workflow visualization
7. Configure GitHub integration with Zenodo
8. Add the Zenodo DOI badge to repository 
9. Choose the appropriate License. 

**Jiawei Wang's contribution**: 
1. Write analysis.py 
2. Create Snakefile and visualization 
3. Create requirment.txt file 
4. Create the README.md 
5. Create .zenodo.json 

# Analysis
Here are the result after comapring the features with their average: 
1. For *Alcalinity_of_ash*, there are 88 less than average, and 90 more or equal to average
2. For *Alcohol*, there are 86 less than average, and 92 more or equal to average
3. For *Ash*, there are 92 less than average, and 86 more or equal to average
4. For *Color_intensity*, there are 100 less than average, and 78 more or equal to average
5. For *Flavanoids*, there are 82 less than average, and 96 more or equal to average
6. For *Hue*, there are 84 less than average, and 94 more or equal to average
7. For *Magnesium*, there are 97 less than average, and 81 more or equal to average
8. For *Malicacid*, there are 111 less than average, and 67 more or equal to average
9. For *Nonflavanoid_phenols*, there are 96 less than average, and 0 more or equal to average
10. For *Total_phenols*, there are 86 less than average, and 96 more or equal to average
11. For *Proanthocyanins*, there are 94 less than average, and 84 more or equal to average
12. For *Proline*, there are 107 less than average, and 71 more or equal to average

# Workflow
<img src="graph.png" width="1000" height = '400'>
We recommend to downlowad the picture to ensure the you can check the picture clearly because there are too much dataset include in this picture. 

# Reproducing
1. To set up the environment. The firs thing is we need to have a git account.
2. Go to https://github.com/signup, You’ll be prompted to enter your email address, create a password, select a username, and decide whether to receive product updates. Follow the instructions to verify your account and select “Submit”
3. Than we need a complier to run the code. The VS code would be a good choice to run the code and access dataset. Download and install VS Code for your Operating System：Go to https://code.visualstudio.com/download
4. After having the VS code. We need to install the python 3.0 if you don't have it on your environment. Go to https://www.python.org/downloads/   From the command line, confirm your Python version
5. To install Python support for VS Code:
     Select the Extensions button
     Search for Python
     Install the Python extension for Visual Studio Code
6. After having the github account, going to the github page: https://github.com/1768485427/is477-fall20230-final-project and downloa the codes and datasets.
7. After that, you need to install the the requests, pandas, matplotlib, scikit-learn, and snakemake. The requirements.txt provide the tools you need to install. In order to install these packages, you need to do this command: pip install requests 
8. And same to other packages. By accepting datasets you need, you only need to simply run the prepare_data.py and datasets will be downloaded automatically.It will also compare the integrity of the dataset automatically for you.
9. In the scripts file, there is one py file called analysis.py. You can run the code in this file. The results of the analysis of the dataset will be stored automatically in to the result file. 

# License
> - Software license: MIT：
Since we are welcome people to use and share our sofware without too much resitriction. So we choose the MIT as our Software License. 
> - Data license: CC BY 4.0：
The data set allows for the sharing and adaptation of the datasets for any purpose, provided that the appropriate credit is given.

# References
> - Wine Dataset. (1991). UCI Machine Learning Repository. https://archive.ics.uci.edu/dataset/109/wine