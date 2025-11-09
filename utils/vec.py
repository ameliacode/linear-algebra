# Copyright 2013 Philip N. Klein


def getitem(v, k):
    assert k in v.D
    return v.f[k] if k in v.f else 0


def setitem(v, k, val):
    assert k in v.D
    v.f[k] = val


def equal(u, v):
    assert u.D == v.D
    pass


def add(u, v):
    assert u.D == v.D
    return Vec(u.D, {d: getitem(u, d) + getitem(v, d) for d in u.D})


def dot(u, v):
    assert u.D == v.D
    return sum([a * b for a, b in zip(u, v)])


def scalar_mul(v, alpha):
    return Vec(v.D, {d: alpha * value for d, value in v.f.items()})


def neg(v):
    return Vec(v.D, {d: -getitem(v, d) for d in v.D})


###############################################################################################################################


class Vec:
    """
    A vector has two fields:
    D - the domain (a set)
    f - a dictionary mapping (some) domain elements to field elements
        elements of D not appearing in f are implicitly mapped to zero
    """

    def __init__(self, labels, function):
        assert isinstance(labels, set)
        assert isinstance(function, dict)
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    __neg__ = neg
    __rmul__ = scalar_mul  # if left arg of * is primitive, assume it's a scalar

    def __mul__(self, other):
        # If other is a vector, returns the dot product of self and other
        if isinstance(other, Vec):
            return dot(self, other)
        else:
            return NotImplemented  #  Will cause other.__rmul__(self) to be invoked

    def __truediv__(self, other):  # Scalar division
        return (1 / other) * self

    __add__ = add

    def __radd__(self, other):
        "Hack to allow sum(...) to work with vectors"
        if other == 0:
            return self

    def __sub__(a, b):
        "Returns a vector which is the difference of a and b."
        return a + (-b)

    __eq__ = equal

    def is_almost_zero(self):
        s = 0
        for x in self.f.values():
            if isinstance(x, int) or isinstance(x, float):
                s += x * x
            elif isinstance(x, complex):
                y = abs(x)
                s += y * y
            else:
                return False
        return s < 1e-20

    def __str__(v):
        "pretty-printing"
        D_list = sorted(v.D, key=repr)
        numdec = 3
        wd = dict(
            [
                (
                    (k, (1 + max(len(str(k)), len("{0:.{1}G}".format(v[k], numdec)))))
                    if isinstance(v[k], int) or isinstance(v[k], float)
                    else (k, (1 + max(len(str(k)), len(str(v[k])))))
                )
                for k in D_list
            ]
        )
        s1 = "".join(["{0:>{1}}".format(str(k), wd[k]) for k in D_list])
        s2 = "".join(
            [
                (
                    "{0:>{1}.{2}G}".format(v[k], wd[k], numdec)
                    if isinstance(v[k], int) or isinstance(v[k], float)
                    else "{0:>{1}}".format(v[k], wd[k])
                )
                for k in D_list
            ]
        )
        return "\n" + s1 + "\n" + "-" * sum(wd.values()) + "\n" + s2

    def __hash__(self):
        "Here we pretend Vecs are immutable so we can form sets of them"
        h = hash(frozenset(self.D))
        for k, v in sorted(self.f.items(), key=lambda x: repr(x[0])):
            if v != 0:
                h = hash((h, hash(v)))
        return h

    def __repr__(self):
        return "Vec(" + str(self.D) + "," + str(self.f) + ")"

    def copy(self):
        "Don't make a new copy of the domain D"
        return Vec(self.D, self.f.copy())

    def __iter__(self):
        raise TypeError("%r object is not iterable" % self.__class__.__name__)
