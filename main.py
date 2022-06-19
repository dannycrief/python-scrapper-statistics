from sc_statistics import SCData, SCAnalytics
from sc_web_scrapper import ScrapperOptions


def call_scrapper():
    sc = ScrapperOptions(
        accept_cookies=True,
    )

    sc.set_filters(
        house_type='Mieszkanie', rent_buy='wynajem', localisation='warszawa',
        price_min=2000, price_max=2750, rooms_number=[1],
        area_min=25, area_max=45
    )

    sc.search()

    sc.end_session()  # ends selenium session and return file path


def prepare_and_visualize(file_path: str, debug_server=False):
    sc_data = SCData(file_path)
    df = sc_data.get_df()
    sc_statistics = SCAnalytics(df)
    sc_statistics.run_server(debug_server)


if __name__ == "__main__":
    call_scrapper()
    prepare_and_visualize(file_path="csv_dir/wynajem_mieszkanie_warszawa.csv", debug_server=False)
