#!/usr/bin/env python
#coding=utf-8
# 基于marisa-trie构建字典树，以快速查询
# pip install marisa-trie
import marisa_trie
import cPickle as pickle

def dump_obj(obj, output):
    with open(output, 'wb') as fd:
        pickle.dump(obj, fd)

def load_obj(input):
    with open(input, 'r+') as fd:
        return pickle.load(fd)


class MarisaTrie(object):
    def __init__(self):
        pass

    def _load_file(self, input, sep='\t', chooseidx=1, coding='utf-8'):
        querylist = list()
        for line in open(input):
            line = line.strip().decode(coding, 'ignore')
            parts = line.split(sep)
            if len(parts) < chooseidx:
                continue
            querylist.append(parts[chooseidx-1])
        return querylist
        
    def build_trie(self, input):
        # 这里可以根据input的信息 计算一个MD5值
        # 如果存在对应的pkl则直接从pkl文件中加载即可
        querylist = self._load_file(input)
        self.trie = marisa_trie.Trie(querylist)

    def load_trie(self, input):
        self.trie = load_obj(input)

    def dump_trie(self, output):
        dump_obj(self.trie, output)

    def in_dict(self, query):
        return query in self.trie

    def prefix_of(self, query):
        return self.trie.prefixes(query)

    def prefix_with(self, query):
        return self.trie.keys(query)

    def search(self, query):
        query = query.decode('utf-8', 'ignore')
        print "\t[%s] in dict" % (query) if self.in_dict(query) else "\t[%s] not in dict" % (query)
        cand_query_list = self.prefix_of(query)
        print "\tprefix of [%s] total: %s" % (query, len(cand_query_list))
        if len(cand_query_list) > 0:
            print "\t\te.g. %s" % "; ".join(cand_query_list[:5])

        cand_query_list = self.prefix_with(query)
        print "\tprefix with [%s] total: %s" % (query, len(cand_query_list))
        if len(cand_query_list) > 0:
            print "\t\te.g. %s" % "; ".join(cand_query_list[:5])
        print ""



if __name__ == '__main__':
    input = "test_set/tv.dict"
    picklefile = 'test_set/tv.pkl'
    trie = MarisaTrie()
    #trie.build_trie(input)
    trie.load_trie(picklefile)
    #trie.dump_trie(picklefile)
    while True:
        query = raw_input("enter query : ")
        trie.search(query)
