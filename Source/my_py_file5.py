#firstly, create your py file

#example from MRJob and intro
from mrjob.job import MRJob
import re

class Map__Reducer(MRJob):

    def mapper(self, _, line):
        words = line.lower().split(' ')
        for word in words:
            key = re.findall(r'[a-z0-9]+', word)
            for k in key:
                yield k,1

    def reducer(self, key, values):
        yield key, sum(values)  #define keys and values


if __name__ == '__main__':
    Map__Reducer.run()
