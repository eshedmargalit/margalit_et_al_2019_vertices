# Visual Noise Consisting of X-Junctions Has Only a Minimal Effect on Object Recognition 
### Eshed Margalit, Sarah B. Herald, Emily X. Meschke, Isabel Irawan, Rafael Maarek, and Irving Biederman

## Read the [preprint](https://psyarxiv.com/cje3y/)!
## How does adding noise to line drawings affect our recognition?
In 1968, Adolfo Guzman published an influential dissertation in which he described how vertices in contours can be used to segment complex shapes, e.g., identifying the volumes in this drawing below:

![Guzman's "Bridge"](https://github.com/eshedmargalit/margalit_et_al_2019_vertices/blob/master/paper_figures/fig1.png)

Guzman predicted that L-vertices (see the upper right corner of surface #15 above) would be more important for segmentation of volumes than X-vertices, where two lines intersect but do not terminate. We tested this prediction by having subjects verbally name line drawings under 5 conditions, shown below. Of particular interest are the CDX condition and the CDL condition, as they are exactly matched except that the noisy line segments are translated slightly between conditions.

![Example Stimuli](https://github.com/eshedmargalit/margalit_et_al_2019_vertices/blob/master/paper_figures/fig3.png)

We evaluated how quickly and accurately subjects named drawings in each condition, then assessed the relative cost of adding visual noise in the form of X-vertices or L-vertices. We found that adding L-vertices to a drawing was far more disruptive than adding X-vertices; the cost on subjects' reaction times (see below) was twice as high for our CDL condition than the CDX condition. Subjects were also twice as likely to make an error in naming in this condition!

![Reaction Times](https://github.com/eshedmargalit/margalit_et_al_2019_vertices/blob/master/paper_figures/fig4.png)

![Error Rates](https://github.com/eshedmargalit/margalit_et_al_2019_vertices/blob/master/paper_figures/fig5.png)

Our results support Guzman's insights from computer vision over 50 years ago. We argue that these insights, founded in an appreciation for explicit shape-based models of perception, can complement ongoing work in modern computer vision, e.g., deep convolutional neural networks for perception. For more information, please check out our [preprint](https://psyarxiv.com/cje3y/), and feel free to contact me with any questions or comments.

## Running the scripts
###### _From raw data to figures_

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
