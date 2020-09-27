import os
import PIL.Image
import shutil
import argparse

# _pathname = "D:\Zdjecia\\test"
# _test_pathname = "D:\\test"


def make_magic(pathname):
    list_of_dates = []
    for file in os.listdir(pathname):
        path_of_file = os.path.join(pathname,file)
        if os.path.isdir(path_of_file):
            continue
        year = extract_year_from_file(path_of_file)
        if year is None:
            continue
        if year not in list_of_dates:
            list_of_dates.append(year)
            new_directory_path = os.path.join(pathname,str(year))
            if not os.path.exists(new_directory_path):
                os.mkdir(new_directory_path)
                print(f"Created new directory: {new_directory_path}")
        try:
            shutil.move(path_of_file, new_directory_path)
        except shutil.Error as e:
            print(str(e))


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

def create_menu():
    parser = argparse.ArgumentParser(description="How to use:")
    parser.add_argument('-p','--path', type=str, help='Path to directory.', required=True)

    menu_args = parser.parse_args()

    return menu_args

def main():
    args = create_menu()

    if not os.path.exists(args.path):
        print("Directory doesn't exist. Ending program...")
        return
    make_magic(args.path)

if __name__ == '__main__':
    main()