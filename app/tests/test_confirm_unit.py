import os
import pytest
import fakeredis
import mongomock
from redis import Redis
from bson import ObjectId

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HOLD_PATH = os.path.join(BASE, 'app', 'hold_seats.lua')
CONFIRM_PATH = os.path.join(BASE, 'app', 'confirm_reserve.lua')
