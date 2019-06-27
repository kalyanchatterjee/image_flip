#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:07:53 2019

@author: kalyan.chatterjee
"""
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("""You need the Pillow module!
                Install it by running "pip install Pillow"
            """)
