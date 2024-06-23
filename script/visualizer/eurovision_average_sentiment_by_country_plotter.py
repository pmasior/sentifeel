import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from io_helper import terminal_printer
from . import _country_code_mapper, _data_getter, _map_shapes_fetcher


def get_data_for_eurovision_average_sentiment_by_country():
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
                        "country_code": song["country_code"],
                        "sentiment_score": sentiment_score,
                    }
                )
        return pd.DataFrame(plot_rows)

    def create_pivot_table(plot_data):
        return pd.pivot_table(
            plot_data,
            index="country_code",
            values="sentiment_score",
            aggfunc="mean",
        )

    def map_country_codes(plot_data):
        plot_data.index = plot_data.index.str.upper()
        plot_data.index = plot_data.index.map(_country_code_mapper.country_code_map)
        return plot_data

    def get_contry_shapes():
        geo_data_path = _map_shapes_fetcher._fetch_and_extract_map_shapes()
        terminal_printer.verbose_print(f"Opening {geo_data_path}")
        geo_data_in_epsg_4326 = gpd.read_file(geo_data_path)
        geo_data_for_europe = geo_data_in_epsg_4326.to_crs(epsg=3035)
        return geo_data_for_europe

    def join_map_data_and_plot_data(map_data, plot_data):
        return pd.merge(
            map_data[["NAME", "SOV_A3", "geometry"]],
            plot_data,
            how="left",
            left_on="SOV_A3",
            right_on="country_code",
        )

    plot_data = prepare_data()
    plot_data = create_pivot_table(plot_data)
    plot_data = map_country_codes(plot_data)
    map_data = get_contry_shapes()
    plot_data = join_map_data_and_plot_data(map_data, plot_data)
    return plot_data


def _plot_eurovision_average_sentiment_by_country(plot_data):
    ax = plot_data.plot(
        cmap="RdYlGn",
        column="sentiment_score",
        legend=True,
        legend_kwds={"label": "Average Sentiment Score by Country"},
        missing_kwds={"color": "lightgrey"},
        vmin=-1,
        vmax=1,
    )
    plt.title("Average setinent score by country in Eurovision songs")
    ax.set_xlim([2500000, 6600000])
    ax.set_ylim([1300000, 5500000])
    ax.set_axis_off()
    return plt.show()


def plot_eurovision_average_sentiment_by_country():
    plot_data = get_data_for_eurovision_average_sentiment_by_country()
    return _plot_eurovision_average_sentiment_by_country(plot_data)


if __name__ == "__main__":
    pass
