# Dask (software)

## Metadata
- **Last Updated:** 2024-12-03 07:53:54 UTC
- **Original Article:** [Dask (software)](https://en.wikipedia.org/wiki/Dask_(software))
- **Language:** en
- **Page ID:** 60583826

## Summary
Dask is an open-source Python library for parallel computing. Dask scales Python code from multi-core local machines to large distributed clusters in the cloud. Dask provides a familiar user interface by mirroring the APIs of other libraries in the PyData ecosystem including: Pandas, scikit-learn and NumPy. It also exposes low-level APIs that help programmers run custom algorithms in parallel.
Dask was created by Matthew Rocklin in December 2014 and has over 9.8k stars and 500 contributors on GitHub.
Dask is used by retail, financial, governmental organizations, as well as life science and geophysical institutes. Walmart, Wayfair, JDA, GrubHub, General Motors, Nvidia, Harvard Medical School, Capital One and NASA are among the organizations that use Dask.

## Categories
This article belongs to the following categories:

- Category:All articles with dead external links
- Category:Articles with dead external links from August 2024
- Category:Articles with permanently dead external links
- Category:Articles with short description
- Category:Parallel computing
- Category:Python (programming language) libraries
- Category:Short description is different from Wikidata

## Table of Contents

- Overview
- Dask collections
- High-level collections
- Low-level collections
- Scheduling
- Dask-ML
- Integrations
- Applications
- History
- References
- External links

## Content

Dask is an open-source Python library for parallel computing. Dask scales Python code from multi-core local machines to large distributed clusters in the cloud. Dask provides a familiar user interface by mirroring the APIs of other libraries in the PyData ecosystem including: Pandas, scikit-learn and NumPy. It also exposes low-level APIs that help programmers run custom algorithms in parallel.
Dask was created by Matthew Rocklin in December 2014 and has over 9.8k stars and 500 contributors on GitHub.
Dask is used by retail, financial, governmental organizations, as well as life science and geophysical institutes. Walmart, Wayfair, JDA, GrubHub, General Motors, Nvidia, Harvard Medical School, Capital One and NASA are among the organizations that use Dask.

Overview
Dask has two parts: 

Big data collections (high level and low level)
Dynamic task scheduling
Dask's high-level parallel collections – DataFrames, Bags, and Arrays – operate in parallel on datasets that may not fit into memory.
Dask’s task scheduler executes task graphs in parallel. It can scale to thousand-node clusters. This powers the high-level collections as well as custom, user-defined workloads using low-level collections.

Dask collections
Dask supports several user interfaces called high-level and low-level collections:

High-level
Dask Array: Parallel NumPy arrays
Dask Bag: Parallel Python lists
Dask DataFrame: Parallel Pandas DataFrames
Machine Learning: Parallel scikit-learn
Others from external projects, like Xarray

Low-level
Delayed: Parallel function evaluation
Futures: Real-time parallel function evaluation
Under the hood, each of these user interfaces adopts the same parallel computing machinery.

High-level collections
Dask's high-level collections are the natural entry point for users who are interested in scaling up their pandas, NumPy or scikit-learn workload. Dask’s DataFrame, Array and Dask-ML are alternatives to Pandas DataFrame, Numpy Array and scikit-learn respectively with slight variations to the original interfaces.

Dask Array
Dask Array is a high-level collection that parallelizes array-based workloads and maintains the familiar NumPy API, such as slicing, arithmetic, reductions, mathematics, etc., making it easy for Numpy users to scale up array operations.
A Dask array comprises many smaller n-dimensional Numpy arrays and uses a blocked algorithm to enable computation on larger-than-memory arrays. During an operation, Dask translates the array operation into a task graph, breaks up large Numpy arrays into multiple smaller chunks, and executes the work on each chunk in parallel. Results from each chunk are combined to produce the final output.

Dask DataFrame
Dask DataFrame is a high-level collection that parallelizes DataFrame based workloads. A Dask DataFrame comprises many smaller Pandas DataFrames partitioned along the index. It maintains the familiar Pandas API, making it easy for Pandas users to scale up DataFrame workloads. During a DataFrame operation, Dask creates a task graph and triggers operations on the constituent DataFrames in a manner that reduces memory footprint and increases parallelism through sharing and deleting of intermediate results.

Dask Bag
Dask Bag is an unordered collection of repeated objects, a hybrid between a set and a list. Dask Bag is used to parallelize computation of semi-structured or unstructured data, such as JSON records, text data, log files or user-defined Python objects using operations such as filter, fold, map and groupby. Dask Bags can be created from an existing Python iterable or can load data directly from text files and binary files in the Avro format.

Low-level collections
The Dask low-level interface allows for more customization. It is suitable for data that does not fall within the scope of a Dask DataFrame, Bag or Array. Dask has the following low-level collections:

Delayed: Parallel function evaluation
Futures: Real-time parallel function evaluation

Delayed
Dask delayed is an interface used to parallelize generic Python code that does not fit into high level collections like Dask Array or Dask DataFrame. Python functions decorated with Dask delayed adopt a lazy evaluation strategy by deferring execution and generating a task graph with the function and its arguments. The Python function will only execute when .compute is invoked. Dask delayed can be used as a function dask.delayed or as a decorator @dask.delayed.

Futures
Dask Futures, an immediate (non-lazy) alternative to Dask delayed, provides a real-time task framework that extends Python’s concurrent.futures interface, which provides a high-level interface for asynchronous execution of callables.
It is common to combine high and low-level interfaces. For example, users can run Dask array/bag/dataframe to load and pre-process data, then switch to Dask delayed for a custom algorithm that is specific to their domain, then switch back to Dask array/dataframe to clean up and store results.

Scheduling
Dask’s high and low-level collections create a directed acyclic graph of tasks, which represents the relationship between computation tasks. A node in a task graph represents a Python function that performs a unit of computation and an edge represents the data dependency between the upstream and downstream task. After a task graph is generated, the task scheduler manages the workflow based on the given task graph by assigning tasks to workers in a manner that improves parallelism and respects the data dependencies.
Dask provides two families of schedulers: single-machine scheduler and distributed scheduler.

Single-machine scheduler
A single-machine scheduler is the default scheduler which provides basic features on local processes or thread pool and is meant to be used on a single machine. It is simple and cheap to use but does not scale.

Local threads
A threaded scheduler leverages Python’s concurrent.futures.ThreadPoolExecuter to execute computations. It has a low memory footprint and does not require any setup. As all the computations occur in the same process, threaded schedulers incur minimal task overhead and no cost from transfer of data between tasks. Due to Python’s Global Interpreter Lock, local threads provide parallelism only when the computation is primarily non-Python code, which is the case for Pandas DataFrame, Numpy arrays or other Python/C/C++ based projects.
Local process
A multiprocessing scheduler leverages Python’s concurrent.futures.ProcessPoolExecutor to execute computations. Tasks and its dependencies are transferred from the main process to a local process, executed, and the results are transferred back to the main process. This allows bypassing of issues with Python’s Global Interpretable Lock and provides parallelism for computation tasks with primarily Python code. However, transferring data between the main and local processes degrades performance, especially in cases when the size of data transferred is large.
Single thread
A single threaded scheduler executes computation with no parallelism. It is used for debugging purposes.

Distributed scheduler
Dask’s distributed scheduler can be set up on a local machine or scale out on a cluster. Dask can work with resource managers, such as Hadoop YARN, Kubernetes, or PBS, Slurm, SGD and LSF for High Performance Computing (HPC) clusters.

Dask-ML
Dask-ML is compatible with scikit-learn’s estimator API of fit, transform and predict and is well integrated with machine learning and deep learning frameworks such XGBoost, LightGBM, PyTorch, Keras, and TensorFlow through scikit-learn compatible wrappers.

Integrations
scikit-learn integration
Selected scikit-learn estimators and utilities can be parallelized through executing jobs across multiple CPU cores using the Joblib library. The number of processes are determined by the n_jobs parameters. By default, the Joblib library uses loky as its multi-processing back-end. Dask offers an alternative Joblib backend which is useful for scaling of Joblib-backed scikit-learn algorithms out to a cluster of machines for compute constrained workloads.
For memory constrained workloads, Dask offers alternatives, such as Parallel Meta-estimators for parallelizing and scaling out tasks that are not parallelized within scikit-learn and Incremental Hyperparameter Optimization for scaling hyper-parameter search and parallelized estimators.

XGBoost & LightGBM integrations
XGBoost and LightGBM are popular algorithms that are based on Gradient Boosting and both are integrated with Dask for distributed learning. Dask does not power XGBoost or LightGBM, rather it facilitates setting up of the cluster, scheduler, and workers required then hands off the data to the machine learning framework to perform distributed training.
Training an XGBoost model with Dask, a Dask cluster is composed of a central scheduler and multiple distributed workers, is accomplished by spinning up an XGBoost scheduler in the same process running the Dask central scheduler and XGBoost worker in the same process running the Dask workers. Dask workers then hand over the Pandas DataFrame to the local XGBoost worker for distributed training.

PyTorch integration
Skorch is a scikit-learn compatible wrapper for PyTorch, which enables Dask-ML to be used together with PyTorch.

Keras and TensorFlow integrations
SciKeras is an scikit-learn compatible wrapper for Keras models which enables Dask-ML to be used with Keras.

Applications
Retail
Examples of retail use include:

Walmart uses Dask for forecasting the demand for 500,000,000 store-item combinations. To provide in-demand items in sufficient quantities at all their outlets, they run large computations. Using RAPIDS and XGBoost, supported by Dask, they have reached 100x acceleration.
Blue Yonder uses Dask to process terabytes of data on a daily basis. They can write Pandas-like code in Dask, which can then be pushed directly to production. This helps keep their feedback cycles short and waste low.
Grubhub uses Dask alongside TensorFlow for pre-processing and ETL. Dask allows them to continue working in Python and get the functionalities needed.

Life sciences
Dask is used for high resolution, 4-dimensional, cellular imagery by Harvard Medical School, Howard Hughes Medical Institute, Chan Zuckerberg Initiative, and the UC Berkeley Advanced Bioimaging Center. They record the evolution and movements of a 3-dimensional cell over time, in maximum detail. This generates large amounts of data that is difficult to analyze with traditional methods. Dask helps them scale their data analysis workflows with its API that resembles NumPy, Pandas, and scikit-learn code.
Dask is also used at the Novartis Institute for Biomedical Research to scale machine learning prototypes.

Finance industry
Capital One uses Dask to accelerate ETL and ML pipelines
Barclays uses Dask for financial system modeling

Geophysical sciences
Dask is used in Climate Science, Energy, Hydrology, Meteorology, and Satellite Imaging by companies such as NASA, LANL, PANGEO: Earth Science and the UK Meteorology Office.
Oceanographers produce massive simulated datasets of the Earth’s oceans and researchers can look at large seismology datasets from sensors around the world, collect a large number of observations from satellites and weather stations, and run big simulations.

Software libraries
Dask is integrated into many libraries, such as Pangeo and xarray; time series software like Prophet and tsfresh; ETL/ML software like scikit-learn, RAPIDS, and XGBoost; workflow management tools like Apache Airflow and Prefect.

History
2014–2015
Dask was originally developed at Continuum Analytics, a for-profit Python consulting company that eventually became Anaconda, Inc., the creator of many open-source packages and the Anaconda Python distribution. Dask grew out of the Blaze project, a DARPA funded project to accelerate computation in open source.
Blaze was an ambitious project that tried to redefine computation, storage, compression, and data science APIs for Python, led originally by Travis Oliphant and Peter Wang, the co-founders of Anaconda. However, Blaze’s approach of being an ecosystem-in-a-package meant that it was harder for new users to easily adopt.
Instead of rewriting a software ecosystem, Dask’s team intended to augment the existing one with the right component. With this idea in mind, on December 21, 2014 Matthew Rocklin created Dask. The purpose of Dask was originally to parallelize NumPy so that it could use one full workstation computer, which was common in finance shops at the time.

2015–2017
The first projects to really adopt Dask were Xarray(commonly used in geo sciences) and Scikit-Image (commonly used in image processing). Dask was integrated into Xarray within a few months of being created. It provided Dask with its first user community, which remains to this day.
Understanding that there is demand for a lightweight parallelism solution for Pandas DataFrames and machine learning tools, such as scikit-learn, Dask quickly evolved to support other projects as well.

2018
Since 2018, other teams and institutions in academia, tech companies, and large corporations such as NASA, UK Met Office, Blue Yonder and Nvidia, became interested in Dask and began integrating it into their systems.
Dask received support from a diverse set of sources: the US Government (DARPA grant), the Gordon and Betty Moore Foundation, Anaconda, NSF, NASA (US research grants with collaborations like Pangeo) and Nvidia.

2020–present
In 2020, Matthew Rocklin founded Coiled Computing, Inc. to provide further support for Dask development and enable companies to deploy Dask clusters in the cloud. In May 2021, the company raised $21 million in series A funding led by Bessemer Venture Partners.

References
External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 20:27:26 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 13886 bytes
- **Word Count:** 2041 words
