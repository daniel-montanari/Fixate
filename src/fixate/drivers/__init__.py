from inspect import isroutine
from functools import wraps, partial
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__file__)


def _ensure_connected(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        if not self.is_connected:
            self.connect()
        return f(self, *args, **kwargs)

    return wrapper


class ResourceMeta(type):
    def __new__(mcs, clsname, bases, dct):
        for name, attr in dct.items():
            if isroutine(attr):
                if name.startswith('_') or name in ('connect', 'disconnect') or name in dct.get('_connect_ignore', []):
                    # Don't wrap these functions with _ensure_connected
                    continue
                dct[name] = _ensure_connected(attr)
        return super().__new__(mcs, clsname, bases, dct)


class Resource(metaclass=ResourceMeta):
    """
    Resource base class for creating self connecting Resources.
    connect is called whenever a public method api call is made and is_connected = False
    ie.
    def _my_func(self):
        pass
    will not call connect as it is a private function by convention whereas
    def my_func(self):
        pass
    will.
    Exceptions to this rule are connect, disconnect and function strings as can be defined by creating a list called
    _connect_ignore on class definition
    """
    is_connected = False

    # _connect_ignore = ['ignored_func1','ignored_func2'] # Set this parameter in derived class definition if required
    def connect(self):
        """
        Override connect function but ensure that self.is_connected is set if connected or an exception occurs if
        connection could not be established
        :return:
        """
        log.debug("Connected to {}".format(self.__class__.__name__))
        self.is_connected = True

    def disconnect(self):
        """
        Override disconnect function but ensure that self.is_connect is set to False
        :return:
        """
        log.debug("Disconnected from {}".format(self.__class__.__name__))
        self.is_connected = False


class ResourceManager:
    """
    Resource manager allows for multiple Resources to be collated and managed from a central location.
    Resources must be either derived from the Resource class or must implement a the functions
    def connect(self): # No Parameters
    def disconnect(self): # No Parameters
    and have an attribute
    is_connected (Boolean)
    """

    def __init__(self):
        self.resources = {}
        self._cleanup = []

    def add_resource(self, id, resource):
        """
        :param kwargs: kwargs of <id>=<Resource>.
        Eg.
        >>>class MyDmm(Resource):
        >>>    def hello(self):
        >>>        print("World")
        >>>dm = ResourceManager(dmm=MyDmm())
        >>>dm.dmm.hello()
        World
        :return:
        """
        self.resources[id] = resource

    def cleanup_register(self, func, *args, **kwargs):
        """
        Registers a cleanup function to be executed on cleanup_execute call.
        The registered functions are executed in the order they are added via this function.
        Use the cleanup_clear to remove all the registered cleanup functions
        :param func: function as directly refrenced. eg. dm.dmm.disconnect
        :param args: The arguments that should be called with the func
        :param kwargs: The keyword arguments that should be called with the func
        :return: None
        """
        self._cleanup.append(partial(func, *args, **kwargs))

    def cleanup_execute(self):
        for partial_func in self._cleanup:
            partial_func()

    def cleanup_clear(self):
        self._cleanup.clear()

    def __setattr__(self, key, value):
        """
        Checks to see if you are trying to set a resource, if that is the case then pass that on to self.resources
        for management
        :param key:
        :param value:
        :return:
        """
        if isinstance(value, Resource):
            self.add_resource(key, value)
            return
        super().__setattr__(key, value)

    def __getattr__(self, attr):
        """
        If no attribute exists then it tries to grab the equivalent attribute from self.resources
        :param attr:
        :return:
        """
        resource = self.resources.get(attr)
        if resource is None:
            return self.__getattribute__(attr)  # Should Raise Attribute Error
        return resource

    def __delattr__(self, name):
        """

        :param item:
        :return:
        """
        if name in self.resources:
            del self.resources[name]
            return
        return super().__delattr__(name)  # Should Raise Attribute Error


if __name__ == "__main__":
    class MyDmm(Resource):
        def __init__(self):
            self.subcls = OtherClass()

        def hello(self):
            """
            Doc for hello
            :return:
            """
            print("Hello World")

        def _unconnected_hell(self):
            print("Goodbye Cruel World")

        def other_method(self):
            pass


    class OtherClass:
        def another_func(self):
            print("Other func")


    # dm = ResourceManager(dmm=MyDmm())
    dm = ResourceManager()
    dm.dmm = MyDmm()
    # dm.add_resource("dmm", MyDmm())
    print("Resource Manager Instantiated")
    dm.dmm.hello()
    dm.dmm.disconnect()
    dm.dmm._unconnected_hell()
    dm.dmm.subcls.another_func()
    dm.dmm.hello()
    dm.dmm.disconnect()
    dm.dmm.hello()
    dm.dmm.hello()
    help(dm.dmm.hello)
    dm.dmm.disconnect()
    'World'
    print(dm.dmm)
    del dm.dmm
    dm.dmm = MyDmm()
    print(dm.dmm)
    # dm.remove_Resources(['dmm'])
    # dm.dmm.hello()
