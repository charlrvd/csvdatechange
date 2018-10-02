class Settings:
    def __init__(self):
        self.in_format = "%Y-%m-%d-%H.%M.%S.%f"
        self.out_format = "%Y-%m-%d %H:%M:%S.%f"
        self.headers = "col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12"
        self.in_file = "in_file.csv"
        self.out_file = "out_file.csv"
        self.date_index = [7,8,9]
        self.split_char = ','
        self.csv_row_len = len(self.headers.split(self.split_char))
        self.timezone = None
        self.out_timezone = None
