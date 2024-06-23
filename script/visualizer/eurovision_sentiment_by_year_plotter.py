import matplotlib.pyplot as plt
import pandas as pd

from . import _data_getter


def get_data_for_eurovision_sentiment_by_year():
    def prepare_data():
        all_data = _data_getter._get_data()
        plot_rows = []
        for playlist_name, playlist in all_data.items():
            for song in playlist:
                plot_rows.append(
                    {
                        "year": playlist_name,
                        "sentiment": song["sentiment_analysis"]["sentiment"],
                    }
                )
        return pd.DataFrame(plot_rows)

    def create_pivot_table(plot_data):
        return pd.pivot_table(
            plot_data,
            index="year",
            columns="sentiment",
            aggfunc="size",
            fill_value=0,
        )

    plot_data = prepare_data()
    plot_data = create_pivot_table(plot_data)
    return plot_data


def _plot_eurovision_sentiment_by_year(plot_data):
    plot_data.plot(
        kind="bar",
        stacked=True,
        color={
            "mixed": "orange",
            "negative": "red",
            "neutral": "grey",
            "positive": "green",
        },
    )
    plt.title("Eurovision song sentiment over years")
    plt.xlabel("Year")
    plt.ylabel("Number of songs")
    plt.legend(title="Sentiment")
    return plt.show()


def plot_eurovision_sentiment_by_year():
    plot_data = get_data_for_eurovision_sentiment_by_year()
    return _plot_eurovision_sentiment_by_year(plot_data)


if __name__ == "__main__":
    pass
