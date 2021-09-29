# Exploring Traffic Prediction Strategies and their Effect on Emergency Vehicle Routing
This is a repository for all the code used in my MSc Dissertation. 

Everything needed to run the Jupyter Notebook and SUMO simulations is contained within the repository. The only exceptions being:
- An [installation of the SUMO software package](https://www.eclipse.org/sumo/) is required.
- Some variables need to be first created on your local machine. 

In some cells, [storemagic](https://ipython.readthedocs.io/en/stable/config/extensions/storemagic.html) is used to locally store certain objects to save executing computationally expensive code repeatedly. For example, this includes the Linear Regression and Random Forest Scikit-Learn GridSearchCV objects, and all the lists of DataFrames output from the simulations.

Please note, the 80 simulations took about 7 hours to run on a Windows 10 PC with a 4.2GHz Intel i7-7700K processor, so be carefull when executing the notebook.
