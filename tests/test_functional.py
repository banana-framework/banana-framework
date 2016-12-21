from __future__ import absolute_import

from banana.utils.functional import LazyObject, Proxy


def test_proxy_with_function():
    def some_function(*args, **kwargs):
        """Some docstring
        """
        some_function._counter += 1
        some_function._call_args = args
        some_function._call_kwargs = kwargs
        return some_function._counter

    some_function._counter = 0
    proxy = Proxy(some_function, args=(1, 2, 3), kwargs={'k': 'v'})
    assert some_function._counter == 0
    assert proxy == 1
    assert some_function._counter == 1
    assert some_function._call_args == (1, 2, 3)
    assert some_function._call_kwargs == {'k': 'v'}
    assert repr(proxy) == repr(2)
    assert proxy.__index__() == some_function._counter.__index__()
    assert hash(proxy) == hash(4)
    assert str(proxy) == str(5)
    assert proxy.__doc__ == some_function._counter.__doc__
    assert help(proxy) == help(some_function._counter)


def test_lazy_object_with_list():
    local = list
    expected_list = [1, 2, 3, 4]
    args = ((1, 2, 3, 4), )
    proxy = LazyObject(local, args=args)
    assert not hasattr(proxy, '_LazyObject__thing')
    assert proxy == expected_list
    assert hasattr(proxy, '_LazyObject__thing')
    assert len(proxy) == len(expected_list)
    assert proxy[1] == expected_list[1]
    assert proxy.pop() == expected_list.pop()
    assert proxy[0:] == expected_list[0:]
    proxy[0:2] = [0, 1]
    assert repr(proxy) == repr([0, 1, 3])
    del proxy[2:10]
    assert repr(proxy) == repr([0, 1])
    assert proxy.__doc__ == list.__doc__
    assert dir(proxy) == dir(expected_list)


def test_lazy_object_with_function():
    def some_function(*args, **kwargs):
        some_function._counter += 1
        some_function._call_args = args
        some_function._call_kwargs = kwargs
        return some_function._counter

    some_function._counter = 0
    # make some calls to ensure counter works
    calls_count = 10
    for i in range(calls_count):
        some_function()

    proxy = LazyObject(some_function, args=(1, 2, 3), kwargs={'k': 'v'})
    assert some_function._counter == calls_count
    assert proxy == calls_count + 1
    assert some_function._counter == calls_count + 1
    assert some_function._call_args == (1, 2, 3)
    assert some_function._call_kwargs == {'k': 'v'}
    assert repr(proxy) == repr(calls_count + 1)
    assert proxy.__index__() == some_function._counter.__index__()
    assert proxy > 0
    assert proxy < 12
    assert proxy >= 10
    assert proxy <= 11
    assert proxy != 0
    assert proxy.__cmp__(calls_count + 1) == 0
    assert proxy.__cmp__(calls_count + 5) < 0
    assert proxy.__cmp__(calls_count - 5) > 0
    assert hash(proxy) == hash(calls_count + 1)
    assert str(proxy) == str(calls_count + 1)

    # Finally function must be called only once
    assert some_function._counter == calls_count + 1
