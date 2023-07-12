# The Method FReE for Dimensionality Reduction in Big Data

### This repository contains the results, code, datasets and tools, used to compare two techniques for the Unsupervised Dimensionality Reduction task: (a) the standard and data variance-based approaches (PCA, SVD, and KPCA), and; (b) An alternative Fractal-based solution (FReE).

You can find the materials detailed bellow:

1.	**codes**: Here, all the codes regarding to the Unsupervised Dimensionality Reduction  compared techniques are listed. You can access the FReE (in Java), PCA/SVD (in Java), and KPCA (in Python);
2.	**datasets**: This directory has a file listing all the datasets used. Additionally, it has all the expressions used to generate the new redundantes datasets tested in our experiments;
3.	**results**: This directory has detailed results obtained by our experimental evaluation. For KPCA and PCA/SVD, the explained variance are described in `.json` files; For FReE, there are the log generated, and table with detailed configuration of noise, for the evaluated correlations.
4.	**tools**: This directory contains the tools used to help us in the experiments settings: Automatic Generator of Redundant Datasets, Script to create expressions, and so on.
