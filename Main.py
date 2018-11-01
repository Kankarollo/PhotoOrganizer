import os
import PIL.Image
import shutil

_pathname = "D:\\Zdjecia"

_test_pathname = "D:\\test"


def make_magic(pathname):
    list_of_dates = []
    for file in os.listdir(pathname):
        path_of_file = pathname + "\\" + file
        year = extract_year_from_file(path_of_file)
        if year is None:
            continue
        if is_directory_doesnt_exist(year, list_of_dates):
            list_of_dates.append(year)
            new_directory_path = pathname + "\\" + str(year)
            make_directory(new_directory_path)
        shutil.move(path_of_file, new_directory_path)


def is_directory_doesnt_exist(_year, _list_of_dates):
    return _year not in _list_of_dates


def make_directory(path):
    try:
        os.mkdir(path)
    except FileExistsError as e:
        print(e)
        input("File already exist! Press enter to quit!")
        exit()


def extract_year_from_file(path):
    year = None
    try:
        img = PIL.Image.open(path)
        exif_data = img._getexif()
        date = exif_data[306]
        year = date[:date.find(":")]
    except Exception as e:
        print(e)
    return year


if __name__ == '__main__':
    if not os.path.exists(_pathname):
        exit()
    make_magic(_pathname)
