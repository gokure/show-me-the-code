#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from collections import Counter

def _analyze_file(fullpath):
    code_line = comment_line = empty_line = 0
    with open(fullpath) as f:
        for line in f:
            line = line.strip()
            if not line:
                empty_line += 1
            elif line.startswith('#'):
                comment_line += 1
            else:
                code_line += 1
    return (code_line, comment_line, empty_line)

def analyze_project(project):
    file_count = total_lines = code_lines = comment_lines = empty_lines = 0
    for root, dirs, files in os.walk(project):
        if not ".git" in dirs:
            for file in files:
                if file.endswith('.py'):
                    file_count += 1
                    code_line, comment_line, empty_line = _analyze_file(os.path.join(root, file))
                    code_lines += code_line
                    comment_lines += comment_line
                    empty_lines += empty_line
    total_lines = code_lines + comment_lines + empty_lines
    print("Analysis result:\n")
    print("total files: {}\ntotal lines: {}\ncode lines: {}\ncomment lines: {}\nempty lines: {}".format(
        file_count,
        total_lines,
        code_lines,
        comment_lines,
        empty_lines)
    )

if __name__ == '__main__':
    project = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
    analyze_project(project)
