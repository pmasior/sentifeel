import pandas as pd

from . import _data_getter


def plot_average_sentiment_for_keywords():
    def prepare_data():
        all_data = _data_getter.get_data()
        plot_rows = []
        for playlist_name, playlist in all_data.items():
            for song in playlist:
                sentiment_scores = song["sentiment_analysis"]["confidence_scores"]
                sentiment_score = (sentiment_scores["positive"] * 1) + (
                    sentiment_scores["negative"] * -1
                )
                for key_phrase in song["key_phrases_recognition"]["key_phrases"]:
                    plot_rows.append(
                        {
                            "year": playlist_name,
                            "key_phrase": key_phrase,
                            "sentiment_score": sentiment_score,
                        }
                    )
        return pd.DataFrame(plot_rows)

    def create_pivot_table(plot_data):
        return pd.pivot_table(
            plot_data,
            index="key_phrase",
            columns="year",
            values="sentiment_score",
            aggfunc="mean",
        )

    def filter_pivot_table(plot_data, indexes_to_filter):
        return plot_data.loc[indexes_to_filter]

    plot_data = prepare_data()
    plot_data = create_pivot_table(plot_data)
    plot_data = filter_pivot_table(plot_data, ["heart", "love", "world"])
    return plot_data
