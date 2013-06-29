Pyroku
######

Pyroku wraps the API provided by Roku devices to simplify its integration into your Python scripts.

Usage
-----

All you need to do is import pyroku, create a Roku object, and pass it the IP of your Roku box.

.. code-block:: python

    >>> import pyroku
    >>> roku = pyroku.Roku('192.168.0.25')
    >>> roku.press_pause()

The buttons available are called like so:

.. code-block:: python

    >>> roku.press_pause()
    >>> roku.press_play()
    >>> roku.press_home()
    >>> roku.press_reverse()
    >>> roku.press_forward()
    >>> roku.press_select()
    >>> roku.press_left()
    >>> roku.press_right()
    >>> roku.press_down()
    >>> roku.press_up()
    >>> roku.press_back()
    >>> roku.press_instant_replay()
    >>> roku.press_search()
