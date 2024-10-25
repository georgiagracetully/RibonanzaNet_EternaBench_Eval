# RibonanzaNet_EternaBench_Eval
Finetuning and evaluating RibonanzaNet on EternaBench Datasets

**RibonanzaNet**: (1)	He, S.; Huang, R.; Townley, J.; Kretsch, R. C.; Karagianes, T. G.; Cox, D. B. T.; Blair, H.; Penzar, D.; Vyaltsev, V.; Aristova, E.; Zinkevich, A.; Bakulin, A.; Sohn, H.; Krstevski, D.; Fukui, T.; Tatematsu, F.; Uchida, Y.; Jang, D.; Lee, J. S.; Shieh, R.; Ma, T.; Martynov, E.; Shugaev, M. V.; Bukhari, H. S. T.; Fujikawa, K.; Onodera, K.; Henkel, C.; Ron, S.; Romano, J.; Nicol, J. J.; Nye, G. P.; Wu, Y.; Choe, C.; Reade, W.; Eterna participants; Das, R. Ribonanza: Deep Learning of RNA Structure through Dual Crowdsourcing. bioRxivorg 2024. https://doi.org/10.1101/2024.02.24.581671.

**EternaBench**: (2)	Wayment-Steele, H. K.; Kladwang, W.; Strom, A. I.; Lee, J.; Treuille, A.; Becka, A.; Participants, E.; Das, R. RNA Secondary Structure Packages Evaluated and Improved by High-Throughput Experiments. Nat. Methods 2022, 19 (10), 1234–1242. https://doi.org/10.1038/s41592-022-01605-0.

Three different benchmark datasets were evaluated: 
* Secondary Structure 
* Chemical Mapping 
* Riboswitch Binding Equilibrium Constants

Step by step instructions on how I used .json files generated from provided colab notebooks to evaluate RibonanzaNet (a deep learning model implemented in Pytorch) on eternabench datasets, and compare with other packages: 
* Step 1: Run predictions in google colab notebooks located in **SS-evaluation**, **CM-evaluation**, and **RS-evaluation**
* Step 2: Create a .json file with formatting identical to calculations from other datasets in EternaBench archived git repository (embedded in colab notebooks used for *Step 1*) 
* Step 3: Clone EternaBench git repository, update files located in **scoringscripts**, **compilingscripts**, and **generateplots** that have been patched for recent package updates. 
* Step 3: Run **scoringscripts** from EternaBench github repository to get bootstrapped statistical results.
* Step 4: Run **compilingscripts** from EternaBench github repository to evaluate model against other secondary structure prediction algorithms.
* Step 5: Use **generateplots** jupyter notebooks in **analysis** folder from EternaBench github repository to generate heatmaps that display the results. 

