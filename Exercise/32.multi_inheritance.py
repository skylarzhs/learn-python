#! /usr/bin/env python3
# -*- encoding : utf-8 -*-

'Multiple inheritance test'

__author__ = 'Skylar Zheng'

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    pass

class Flyable(object):
    pass

class Dog(Mammal,Runnable):
    pass

class Parrot(Bird,Flyable):
    pass

class MyTCPServer(TCPServer,ForkingMixIn):
    pass

class MyUDPServer(UDPServer,ThreadingMixIn):
    pass

class MyTCPServer(TCPServer,CoroutineMixIn):
    pass