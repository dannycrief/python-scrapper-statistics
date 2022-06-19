import os
import errno
import pandas as pd


class SCData:
    def __init__(self, file_path: str):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.file_path)

        self.df = pd.read_csv(self.file_path)

        self.df['location'] = self.df['location'].apply(lambda loc_value: ','.join(loc_value.split(',')[:2]))
        self.df['price'] = self.__get_float_from_currency('price')
        self.df['deposit_price'] = self.__get_float_from_currency('deposit_price')
        self.df['year_built'] = self.df['year_built'].astype('Int64')
        self.df['area'] = self.__get_area_as_float('area')
        self.df['media_price'] = self.__get_float_from_currency('media_price')
        self.df['floor_number'] = self.__get_floor_number_as_('floor_number')

    def get_df(self):
        return self.df

    def __get_float_from_currency(self, column: str):
        return self.df[column].replace('[,]', '.', regex=True).replace('[ , zł / miesiąc]', '', regex=True).astype(
            'float64')

    def __get_area_as_float(self, column):
        return self.df[column].replace('[,]', '.', regex=True).replace('[ m²]', '', regex=True).astype('float64')

    def __get_floor_number_as_(self, column):
        return self.df[column].str.replace('parter', '1').str.replace('> ', '').str.split('/', expand=True)[0].astype(
            'Int64')
