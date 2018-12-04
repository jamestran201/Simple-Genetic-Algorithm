# Simple-Genetic-Algorithm

## Installing dependencies
Run the following command in the project folder to install dependencies. If your system has both Python 2 and 3 installed, run `pip` if you are using Python 2 and `pip3` for Python 3.  
```pip install -r dependencies.txt```

## Run the SGA
1. In the project directory, run: `python SGA-functions.py`. Use `python3` instead of `python` if you have both Python 2 and Python 3 installed. 
2. Follow the prompt and select the objective function to use and configurations.  
3. Once the algorithm finished running, some graphs and a summary will be created and stored in the `results/` directory.  

## Visualize the fitness values live
1. Go to the project directory and run the command: `bokeh serve --show live_plot.py`. 
2. A new tab will pop up in the browser with an empty plot. 
3. In a separate terminal, go to the project directory and follow the steps in the section above to run the algorithm.  
4. The mean and minimum fitness values of each generation will be displayed on the plot as the algorithm runs.  
5. If you are running the algorithm multiple times, the browser tab has to be refreshed before each run for the new data to be displayed.  
