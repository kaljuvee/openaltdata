
import arrow

testdatestr = 'Mon, 25 May 2020 10:05:33 UT'

def convert_businesswire_datestring(datestr):
     print('converting datestr:', datestr)

def get_root_symbol(ric):
    try:
        ticker = ric.split('.')[0]
    except Exception:
        print('Exception in get_ticker()', ric)
    return ticker

def main():
    convert_businesswire_datestring(testdatestr)

if __name__ == "__main__":
    main()