from sc_web_scrapper import ScrapperOptions
from sc_statistics import SCData


def call_scrapper(link: str):
    sc = ScrapperOptions(
        link=link,
        accept_cookies=True,
    )

    sc.set_filters(
        house_type='Mieszkanie', rent_buy='wynajem', localisation='warszawa/wola',
        price_min=2000, price_max=2750, rooms_number=[1],
        area_min=25, area_max=45
    )

    sc.search()

    sc.end_session()  # ends selenium session and return file path


if __name__ == "__main__":
    sc_data = SCData(file_path="csv_dir/wynajem_mieszkanie_warszawa.csv")
    test = sc_data.get_df()
    print(test['media_price'])
    # call_scrapper(link="https://otodom.pl/")
