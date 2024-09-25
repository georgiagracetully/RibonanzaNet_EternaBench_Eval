# RibonanzaNet_EternaBench_Eval
Finetuning and evaluating RibonanzaNet on EternaBench Datasets

Three different benchmark datasets were evaluated: 
* Secondary Structure datasets
* Chemical Mapping Datasets
* Riboswitch Equilibrium Constant Datasets

How I used these colab notebooks to evaluate RibonanzaNet (a deep learning model implemented in Pytorch) with these datasets
* Step 1: Run predictions in google colab notebooks
* Step 2: Create a .json file with formatting identical to calculations from other datasets in EternaBench archived git repository
* Step 3: Clone EternaBench git repository, update files located in **scoringscripts**, **compilingscripts**, and **generateplots** that have been patched to match updated changes
* Step 3: Run **scoringscripts** from EternaBench github repository to get bootstrapped statistical results
* Step 4: Run **compilingscripts** from EternaBench github repository to evaluate model against other secondary structure prediction algorithms
* Step 5: Use **generateplots** jupyter notebooks in **analysis** folder from EternaBench github repository to generate heatmaps that display the results

