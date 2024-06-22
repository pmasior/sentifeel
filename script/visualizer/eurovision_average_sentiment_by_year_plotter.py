import pandas as pd

from . import _data_getter


def plot_eurovision_average_sentiment_by_year():
    def prepare_data():
        all_data = _data_getter.get_data()
        plot_rows = []
        for playlist_name, playlist in all_data.items():
            for song in playlist:
                sentiment_scores = song["sentiment_analysis"]["configence_score"]
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
