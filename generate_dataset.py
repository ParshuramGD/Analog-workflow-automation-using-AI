from parallel_runner import run_parallel
import pandas as pd
import os


def clean_dataset():

    if not os.path.exists("dataset.csv"):
        print("dataset.csv not found")
        return

    print("Cleaning dataset...")

    df = pd.read_csv("dataset.csv")

    # remove repeated header rows
    df = df[df["W1"] != "W1"]

    # convert values to numeric
    df = df.apply(pd.to_numeric, errors="coerce")

    # remove rows with NaN
    df = df.dropna()

    # remove duplicate samples
    df = df.drop_duplicates()

    # keep only realistic op-amp designs
    #df = df[(df["pm"] > 20) & (df["pm"] < 90)]
    #df = df[(df["gain"] > 20) & (df["gain"] < 120)]
    #df = df[(df["ugf"] > 1e5) & (df["ugf"] < 1e10)]

    df = df[(df["pm"] > 30) & (df["pm"] < 90)]
    df = df[(df["gain"] > 30) & (df["gain"] < 120)]
    df = df[(df["ugf"] > 1e6) & (df["ugf"] < 1e10)]

    # reset index after filtering
    df = df.reset_index(drop=True)

    # save cleaned dataset
    df.to_csv("dataset_clean.csv", index=False)

    print(f"Clean dataset saved as dataset_clean.csv ({len(df)} rows)")

if __name__ == "__main__":

    run_parallel(
        n=100000,
        workers= os.cpu_count()
    )

    clean_dataset()
