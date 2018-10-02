#from settings import Settings
from settingstest import Settings
import csvdate

def main():
    settings = Settings()
    csvdate.main(settings)
    print('Modified file create: {}'.format(settings.out_file))

if __name__ == '__main__':
    main()
