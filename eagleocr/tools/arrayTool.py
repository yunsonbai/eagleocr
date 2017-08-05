import numpy


def mean_without_poles(a):
    '''
    a: numpy arrary
    '''
    na = a[:]
    na = numpy.array(na)
    if len(na) <= 3:
        return na.sum() - (na.min() + na.max())
    return (na.sum() - (
        na.min() + na.max())) / (len(na) - 2)


def var_without_poles(a):
    '''
    a: numpy arrary
    '''
    index = [numpy.argmax(a), numpy.argmin(a)]
    return numpy.delete(a, index).var()
