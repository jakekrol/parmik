#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--input",default="../../data/2026_09-minimap2-best_match_per_query/minimap2_best_match_lengths.tsv")
parser.add_argument("--output",default="hist.png")
parser.add_argument("--title", default="Minimap2 NC045512-SRR12432009")
parser.add_argument("--bins",default = 30)
parser.add_argument("--xmin",default=0)
parser.add_argument("--xmax",default=150)
parser.add_argument("--xlabel", default="Alignment length (bp)")
parser.add_argument("--ylabel", default="Query count")
args = parser.parse_args()
args.bins = int(args.bins)
args.xmin = float(args.xmin)
args.xmax = float(args.xmax)

def main():
    df = pd.read_csv(args.input,sep="\t")
    x = df['Best_Match_Length'].values
    n = len(x)
    median = np.median(x)
    print("# queries:", n)
    print("# median length:", median)
    num_zero = np.sum(x==0)
    perc_zero = num_zero/n*100
    print("# zero length:", perc_zero,"%")
    assert np.all(x >= 0)
    assert np.all(x < 151)
    fig, ax = plt.subplots(figsize=(6,4))
    ax.hist(x,color='black', bins = args.bins)
    ax.set_title(args.title,loc="left")
    ax.set_yscale('log')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(args.xmin, args.xmax)
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    fig.savefig(args.output)

if __name__ == "__main__":
    main()