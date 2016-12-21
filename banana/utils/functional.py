

class Proxy(object):
    """Proxy wrapper. Provides deferred calculation of wrapped object (wrapped
    object will processed every time when it called)

    Examples:
        >>> from banana.utils.functional import Proxy
        >>>
        >>> def some_function(*args, **kwargs):
        ...     some_function._counter += 1
        ...     some_function._called_with = args, kwargs
        ...     return some_function._counter
        >>>
        >>> some_function._called_with = None, None
        >>> some_function._counter = 0
        >>>
        >>> lazy_result = Proxy(
        ...     some_function, args=(1, 2), kwargs={'k': 'v'}
        ... )
        >>> some_function._counter
        0
        >>> some_function._called_with
        (None, None)
        >>> lazy_result == 1
        True
        >>> some_function._counter
        1
        >>> some_function._called_with
        ((1, 2), {'k': 'v'})
        >>> lazy_result == 2
        True
        >>> some_function._counter
        2
    """

    def __init__(self, local, args=None, kwargs=None):
        self.__wrapped__ = self.__local = local
        self.__args = args or ()
        self.__kwargs = kwargs or {}

    def _get_current_object(self):
        return self.__local(*self.__args, **self.__kwargs)

    @property
    def __name__(self):
        return self._get_current_object().__name__

    @property
    def __module__(self):
        return self._get_current_object().__module__

    @property
    def __doc__(self):
        return self._get_current_object().__doc__

    @property
    def __class__(self):
        return self._get_current_object().__class__

    def __repr__(self):
        return repr(self._get_current_object())

    def __dir__(self):
        return dir(self._get_current_object())

    def __getattr__(self, item):
        return getattr(self._get_current_object(), item)

    def __len__(self):
        return len(self._get_current_object())

    def __index__(self):
        return self._get_current_object().__index__()

    def __getitem__(self, key):
        return self._get_current_object()[key]

    def __setitem__(self, key, value):
        self._get_current_object()[key] = value

    def __delitem__(self, key):
        del self._get_current_object()[key]

    def __str__(self):
        return str(self._get_current_object())

    def __lt__(self, other):
        return self._get_current_object() < other

    def __le__(self, other):
        return self._get_current_object() <= other

    def __eq__(self, other):
        return self._get_current_object() == other

    def __ne__(self, other):
        return self._get_current_object() != other

    def __gt__(self, other):
        return self._get_current_object() > other

    def __ge__(self, other):
        return self._get_current_object() >= other

    def __cmp__(self, other):
        current_object = self._get_current_object()
        # python 3 is not support `cmp` function
        return (current_object > other) - (current_object < other)

    def __hash__(self):
        return hash(self._get_current_object())


class LazyObject(Proxy):
    """Proxy wrapper. Provides lazy calculation of wrapped object (wrapped
    object will processed only once on demand)

    Examples:
        >>> from banana.utils.functional import LazyObject
        >>>
        >>> def some_function(*args, **kwargs):
        ...     some_function._counter += 1
        ...     some_function._called_with = args, kwargs
        ...     return some_function._counter
        >>>
        >>> some_function._called_with = None, None
        >>> some_function._counter = 0
        >>>
        >>> lazy_result = LazyObject(
        ...     some_function, args=(1, 2), kwargs={'k': 'v'}
        ... )
        >>> some_function._counter
        0
        >>> some_function._called_with
        (None, None)
        >>> lazy_result == 1
        True
        >>> some_function._counter
        1
        >>> some_function._called_with
        ((1, 2), {'k': 'v'})
        >>> lazy_result == 1
        True
        >>> some_function._counter
        1
    """

    @property
    def __doc__(self):
        return self._get_current_object().__doc__

    def _get_current_object(self):
        try:
            return object.__getattribute__(self, '_LazyObject__thing')
        except AttributeError:
            return self.__evaluate__()

    def __evaluate__(self):
        self.__thing = thing = Proxy._get_current_object(self)
        return thing
