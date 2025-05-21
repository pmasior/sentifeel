import matplotlib.pyplot as plt
import pandas as pd

from . import _data_getter


def get_data_for_eurovision_average_sentiment_by_year():
    def prepare_data():
        all_data = _data_getter._get_data()
        plot_rows = []
        for playlist_name, playlist in all_data.items():
            for song in playlist:
                sentiment_scores = song["sentiment_analysis"]["confidence_scores"]
                sentiment_score = (sentiment_scores["positive"] * 1) + (
                    sentiment_scores["negative"] * -1
                )
                plot_rows.append(
                    {
                        "year": playlist_name,
                        "sentiment_score": sentiment_score,
                    }
                )
        return pd.DataFrame(plot_rows)

    def create_pivot_table(plot_data):
        return pd.pivot_table(
            plot_data,
            index="year",
            values="sentiment_score",
            aggfunc="mean",
        )

    plot_data = prepare_data()
    plot_data = create_pivot_table(plot_data)
    return plot_data


def _plot_eurovision_average_sentiment_by_year(plot_data):
    plot_data.plot(kind="line", marker="o", linestyle="-")
    plt.title("Average sentiment score in Eurovision songs over years")
    plt.xlabel("Year")
    plt.ylabel("Average sentiment score")
    plt.axhline(0, color="black", linestyle="-")
    plt.legend(title="Year")
    return plt.show()


def plot_eurovision_average_sentiment_by_year():
    plot_data = get_data_for_eurovision_average_sentiment_by_year()
    return _plot_eurovision_average_sentiment_by_year(plot_data)


if __name__ == "__main__":
    pass
