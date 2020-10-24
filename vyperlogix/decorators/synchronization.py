from __future__ import print_function
# Synchronization classes using decorators. Provides synchronized, semaphore
# and event classes which provide transparent decorator patterns for
# Lock, BoundedSemaphore and Event objects in Python.

from threading import Thread, Lock, BoundedSemaphore, Event, currentThread
from time import sleep
from random import random

class synchronized(object):
    """ Class enapsulating a lock and a function
    allowing it to be used as a synchronizing
    decorator making the wrapped function
    thread-safe """

    def __init__(self, *args):
        self.lock = Lock()

    def __call__(self, f):
        def lockedfunc(*args, **kwargs):
            try:
                self.lock.acquire()
                print('Acquired lock=> %s' % (currentThread()))
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    raise
            finally:
                self.lock.release()
                print('Released lock=> %s' % (currentThread()))

        return lockedfunc


class semaphore(object):
    """ Class encapsulating a semaphore to limit
    number of resources  """

    def __init__(self, *args):
        self.sem = BoundedSemaphore(args[0])

    def __call__(self, f):
        def semfunc(*args, **kwargs):
            try:
                print('Trying to acquire sem=> %s' % (currentThread()))
                self.sem.acquire()
                print('Acquired sem=> %s' % (currentThread()))
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    raise
            finally:
                self.sem.release()
                print('Released sem=> %s' % (currentThread()))


        return semfunc

class event(object):
    """ Class encapsulating an event object to control
    sequential access to a resource """

    def __init__(self, *args):
        self.evt = Event()
        self.evt.set()

    def __call__(self, f):
        def eventfunc(*args, **kwargs):
            try:
                print('Waiting on event => %s' % (currentThread()))
                self.evt.wait()
                # First thread will clear the event and
                # make others wait, once it is done with the
                # job, it sets the event which wakes up
                # another thread, which does the same thing...
                # This provides sequential access to a
                # resource...
                self.evt.clear()
                print('Cleared event => %s' % (currentThread()))
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    raise
            finally:
                # Wake up another thread...
                self.evt.set()
                print('Set event=> %s' % (currentThread()))

        return eventfunc
