#! /usr/bin/env python
''' This module provides a simple interface to the Roku
    streaming media player.
    '''

__author__ = "Alex Philipp"
__email__ = "alex@snapfiber.com"
__license__ = """
Copyright (c) 2013 Alex Philipp <alex@snapfiber.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
USA

"""

try:
    import requests
except:
    raise Exception("""
                    You will need to install the requests module. Try
                    "pip install requests".
                    """
                    )

class Roku(object):
    ''' Primary Roku object. '''

    def __init__(self, roku_ip, roku_port='8060'):
        self.roku_address = roku_ip + ":" + roku_port

    def keypress(self, button):
        ''' Hits the Roku REST API and requests a keypress.
            @button: Which button should be hit.
            '''
        requests.post('http://' + self.roku_address + "/keypress/" + button)

    def press_pause(self):
        ''' Presses the pause button. '''
        self.keypress('Play')

    def press_play(self):
        ''' Presses the play button. '''
        self.keypress('Play')

    def press_home(self):
        ''' Presses the home button. '''
        self.keypress('Home')

    def press_reverse(self):
        ''' Presses the reverse button. '''
        self.keypress('Rev')

    def press_forward(self):
        ''' Presses the forward button. '''
        self.keypress('Fwd')

    def press_select(self):
        ''' Presses the select button. '''
        self.keypress('Select')

    def press_left(self):
        ''' Presses the left button. '''
        self.keypress('Left')

    def press_right(self):
        ''' Presses the right button. '''
        self.keypress('Right')

    def press_down(self):
        ''' Presses the down button. '''
        self.keypress('Down')

    def press_up(self):
        ''' Presses the up button. '''
        self.keypress('Up')

    def press_back(self):
        ''' Presses the back button. '''
        self.keypress('Back')

    def press_instant_replay(self):
        ''' Presses the instant replay button. '''
        self.keypress('InstantReplay')

    def press_info(self):
        ''' Presses the info button. '''
        self.keypress('Info')

    def press_search(self):
        ''' Presses the search button. '''
        self.keypress('Search')
