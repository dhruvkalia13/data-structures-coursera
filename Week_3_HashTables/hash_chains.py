# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.buckets = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + bucket

    def delete(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string in bucket:
            for i in range(len(bucket)):
                if bucket[i] == string:
                    bucket.pop(i)
                    break

    def find(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string in self.buckets[hashed]:
            return "yes"
        return "no"

    def check(self, i):
        return self.buckets[i]


def process_queries(queries):
    for query in queries:
        command, arg = query.split()
        if command == "add":
            qp.add(arg)
        elif command == "del":
            qp.delete(arg)
        elif command == "find":
            print(qp.find(arg))
        elif command == "check":
            print(" ".join(qp.check(int(arg))))


if __name__ == '__main__':
    bucket_count = int(input())
    n = int(input())
    qp = QueryProcessor(bucket_count)
    queries = [input() for i in range(n)]
    process_queries(queries)
