#firstly, create your py file

#file word count. lots of intentional mistakes
from mrjob.job import MRJob


class Map_REducer(MRJob):
    def mapper(self, _, line):
        key = line.split(",")[1]
        yield key, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    Map_REducer.run()
