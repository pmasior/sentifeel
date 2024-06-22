import geodatasets
import geopandas as gpd
import pandas as pd

from . import _country_code_mapper, _data_getter


def plot_eurovision_average_sentiment_by_country():
    def prepare_data():
        all_data = _data_getter.get_data()
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
        plot_data.index = plot_data.index.map(_country_code_mapper.country_code_map)

    def get_contry_shapes():
        geo_data_path = geodatasets.get_path("naturalearth")
        geo_data_in_epsg_4326 = gpd.read_file(geo_data_path)
        geo_data_for_europe = geo_data_in_epsg_4326.to_crs(epsg=3035)
        return geo_data_for_europe

    def join_map_data_and_plot_data(map_data, plot_data):
        return pd.merge(
            map_data["name", "iso_a3", "geometry"],
            plot_data,
            how="left",
            left_on="iso_a3",
            right_on="country_code",
        )

    plot_data = prepare_data()
    plot_data = create_pivot_table(plot_data)
    plot_data = map_country_codes(plot_data)
    map_data = get_contry_shapes()
    plot_data = join_map_data_and_plot_data(map_data, plot_data)
    return plot_data
