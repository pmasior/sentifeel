import pandas as pd

from . import _data_getter


def plot_key_phrases_over_years():
    def prepare_data():
        all_data = _data_getter.get_data()
        plot_rows = []
        for playlist_name, playlist in all_data.items():
            for song in playlist:
                for key_phrase in song["key_phrases_recognition"]["key_phrases"]:
                    plot_rows.append(
                        {
                            "year": playlist_name,
                            "key_phrase": key_phrase,
                        }
                    )
        return pd.DataFrame(plot_rows)

    def create_pivot_table(plot_data):
        return pd.pivot_table(
            plot_data,
            index="key_phrase",
            columns="year",
            aggfunc="size",
            fill_value=0,
        )

    def _get_sum_of_every_row(plot_data):
        return plot_data.sum(axis=1)

    def filter_pivot_table(plot_data):
        sum_of_every_row = _get_sum_of_every_row(plot_data)
        filter_condition = sum_of_every_row > 2
        return plot_data[filter_condition]

    def sort_pivot_table(plot_data):
        def _get_sorted_indexes():
            sum_of_every_row = _get_sum_of_every_row(plot_data)
            return sum_of_every_row.sort_values(ascending=False).index

        indexes_to_filter = _get_sorted_indexes()
        return plot_data.loc[indexes_to_filter]

    plot_data = prepare_data()
    plot_data = create_pivot_table(plot_data)
    plot_data = filter_pivot_table(plot_data)
    plot_data = sort_pivot_table(plot_data)
    return plot_data
