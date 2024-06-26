import os

import tempfile
import shutil


def main():
    # 数えるファイルの入ったディレクトリ
    dir_path = input("Enter Directly Path: ")
    # 出力先とファイル
    output_file_path = dir_path + "count_lines.txt"
    # 数えるファイルの拡張子
    check_ext = [".js", ".scss", ".html", ".py"]
    # 数えないファイルの拡張子
    exclude_ext = [".map.css"]
    ext_count = make_dict(check_ext)
    datas: dict = {}
    if os.path.isdir(dir_path):
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(dir_path)
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                filename = "{}\{}".format(root, file)
                if len(datas) < 10:
                    if os.path.isfile(filename):
                        if not any(file.endswith(ext) for ext in exclude_ext):
                            for ext in check_ext:
                                if file.endswith(ext):
                                    count = count_lines(filename)
                                    datas[filename] = count
                                    ext_count[ext] += count
                                    ext_count["sum"] += count
                else:
                    with open(output_file_path, "a", encoding="utf-8") as file:
                        for f, data in datas.items():
                            file.write("\n{}:{}".format(f, data))
                    datas = {}
        with open(output_file_path, "a", encoding="utf-8") as file:
            for f, data in datas.items():
                file.write("\n{}:{}".format(f, data))
            datas = {}
        count_txt = format_dict_to_string(ext_count)
        insert_line(output_file_path, 2, count_txt)
    else:
        print("Not exist directly.")


def count_lines(file_path):
    count = 0
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            count += 1
    return count


def make_dict(ext_list: list) -> dict:
    ext_count = {"sum": 0}
    for file in ext_list:
        ext_count[file] = 0
    return ext_count


def format_dict_to_string(ext_count: dict) -> str:
    formatted_string = ""
    for key, value in ext_count.items():
        formatted_string += f"{key}: {value}\n"
    return formatted_string


def insert_line(file_path, line_number, new_line):
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8")

    with open(file_path, "r", encoding="utf-8") as original_file, temp_file:
        for current_line_number, line in enumerate(original_file, start=1):
            if current_line_number == line_number:
                temp_file.write(new_line + "\n")
            temp_file.write(line)

    # Move the temporary file to the original file
    shutil.move(temp_file.name, file_path)


if __name__ == "__main__":
    main()
