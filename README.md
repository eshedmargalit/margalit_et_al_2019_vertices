# xl-vertices

## Code for the X-junction L-vertex project of the [IUL](geon.usc.edu)
### Eshed Margalit and Sarah Herald

## Workflow
_From raw data to figures_
Note: this pipeline uses Python, MATLAB, and R, mostly for historical reasons. Only one MATLAB file is still used, and that could be somewhat readily replaced by Python.

0. **Setting environment variables**

    To tell the scripts where to find data, set an environment variable called `XL_ROOT`.
    ```bash
	export XL_ROOT='/Users/eshed/projects/xl-vertices'
	```

1. **Copying valid logs to `processed_data`**

    ```bash
	python get_valid_logs_1.py
	```

2. **Collapse all data into one big table to be read in by R (do this in MATLAB)**

    ```MATLAB
	process_logs_2.m
	```

3. **Run analyses and make figures (R)**
	Run the R-MarkDown file `x-vertices_analysis.Rmd`
