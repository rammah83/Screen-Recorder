#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author : @m4lal0
# github : @m4lal0
# version : 1.0.0
# date : 10/4/2021
# project name : ScreenSaverPreventer
# software name : ScreenSaverPreventer
"""
ScreenSaverPreventer is a Python script that prevents 
the user from locking the screen using the PyAutoGUI library.
"""
import random
import time

import pyautogui

# Set the random duration between
RANDOM_DURATION: tuple[int, int] = (1, 5)
MARGIN: int = 10

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()

# Run indefinitely
while True:
    # Generate a random x and y coordinate
    x = random.randint(0, screenWidth - MARGIN)
    y = random.randint(0, screenHeight - MARGIN)
    print(screenHeight, screenWidth)

    # Move the mouse to the random x and y coordinates
    pyautogui.moveTo(
        x,
        y,
        duration=random.randint(1, 3),
        tween=pyautogui.easeOutQuad,
    )

    # Wait for 10 seconds before moving the mouse again
    duration = random.randint(*RANDOM_DURATION)
    print(f"duration : {duration}!")
    time.sleep(duration)
