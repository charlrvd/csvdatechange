from pytz import timezone

class Settings:
    def __init__(self):
        self.in_format = "%a %b %d %H:%M:%S %Z %Y"
        self.out_format = "%Y/%m/%d-%H.%M.%S(%Z)"
        #self.headers = "street,city,zip,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude"
        self.headers = None
        self.in_file = "Sacramentorealestatetransactions.csv"
        self.out_file = "out_file.csv"
        #self.date_index = [8]
        self.date_index = None
        self.split_char = ','
        #self.csv_row_len = len(self.headers.split(self.split_char))
        self.timezone = timezone('US/Eastern')
        #self.timezone = timezone('America/Los_Angeles') # original file is EDT which is not sacramento local time
        self.out_timezone = timezone('Europe/London')
