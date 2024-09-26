# RibonanzaNet_EternaBench_Eval
Finetuning and evaluating RibonanzaNet on EternaBench Datasets

Three different benchmark datasets were evaluated: 
* Secondary Structure datasets
* Chemical Mapping Datasets
* Riboswitch Equilibrium Constant Datasets

Step by step instructions on how I used .json files generated from provided colab notebooks to evaluate RibonanzaNet (a deep learning model implemented in Pytorch) on eternabench datasets, and compare with other packages: 
* Step 1: Run predictions in google colab notebooks located in **SS-evaluation**, **CM-evaluation**, and **RS-evaluation**
* Step 2: Create a .json file with formatting identical to calculations from other datasets in EternaBench archived git repository (embedded in colab notebooks used for *Step 1*) 
* Step 3: Clone EternaBench git repository, update files located in **scoringscripts**, **compilingscripts**, and **generateplots** that have been patched for recent package updates. 
* Step 3: Run **scoringscripts** from EternaBench github repository to get bootstrapped statistical results.
* Step 4: Run **compilingscripts** from EternaBench github repository to evaluate model against other secondary structure prediction algorithms.
* Step 5: Use **generateplots** jupyter notebooks in **analysis** folder from EternaBench github repository to generate heatmaps that display the results. 

