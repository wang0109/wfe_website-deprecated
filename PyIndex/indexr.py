#!/usr/bin/env python
__author__ = 'Wei Wang'

import os
import sys
import time

from util import myutil
from data import stream
from data import db

MIN_PATH_CHECK_LEVEL = 3
ESTIMATED_TOTAL_FILE_NUM = 65000
DIST_ROOT = "/Volumes/NO NAME"


def not_interested_path(root, path):
    # returns true for paths that we do not care
    if myutil.rel_level(root, path) < MIN_PATH_CHECK_LEVEL:
        return True
    if myutil.is_hidden(path):
        return True
    if myutil.contain_hidden_dir(path):
        return True
        # if not myutil.match_type(path, ["mp4", "jpg", "wav", "mts", "lrv"]):
    if not myutil.match_type(path, ["mp4", "wav", "mts", "lrv"]): # fixme
        return True
    return False


def dir_in_white_list(dir_name):
    white_list = ("/Volumes/NO NAME/2014-02-18", "/Volumes/NO NAME/2014-02-14")
    if dir_name.startswith(white_list):
        return True
    return False


def get_parsed_file(full_file_path):
    s_file = stream.StreamFile(full_file_path)
    s_file.parse()
    return s_file


def scan_file(root, full_file_path):
    if not_interested_path(root, full_file_path):
        return False
    s_file = get_parsed_file(full_file_path)
    db.insert_stream(s_file)
    return True


def scan_disk(root, file_begin, file_limit=1000000):
    if not os.path.exists(root):
        print root, "not exist. Nothing to scan."
        return
    file_count = 0
    inserted_count = 0
    file_end = file_begin + file_limit
    last_time = time.time()
    prof_round = 2  # profiling: check time for each round
    db.connect_db()
    for dir_, dir_names, file_names in os.walk(root):
        if not dir_in_white_list(dir_):
            continue

        for file_name in file_names:
            file_count += 1
            # if file_count % prof_round == 0:
            if True:
                cur_time = time.time()
                round_diff = cur_time - last_time
                last_time = cur_time
                sys.stdout.write(
                    "Scanning %d (at about %f %%) .. Avg speed: %f s/item. Estimated time for 10k items: %f s\r" %
                    (file_count, file_count * 100.0 / ESTIMATED_TOTAL_FILE_NUM,
                     round_diff / prof_round, round_diff / prof_round * 10000.0))
            if file_count < file_begin:
                continue
            if file_count > file_end:
                break
            full_file_path = os.path.join(dir_, file_name)
            if not scan_file(root, full_file_path):
                continue
            inserted_count += 1
        if file_count > file_end:
            break

    db.close_db()


def timed_scan_disk(root, file_begin, file_limit=1000000):
    start_time = time.time()
    scan_disk(root, file_begin, file_limit)
    end_time = time.time()

    # print "Scanned", file_count - 1, "files in", \
    #     end_time - start_time, "seconds. Inserted:", \
    #     inserted_count, "db records."


def run_main():
    # db.prepare_empty_db()
    db.ensure_main_table()
    timed_scan_disk(DIST_ROOT, 0)
    # scan_disk(DIST_ROOT, 0)


def run_test():
    test_file = "/Volumes/NO NAME/2014-02-18/WB wall/162GOPRO/G0022975.JPG"
    stream.StreamFile.Debug = True
    s_file = get_parsed_file(test_file)
    print s_file
    stream.StreamFile.Debug = False

run_main()
# run_test()

print "[Program ended.]"

