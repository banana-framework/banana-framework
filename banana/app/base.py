from banana.pluggins.config import get_plugin_manager
from banana.utils.functional import LazyObject


class Application(object):
    __stop_mutation = False

    def __init__(self):
        self.__stop_mutation = False
        self.plugin_manager = get_plugin_manager()
        self.hook = self.plugin_manager.hook
        self._initialize()

    def _initialize(self):
        self.hook.banana_on_app_initialize(registry=self)
        self._after_initialization()

    def _after_initialization(self):
        self.__stop_mutation = True

    def __setattr__(self, key, value):
        if self.__stop_mutation:
            raise ValueError('Cannot modify Application object')
        else:
            super(Application, self).__setattr__(key, value)

    def __delattr__(self, item):
        if self.__stop_mutation:
            raise ValueError('Cannot modify Application object')
        else:
            super(Application, self).__delattr__(item)


app = LazyObject(Application)
