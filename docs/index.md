# FAST User Guide

![fast_index](img/fast_index_page.png)

**Welcome to FAST's documentation**
=========================================

**FAST** is an end-to-end and unsupervised earthquake detection pipeline. It is a useful tool for seismologists to extract more small earthquakes from continuous seismic data.

**Github development page:**
------------------------
[https://github.com/stanford-futuredata/FAST](https://github.com/stanford-futuredata/FAST)

**Contents**
------------
1.  [FAST Overview](fast_overview.md).  
   **Click here for a summary of the FAST algorithm and why you might want to use it on your seismic data.**

2.  Install  
    **Go here to learn how to install and run the FAST software on your computer.**

    1.  [Google Colab](setup_colab.md)

    2.  [Linux](setup_linux.md)

    3.  [Docker](setup_docker.md)

3.  [Tutorial](tutorial.md)  
    **Learn how FAST detects earthquakes on the Hector Mine data set.**

4.  How to Set Parameters  
    **Click here to learn how to test FAST on your own data sets.**

    1.  [FAST Checklist](FAST_checklist.md)

    2.  [Getting Seismic Data](get_seismic_data.md)
   
    3.  [Input and Preprocessing](input_and_preprocess.md)

    4.  [Fingerprint](f_p.md)

    5.  [Similarity Search](sim_search.md)

    6.  [Network Detection](network_detection.md)  

    7.  [FAST Output](FAST_output.md)  

    8.  [Phase Picking](phase_picking.md)  

    9.  [Earthquake Location](earthquake_location.md)  

    10. [Example Parameters](ex_params_intro.md)  
        **Click here to see data sets FAST has been used on to detect earthquakes.**

5.  [References](references.md)  
    **Read publications about FAST here.**


<!-- ## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files. -->
