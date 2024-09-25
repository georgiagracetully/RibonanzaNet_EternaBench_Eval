import sys
import argparse
import pandas as pd
from glob import glob
from eternabench.stats import calculate_Z_scores

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=
    '''Compile results from EternaBench bootstrapping.
    Input: keyword that all .json's to compile should start with
    Output: .json file''')

    p.add_argument("keyword", action="store", help="Keyword that all jsons to read in start with.")
    p.add_argument("-o", action='store', dest="outfile", help="Output name.")
    p.add_argument('--metric', action='store', default='pearson', help='name of metric field, default=pearson.')
    p.add_argument('--dataset_field', action='store', default='Dataset', help="name of dataset field, default='Dataset'")
    p.add_argument('--ranking_category', action='store', default=None, help="If provided, splits ranking into these classes.")
    p.add_argument('--calculate_Z_scores', action='store', help="Calculate Z scores based on package list provided.")
    p.add_argument('--dataset_list', action='store', help='Only calculate over specified datasets.')
    args = p.parse_args()

    files = sorted(glob(f"{args.keyword}*_BOOTSTRAPS.json.zip"))

    print(f"Found {len(files)} files")

    # Initialize a list to accumulate DataFrames
    df_list = []

    for fil in files:
        # Read and accumulate the DataFrames
        tmp = pd.read_json(fil)
        df_list.append(tmp)

    # Concatenate the DataFrames after accumulation
    df = pd.concat(df_list, ignore_index=True)

    if args.dataset_list is not None:
        dataset_list = []
        with open(args.dataset_list, 'r') as f:
            for lin in f.readlines():
                dataset_list.append(lin.strip())

        print("Calculating for datasets: ", dataset_list)

        df = df.loc[df[args.dataset_field].isin(dataset_list)]

    if args.calculate_Z_scores is not None:
        package_list = []
        with open(args.calculate_Z_scores, 'r') as f:
            for lin in f.readlines():
                package_list.append(lin.strip())

        print("Read in packages from package list: ", package_list)

        sorted_zscore_stats, ranking = calculate_Z_scores(
            df, package_list, metric=args.metric, 
            dataset_field=args.dataset_field, 
            ranking_category=args.ranking_category, 
            include_efold=True
        )

        sorted_zscore_stats.to_csv(f"{args.outfile}_{args.metric}_zscores_by_{args.dataset_field}.csv", index=False)
        ranking.to_csv(f"{args.outfile}_{args.metric}_ranking.csv", index=False)

