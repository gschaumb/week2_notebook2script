"""
Module for summarizing and plotting word count groupings from CSV files.
Originally created as a preprocessing step for analyzing legal documents.

"""


import argparse
import pandas as pd
import matplotlib.pyplot as plt


def summarize_csv(filename):
    """
    Reads a CSV, groups by 'GroupName', and calculates count and total word count.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        DataFrame: Summary DataFrame with counts and word counts per 'GroupName'.
    """
    df = pd.read_csv(filename)
    # order_of_appearance and merge lines below included in case subset of data desired
    order_of_appearance = pd.Series(df["GroupName"].unique()).to_frame("GroupName")
    grouped = (
        df.groupby("GroupName")
        .agg(
            Paragraphs=("GroupName", "count"),
            Total_Word_Count=("Text", lambda x: len(" ".join(x).split())),
        )
        .reset_index()
    )
    # Merge will use the order_of_appearance defined above
    # Base code here is just unique group names in orginal order
    summary_df = order_of_appearance.merge(grouped, on="GroupName")
    return summary_df


def plot_word_count(df, max_words, output_path):
    """
    Generates and saves a bar plot of word counts for each 'GroupName'.

    Args:
        df (DataFrame): Data to plot, from summarize_csv function.
        max_words (int): Max number of words for each 'GroupName' in the plot.
        output_path (str): File path to save the plot image.
    """
    top_padding = 0.85
    bar_height = 0.8
    truncated_names = df["GroupName"].apply(lambda x: " ".join(x.split()[:max_words]))
    viridian_like_color = "#40826D"
    _, ax = plt.subplots(figsize=(10, 8))
    ax.barh(
        truncated_names,
        df["Total_Word_Count"],
        height=bar_height,
        color=viridian_like_color,
    )
    # Removed axes and titles for cleaner image
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.xlabel("")
    plt.ylabel("")
    plt.title("")
    plt.subplots_adjust(top=top_padding)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(output_path)  # Save the figure to a file
    plt.close()  # Close the plot to free up memory


if __name__ == "__main__":
# Command-line interface for summarizing and plotting data from a CSV file.
    parser = argparse.ArgumentParser(
        description="Summarize and plot word count from CSV data, saving plot to a PNG file."
    )
    parser.add_argument("filename", type=str, help="Path to the CSV file.")
    parser.add_argument(
        "--max_words",
        type=int,
        default=8,
        help="Maximum number of words to include from each group name for plot.",
    )
    parser.add_argument(
        "output_path", type=str, help="Path to save the output plot PNG file."
    )
    args = parser.parse_args()

    df_summary = summarize_csv(args.filename)
    plot_word_count(df_summary, args.max_words, args.output_path)
