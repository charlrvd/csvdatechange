from pytz import timezone

class Settings:
    def __init__(self):
        self.in_format = "%a %b %d %H:%M:%S %Z %Y"
        self.out_format = "%Y/%m/%d-%H.%M.%S(%Z)"
        self.headers = "street,city,zip,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude"
        self.in_file = "Sacramentorealestatetransactions.csv"
        self.out_file = "out_file.csv"
        self.date_index = [8]
        self.split_char = ','
        self.csv_row_len = len(self.headers.split(self.split_char))
        #self.timezone = timezone('US/Pacific')
        self.timezone = timezone('US/Eastern')
