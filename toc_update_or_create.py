# -*- coding:utf-8 -*-

import re
import sys

TOC_START_STR = "<!-- markdown-toc start - Don't edit this section. Run this file again -->\n**目录**\n\n"
TOC_END_STR = "<!-- markdown-toc end -->\n"
need_toc_regx = r'(?<=\n)#+\s+\.+'

def toc_create_or_update(filepath='README.md'):
    """创建或者更新目录"""

    with open(filepath, 'r+', encoding='utf-8') as f:
        f_str = f.read()
        toc_end = re.findall(TOC_END_STR, f_str)
        if len(toc_end) == 0:
            need_toc_list = re.findall(need_toc_regx, f_str)
            toc_list = map(from_title_to_toc, need_toc_list)
        
        toc_str = ' '.join(toc_list)
        f.write(TOC_START_STR)
        f.write(toc_str)
        f.write(TOC_END_STR)
        f.write(f_str)


def from_title_to_toc(title):
    """将标题转化为目录"""
    title_split = title.split(' ')
    table_count = len(title_split[0])
    tables = '\t'*table_count
    text = ' '.join(title_split[1:])
    url = '#' + '-'.join(title_split[1:])
    return '{tables} * [{text}]({url})\n'.format(tables=tables, text=text, url=url)



if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        toc_create_or_update(args[1])
    else:
        toc_create_or_update()
