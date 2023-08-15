#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re

in_file = "C:\\Users\\Xin_Fang\\Desktop\\MBAPP\\KT_INPUT.txt"
out_file = "C:\\Users\\Xin_Fang\\Desktop\\KT_LIST.csv"
KT_content = []


def exist_story_name(content):
    if "CSA" in content and "[QA]" not in content:
        return True
    else:
        return False


# def get_story_name(content):
#     if "[QA]" not in content:
#         return content
#     else:
#         content_new = content.split("创建日期")[0]
#         return content_new


def get_result(input_file, output_file):
    with open(input_file, 'r+', encoding='UTF-8') as f_in:
        for line in f_in.readlines():
            KT_content.append(line.strip())
        with open(output_file, "w+", encoding='utf_8_sig', newline='') as f_out:
            csv_writer = csv.writer(f_out)
            csv_writer.writerow(['story_name', 'story_link'])
            for line in KT_content:
                if exist_story_name(line):
                    story_link = "https://itsc-jira.mercedes-benz.com.cn/jira/browse/" + re.findall(r'CSA-\d+', line)[0]
                    story_name = re.sub(r'CSA-\d+', '', line).replace("()", '')
                    result = [story_name, story_link]
                    csv_writer.writerow(result)


if __name__ == '__main__':
    get_result(in_file, out_file)
