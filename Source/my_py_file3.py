#firstly, create your py file

#example from MRJob and intro
from mrjob.job import MRJob

class Map_Reducer1(MRJob):

    def mapper(self, _, line):
        key = line.split(",")[1].split("\t")[0] 
        value = float(line.split("\t")[1])
        if value>=37.0:
            yield key,1

    def reducer(self, key, values):
        yield key, sum(values)  #define keys and values


if __name__ == '__main__':
    Map_Reducer1.run()
