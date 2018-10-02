import csvdate
from sacramento_settings import Settings as Sacramento
from settings import Settings

def main():
    settings = Sacramento()
    csvdate.main(settings)
    print('Modified file written to: {}'.format(settings.out_file))

if __name__ == '__main__':
    main()
