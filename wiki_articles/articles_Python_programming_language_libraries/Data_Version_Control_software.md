# Data Version Control (software)

## Metadata
- **Last Updated:** 2024-12-03 08:02:02 UTC
- **Original Article:** [Data Version Control (software)](https://en.wikipedia.org/wiki/Data_Version_Control_(software))
- **Language:** en
- **Page ID:** 71925313

## Summary
DVC is a free and open-source, platform-agnostic version system for data, machine learning models, and experiments. It is designed to make ML models shareable, experiments reproducible, and to track versions of models, data, and pipelines. DVC works on top of Git repositories and cloud storage.
The first (beta) version of DVC 0.6 was launched in May 2017. In May 2020, DVC 1.0 was publicly released by Iterative.ai.

## Categories
This article belongs to the following categories:

- Category:2017 software
- Category:Articles with short description
- Category:Data mining and machine learning software
- Category:Free software programmed in Python
- Category:Official website not in Wikidata
- Category:Python (programming language) libraries
- Category:Python (programming language) software
- Category:Short description matches Wikidata
- Category:Software using the Apache license

## Table of Contents

- Overview
- DVC and Git
- Features
- The DVC VS Code extension
- History
- Alternative solutions to DVC
- References
- External links

## Content

DVC is a free and open-source, platform-agnostic version system for data, machine learning models, and experiments. It is designed to make ML models shareable, experiments reproducible, and to track versions of models, data, and pipelines. DVC works on top of Git repositories and cloud storage.
The first (beta) version of DVC 0.6 was launched in May 2017. In May 2020, DVC 1.0 was publicly released by Iterative.ai.

Overview
DVC is designed to incorporate the best practices of software development into Machine Learning workflows. It does this by extending the traditional software tool Git by cloud storages for datasets and Machine Learning models.
Specifically, DVC makes Machine Learning operations:   

Codified: it codifies datasets and models by storing pointers to the data files in cloud storages.
Reproducible: it allows users to reproduce experiments, and rebuild datasets from raw data. These features also allow to automate the construction of datasets, the training, evaluation, and deployment of ML models.

DVC and Git
DVC stores large files and datasets in separate storage, outside of Git. This storage can be on the user’s computer or hosted on any major cloud storage provider, such as Amazon S3, Google Cloud Storage, and Microsoft Azure Blob Storage. DVC users may also set up a remote repository on any server and connect to it remotely.
When a user stores their data and models in the remote repository, text file is created in their Git repository which points to the actual data in remote storage.

Features
DVC's features can be divided into three categories: data management, pipelines, and experiment tracking.

Data management
Data and model versioning is the base layer of DVC for large files, datasets, and machine learning models. It allows the use of a standard Git workflow, but without the need to store those files in the repository. Large files, directories and ML models are replaced with small metafiles, which in turn point to the original data. Data is stored separately, allowing data scientists to transfer large datasets or share a model with others.
DVC enables data versioning through codification. When a user creates metafiles, describing what datasets, ML artifacts and other features to track, DVC makes it possible to capture versions of data and models, create and restore from snapshots, record evolving metrics, switch between versions, etc.
Unique versions of data files and directories are cached in a systematic way (also preventing file duplication). The working datastore is separated from the user’s workspace to keep the project light, but stays connected via file links handled automatically by DVC.

Pipelines
DVC provides a mechanism to define and execute pipelines. Pipelines represent the process of building ML datasets and models, from how data is preprocessed to how models are trained and evaluated. Pipelines can also be used to deploy models into production environments.
DVC pipeline is focused on the experimentation phase of the ML process. Users can run multiple copies of a DVC pipeline by cloning a Git repository with the pipeline or running ML experiments. They can also record the workflow as a pipeline, and reproduce it in the future.
Pipelines are represented in code as yaml  configuration files. These files define the stages of the pipeline and how data and information flows from one step to the next.
When a pipeline is run, the artifacts produced by that pipeline are registered in a dvc.lock file. The lockfile records the stages that were run, and stores a hash of the resulting output for each stage. Not only is it a record of the execution of the pipeline, but is also useful when deciding which steps must be rerun on subsequent executions of the pipeline.

Experiment tracking
Experiment tracking allows developers to explore, iterate and compare different machine learning experiments.
Each experiment represents a variation of a data science project defined by changes in the workspace. Experiments maintain a link to the commit in the current branch (Git HEAD) as their parent or baseline. However, they do not form part of the regular Git tree (unless they are made persistent). This stops temporary commits and branches from overflowing a user's repository.
Common use cases for experiments are:

Comparison of model architectures
Comparison of training or evaluation datasets
Selection of model hyperparameters
DVC experiments can be managed and visualized either from the VS Code IDE or online using Iterative Studio. Visualization allows each user to compare experiment results visually, track plots and generate them with library integrations.
DVC offers several options for using visualization in a regular workflow:

DVC can generate HTML files that include interactive plots from data series in JSON, YAML, CSV, or TSV format
DVC can keep track of image files produced as plot outputs from the training/evaluation scripts
DVCLive integrations can produce plots automatically during the training

The DVC VS Code extension
In 2022, Iterative released a free extension for Visual Studio Code (VS Code), a source-code editor made by Microsoft, which provides VS Code users with the ability to use DVC in their editors with additional user interface functionality.

History
In 2017, the first (beta) version of DVC 0.6 was publicly released (as a simple command line tool). It allowed data scientists to keep track of their machine learning processes and file dependencies in the simple form of git-like commands. It also allowed them to transform existing machine learning processes into reproducible DVC pipelines. DVC 0.6 solved most of the common problems that machine learning engineers and data scientists were facing: the reproducibility of machine learning experiments, as well as data versioning and low levels of collaboration between teams.
Created by ex-Microsoft data scientist Dmitry Petrov, DVC aimed to integrate the best existing software development practices into machine learning operations. 
In 2018, Dmitry Petrov together with Ivan Shcheklein, an engineer and entrepreneur, founded Iterative.ai, an MLOps company that continued the development of DVC. Besides DVC, Iterative.ai is also behind open source tools like CML, MLEM, and Studio, the enterprise version of the open source tools.
In June 2020, the Iterative.ai team released DVC 1.0. New features like multi-stage DVC files, run cache, plots, data transfer optimizations, hyperparameter tracking, and stable release cycles were added as a result of discussions and contributions from the community.
In March 2021, DVC released DVC 2.0, which introduced ML experiments (experiment management), model checkpoints and metrics logging.
ML experiments: To solve the problem of Git overhead, when hundreds of experiments need to be run in a single day and each experiment run requires additional Git commands, DVC 2.0 introduced the lightweight experiments feature. It allows its users to auto-track ML experiments and capture code changes.
This eliminated the dependence upon additional services by saving data versions as metadata in Git, as opposed to relegating it to external databases or APIs.
ML model checkpoints versioning: The new release also enables versioning of all checkpoints with corresponding code and data.
Metrics logging: DVC 2.0 introduced a new open-source library DVC-Live that would provide functionality for tracking model metrics and organizing metrics in a way that DVC could visualize with navigation in Git history.

Alternative solutions to DVC
There are several open source projects that provide similar data version control capabilities to DVC, such as: Git LFS, Dolt, Nessie, and lakeFS. These projects vary in their fit to the different needs of data engineers and data scientists such as: scalability, supported file formats, support in tabular data and unstructured data, volume of data that are supported, and more.

References
External links
Official website
dvc on GitHub
VS Code extension

## Archive Info
- **Archived on:** 2024-12-15 20:39:14 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 8018 bytes
- **Word Count:** 1245 words
