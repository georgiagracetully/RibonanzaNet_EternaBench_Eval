import pandas as pd
import os
from eternabench.stats import calculate_Z_scores

package_list = [
    'vienna_2', 'vienna_2_60C', 'rnastructure',
    'RibonanzaNet', 'rnasoft_blstar', 'contrafold_2', 'eternafold_B', 'nupack_99'
]

external_dataset_types = pd.read_csv(
    os.path.join(os.environ['ETERNABENCH_PATH'], 'eternabench/external_dataset_metadata.csv')
)

RNA_CLASSES = external_dataset_types['Class'].unique()

EB_CM_bootstraps_list = []

for pkg in package_list:
    tmp = pd.read_json(
        os.path.join(os.environ['ETERNABENCH_PATH'], f'data/ChemMapping/bootstraps/CM_pearson_Dataset_{pkg}_BOOTSTRAPS.json.zip')
    )
    EB_CM_bootstraps_list.append(tmp)

EB_CM_bootstraps = pd.concat(EB_CM_bootstraps_list, ignore_index=True)
EB_CM_bootstraps = EB_CM_bootstraps.loc[EB_CM_bootstraps['Dataset'] == 'RYOS_I']
EB_CM_bootstraps['Dataset'] = 'Leppek,2021 In-line-seq'

net_dataset_zscore_stats = []
net_ranking = []

for window_size in [300, 600, 900, 1200]:

    df_list = []

    for pkg in package_list:
        tmp = pd.read_json(
            os.path.join(
                os.environ['ETERNABENCH_PATH'],
                f'data/ChemMapping/bootstraps/CM_pearson_Dataset_{pkg}_BOOTSTRAPS.json.zip'
            )
        )
        df_list.append(tmp)

    df = pd.concat(df_list + [EB_CM_bootstraps], ignore_index=True)
    df = df.merge(external_dataset_types, on='Dataset', how='left')

    for rna_class in RNA_CLASSES:

        print(window_size, rna_class)

        tmp = df.loc[df['Class'] == rna_class]

        if not tmp.empty:
            zscore_stats, ranking = calculate_Z_scores(
                tmp, metric='pearson', dataset_field='Dataset', sort=False
            )

            zscore_stats['window_size'] = window_size
            ranking['window_size'] = window_size

            zscore_stats['Class'] = rna_class
            ranking['Class'] = rna_class

            net_dataset_zscore_stats.append(zscore_stats)
            net_ranking.append(ranking)

# Concatenate all accumulated DataFrames before saving
net_dataset_zscore_stats = pd.concat(net_dataset_zscore_stats, ignore_index=True)
net_ranking = pd.concat(net_ranking, ignore_index=True)

# Save the final DataFrames to CSV files
net_dataset_zscore_stats.to_csv('EternaBench_external_zscores_by_dataset.csv', index=False)
net_ranking.to_csv('EternaBench_external_ranking.csv', index=False)


