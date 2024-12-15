# Data Version Control (software)

## Article Metadata

- **Last Updated:** 2024-12-15T03:43:28.454129+00:00
- **Original Article:** [Data Version Control (software)](https://en.wikipedia.org/wiki/Data_Version_Control_(software))
- **Language:** en
- **Page ID:** 71925313

## Summary

DVC is a free and open-source, platform-agnostic version system for data, machine learning models, and experiments. It is designed to make ML models shareable, experiments reproducible, and to track versions of models, data, and pipelines. DVC works on top of Git repositories and cloud storage.
The first (beta) version of DVC 0.6 was launched in May 2017. In May 2020, DVC 1.0 was publicly released by Iterative.ai.

## Categories

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

## Related Articles

### Internal Links

- [Amazon S3](https://en.wikipedia.org/wiki/Amazon_S3)
- [Apache License](https://en.wikipedia.org/wiki/Apache_License)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Artifact (software development)](https://en.wikipedia.org/wiki/Artifact_(software_development))
- [Cache (computing)](https://en.wikipedia.org/wiki/Cache_(computing))
- [Cloud storage](https://en.wikipedia.org/wiki/Cloud_storage)
- [Code](https://en.wikipedia.org/wiki/Code)
- [Computer file](https://en.wikipedia.org/wiki/Computer_file)
- [Configuration file](https://en.wikipedia.org/wiki/Configuration_file)
- [Data](https://en.wikipedia.org/wiki/Data)
- [Data and information visualization](https://en.wikipedia.org/wiki/Data_and_information_visualization)
- [Data management](https://en.wikipedia.org/wiki/Data_management)
- [Data science](https://en.wikipedia.org/wiki/Data_science)
- [Data set](https://en.wikipedia.org/wiki/Data_set)
- [Data storage](https://en.wikipedia.org/wiki/Data_storage)
- [Free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software)
- [Git](https://en.wikipedia.org/wiki/Git)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Google Cloud Storage](https://en.wikipedia.org/wiki/Google_Cloud_Storage)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Container format](https://en.wikipedia.org/wiki/Container_format)
- [Microsoft](https://en.wikipedia.org/wiki/Microsoft)
- [Microsoft Azure](https://en.wikipedia.org/wiki/Microsoft_Azure)
- [Pipeline (computing)](https://en.wikipedia.org/wiki/Pipeline_(computing))
- [Pipeline (software)](https://en.wikipedia.org/wiki/Pipeline_(software))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Raw data](https://en.wikipedia.org/wiki/Raw_data)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Server (computing)](https://en.wikipedia.org/wiki/Server_(computing))
- [Software](https://en.wikipedia.org/wiki/Software)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Source-code editor](https://en.wikipedia.org/wiki/Source-code_editor)
- [Training, validation, and test data sets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets)
- [User interface](https://en.wikipedia.org/wiki/User_interface)
- [Visual Studio Code](https://en.wikipedia.org/wiki/Visual_Studio_Code)
- [Workflow](https://en.wikipedia.org/wiki/Workflow)
- [YAML (framework)](https://en.wikipedia.org/wiki/YAML_(framework))

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:43:28.454129+00:00_