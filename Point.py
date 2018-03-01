class Point:

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __eq__(self, other):
        return self.r == other.r and self.c == other.c