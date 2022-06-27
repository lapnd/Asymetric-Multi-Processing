LEDS
====

Register Listing for LEDS
-------------------------

+----------------------------+------------------------------+
| Register                   | Address                      |
+============================+==============================+
| :ref:`LEDS_OUT <LEDS_OUT>` | :ref:`0x10001800 <LEDS_OUT>` |
+----------------------------+------------------------------+

LEDS_OUT
^^^^^^^^

`Address: 0x10001800 + 0x0 = 0x10001800`

    Led Output(s) Control.

    .. wavedrom::
        :caption: LEDS_OUT

        {
            "reg": [
                {"name": "out[9:0]", "bits": 10},
                {"bits": 22},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


