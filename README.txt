Group_10
-----------------
Anamarija Eres
Dominik Kos
Ema Ilic
Akos Tanczos
-----------------
Welcome to our code!
This file explains the 
-----------------
FINAL PROJECT STATEMENT

-----------------
PYTHON NOTEBOOKS USED FOR THE PROJECT

The prefixes of the filenames help identify the chapter in the exercise statement the given file solves.
--> 2_data_harvesting.ipynb
DESCRIPTION: 
This notebook is used to harvest the data by scraping investing.com. If the notebook's cells are run, the data belonging to the assets of interests will be saved in the same folder, with [asset-name].csv filename. This files include all historic data in the specific date range, not only the one that will be used later. 
HOW TO RUN:
This notebook was written in Python 3.7.10. It uses selenium as the scraping library with a Firefox driver.

-->3_0Missing_Value_Treatment.ipynb
DESCRIPTION:
This notebook was used for cleaning the data and preparing it for 
further use. Namely, in this notebook, the missing date values
(relevant for holidays and weekends, such as 01-01-2020, 31-01-2020...
) were artificially added to the dataset. Initially, there were
some missing values only in the Vol. attribute, but with the addition
of the extra dates, there were significantly more missing values.
Vol and Change atrtibutes were initially string type, and were
later on quantified. The missing values were filled using the
interpolation method.
For the sake of conciseness, only the notebook relevant for Gold asset
is included and described here. This same  code was later on run on
the other assets, too.
HOW TO RUN:
This notebook was written in Python 3.7.10, in the google colab 
platform. In order to run it, it is necessary to modify the path to 
the relevant google drive folder of the person trying to run the code.

-->3_1portfolio_allocation.py
DESCRIPTION: 
This notebook does the Portfolio Allocation. It automatically 
generates the portfolio combinations with the difference of 0.05 (5%).
HOW TO RUN:
Run the code with python3.7.

--> 3_2trading_methodologies.ipynb
DESCRIPTION: 
The notebook assigns the different trading methodologies to each portfolio allocations. Thus, from 10626 portfolio allocations there will be 10626*4=42504 entries in the trading_methodologies.csv file.
HOW TO RUN:
All cells of the jupyter-notebook should be run. 

-->3_3Cost_Volatility.ipynb
This notebook applies different trading methodologies for different 
portfolio allocations in order to find the volatility metric for each of
the portfolio allocations, using the training methodologies, with and
without rebalance. 

HOW TO RUN:
This notebook was written in Python 3.7.10, in the google colab 
platform. In order to run it, it is necessary to modify the path to 
the relevant google drive folder of the person trying to run the code.
Also the necessary CSV files need to be added to the same path.

--> 4_1return.ipynb
DESCRIPTION:
This notebook applies different trading methodologies for different
portfolio allocations in order to find the return metric for each of
the portfolio allocations, using the training methodologies, with and
without rebalance. 

HOW TO RUN:
This notebook was written in Python 3.7.10, in the google colab 
platform. In order to run it, it is necessary to modify the path to 
the relevant google drive folder of the person trying to run the code.
Also the necessary CSV files need to be added to the same path.

--> 4_2return_risk.ipynb
DESCRIPTION:
This notebook was done with the purpose of visualizing the data 
created in previous tasks.

HOW TO RUN:
This notebook was also written in colab, so the process for running it
is the same as described earlier. 

--> 4_3financialAdvisoring.ipynb
DESCRIPTION:
This notebook is used to answer the questions in chapter 4. The detailed rationale behind the decisions can be found in the report, while the data that supports the decision can be found in this notebook.
HOW TO RUN:
Run all the cells. The portfolio_allocations.csv and the files containing the asset prices (with the missing values filled) have to be in the same folder.
