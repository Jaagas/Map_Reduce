#firstly, create your py file

#file word count. lots of intentional mistakes
from mrjob.job import MRJob


class MapREducer(MRJob):
    def mapper(self, _, line):
        location, time, voter = line.split(",")
        voter = int(voter)
        yield location, voter

    def reducer(self, location, voters):
        min_voter = next(voters)
        max_voter = min_voter
        for item in voters:
            min_voter = min(item, min_voter)
            max_voter = max(item, max_voter)
        yield location, (min_voter, max_voter)


if __name__ == '__main__':
    MapREducer.run()
