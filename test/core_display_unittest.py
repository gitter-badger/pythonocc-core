#!/usr/bin/python

##Copyright 2010-2014 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import sys
print(sys.path)

from OCC.Display.SimpleGui import init_display
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox

# pyside test
print('pyside test')
PYSIDE_INITIALIZED = False
try:
    pyside_display, start_display, add_menu, add_function_to_menu = init_display('qt-pyside')
    PYSIDE_INITIALIZED = True
except:
    print('cant load the qt-pyside backend')
if PYSIDE_INITIALIZED:
    my_box_1 = BRepPrimAPI_MakeBox(10., 20., 30.).Shape()
    pyside_display.DisplayShape(my_box_1, update=True)

# pyqt4 test
print('pyqt4 test')
PYQT4_INITIALIZED = False
try:
    pyqt4_display, start_display, add_menu, add_function_to_menu = init_display('qt-pyqt4')
    PYQT4_INITIALIZED = True
except:
    print('cant load the qt-pyqt4 backend')
if PYQT4_INITIALIZED:
    my_box_2 = BRepPrimAPI_MakeBox(10., 20., 30.).Shape()
    pyqt4_display.DisplayShape(my_box_2, update=True)

# wx test
print('wx test')
WX_INITIALIZED = False
try:
    wx_display, start_display, add_menu, add_function_to_menu = init_display('wx')
    WX_INITIALIZED = True
except:
    print('cant load the wx backend')
if WX_INITIALIZED:
    my_box_3 = BRepPrimAPI_MakeBox(10., 20., 30.).Shape()
    wx_display.DisplayShape(my_box_3, update=True)
