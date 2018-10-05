class Settings:
    def __init__(self):
        self.in_format = "%Y-%m-%d-%H.%M.%S.%f"
        self.out_format = "%Y-%m-%d %H:%M:%S.%f"
        self.in_file = "in_file.csv"
        self.out_file = "out_file.csv"
        self.split_char = ','
        self.headers = None
        self.date_index = None
        self.timezone = None
        self.out_timezone = None
