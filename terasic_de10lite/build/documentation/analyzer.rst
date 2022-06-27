ANALYZER
========

Register Listing for ANALYZER
-----------------------------

+------------------------------------------------------------------+-------------------------------------------------+
| Register                                                         | Address                                         |
+==================================================================+=================================================+
| :ref:`ANALYZER_MUX_VALUE <ANALYZER_MUX_VALUE>`                   | :ref:`0x10000000 <ANALYZER_MUX_VALUE>`          |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_ENABLE <ANALYZER_TRIGGER_ENABLE>`         | :ref:`0x10000004 <ANALYZER_TRIGGER_ENABLE>`     |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_DONE <ANALYZER_TRIGGER_DONE>`             | :ref:`0x10000008 <ANALYZER_TRIGGER_DONE>`       |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_WRITE <ANALYZER_TRIGGER_MEM_WRITE>`   | :ref:`0x1000000c <ANALYZER_TRIGGER_MEM_WRITE>`  |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_MASK3 <ANALYZER_TRIGGER_MEM_MASK3>`   | :ref:`0x10000010 <ANALYZER_TRIGGER_MEM_MASK3>`  |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_MASK2 <ANALYZER_TRIGGER_MEM_MASK2>`   | :ref:`0x10000014 <ANALYZER_TRIGGER_MEM_MASK2>`  |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_MASK1 <ANALYZER_TRIGGER_MEM_MASK1>`   | :ref:`0x10000018 <ANALYZER_TRIGGER_MEM_MASK1>`  |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_MASK0 <ANALYZER_TRIGGER_MEM_MASK0>`   | :ref:`0x1000001c <ANALYZER_TRIGGER_MEM_MASK0>`  |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_VALUE3 <ANALYZER_TRIGGER_MEM_VALUE3>` | :ref:`0x10000020 <ANALYZER_TRIGGER_MEM_VALUE3>` |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_VALUE2 <ANALYZER_TRIGGER_MEM_VALUE2>` | :ref:`0x10000024 <ANALYZER_TRIGGER_MEM_VALUE2>` |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_VALUE1 <ANALYZER_TRIGGER_MEM_VALUE1>` | :ref:`0x10000028 <ANALYZER_TRIGGER_MEM_VALUE1>` |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_VALUE0 <ANALYZER_TRIGGER_MEM_VALUE0>` | :ref:`0x1000002c <ANALYZER_TRIGGER_MEM_VALUE0>` |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_TRIGGER_MEM_FULL <ANALYZER_TRIGGER_MEM_FULL>`     | :ref:`0x10000030 <ANALYZER_TRIGGER_MEM_FULL>`   |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_SUBSAMPLER_VALUE <ANALYZER_SUBSAMPLER_VALUE>`     | :ref:`0x10000034 <ANALYZER_SUBSAMPLER_VALUE>`   |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_STORAGE_ENABLE <ANALYZER_STORAGE_ENABLE>`         | :ref:`0x10000038 <ANALYZER_STORAGE_ENABLE>`     |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_STORAGE_DONE <ANALYZER_STORAGE_DONE>`             | :ref:`0x1000003c <ANALYZER_STORAGE_DONE>`       |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_STORAGE_LENGTH <ANALYZER_STORAGE_LENGTH>`         | :ref:`0x10000040 <ANALYZER_STORAGE_LENGTH>`     |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_STORAGE_OFFSET <ANALYZER_STORAGE_OFFSET>`         | :ref:`0x10000044 <ANALYZER_STORAGE_OFFSET>`     |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_STORAGE_MEM_LEVEL <ANALYZER_STORAGE_MEM_LEVEL>`   | :ref:`0x10000048 <ANALYZER_STORAGE_MEM_LEVEL>`  |
+------------------------------------------------------------------+-------------------------------------------------+
| :ref:`ANALYZER_STORAGE_MEM_DATA <ANALYZER_STORAGE_MEM_DATA>`     | :ref:`0x1000004c <ANALYZER_STORAGE_MEM_DATA>`   |
+------------------------------------------------------------------+-------------------------------------------------+

ANALYZER_MUX_VALUE
^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x0 = 0x10000000`


    .. wavedrom::
        :caption: ANALYZER_MUX_VALUE

        {
            "reg": [
                {"name": "mux_value", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


ANALYZER_TRIGGER_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x4 = 0x10000004`


    .. wavedrom::
        :caption: ANALYZER_TRIGGER_ENABLE

        {
            "reg": [
                {"name": "trigger_enable", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


ANALYZER_TRIGGER_DONE
^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x8 = 0x10000008`


    .. wavedrom::
        :caption: ANALYZER_TRIGGER_DONE

        {
            "reg": [
                {"name": "trigger_done", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


ANALYZER_TRIGGER_MEM_WRITE
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0xc = 0x1000000c`


    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_WRITE

        {
            "reg": [
                {"name": "trigger_mem_write", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


ANALYZER_TRIGGER_MEM_MASK3
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x10 = 0x10000010`

    Bits 96-107 of `ANALYZER_TRIGGER_MEM_MASK`.

    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_MASK3

        {
            "reg": [
                {"name": "trigger_mem_mask[127:96]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_TRIGGER_MEM_MASK2
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x14 = 0x10000014`

    Bits 64-95 of `ANALYZER_TRIGGER_MEM_MASK`.

    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_MASK2

        {
            "reg": [
                {"name": "trigger_mem_mask[95:64]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_TRIGGER_MEM_MASK1
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x18 = 0x10000018`

    Bits 32-63 of `ANALYZER_TRIGGER_MEM_MASK`.

    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_MASK1

        {
            "reg": [
                {"name": "trigger_mem_mask[63:32]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_TRIGGER_MEM_MASK0
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x1c = 0x1000001c`

    Bits 0-31 of `ANALYZER_TRIGGER_MEM_MASK`.

    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_MASK0

        {
            "reg": [
                {"name": "trigger_mem_mask[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_TRIGGER_MEM_VALUE3
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x20 = 0x10000020`

    Bits 96-107 of `ANALYZER_TRIGGER_MEM_VALUE`.

    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_VALUE3

        {
            "reg": [
                {"name": "trigger_mem_value[127:96]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_TRIGGER_MEM_VALUE2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x24 = 0x10000024`

    Bits 64-95 of `ANALYZER_TRIGGER_MEM_VALUE`.

    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_VALUE2

        {
            "reg": [
                {"name": "trigger_mem_value[95:64]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_TRIGGER_MEM_VALUE1
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x28 = 0x10000028`

    Bits 32-63 of `ANALYZER_TRIGGER_MEM_VALUE`.

    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_VALUE1

        {
            "reg": [
                {"name": "trigger_mem_value[63:32]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_TRIGGER_MEM_VALUE0
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x2c = 0x1000002c`

    Bits 0-31 of `ANALYZER_TRIGGER_MEM_VALUE`.

    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_VALUE0

        {
            "reg": [
                {"name": "trigger_mem_value[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_TRIGGER_MEM_FULL
^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x30 = 0x10000030`


    .. wavedrom::
        :caption: ANALYZER_TRIGGER_MEM_FULL

        {
            "reg": [
                {"name": "trigger_mem_full", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


ANALYZER_SUBSAMPLER_VALUE
^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x34 = 0x10000034`


    .. wavedrom::
        :caption: ANALYZER_SUBSAMPLER_VALUE

        {
            "reg": [
                {"name": "subsampler_value[15:0]", "bits": 16},
                {"bits": 16},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_STORAGE_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x38 = 0x10000038`


    .. wavedrom::
        :caption: ANALYZER_STORAGE_ENABLE

        {
            "reg": [
                {"name": "storage_enable", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


ANALYZER_STORAGE_DONE
^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x3c = 0x1000003c`


    .. wavedrom::
        :caption: ANALYZER_STORAGE_DONE

        {
            "reg": [
                {"name": "storage_done", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


ANALYZER_STORAGE_LENGTH
^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x40 = 0x10000040`


    .. wavedrom::
        :caption: ANALYZER_STORAGE_LENGTH

        {
            "reg": [
                {"name": "storage_length[9:0]", "bits": 10},
                {"bits": 22},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_STORAGE_OFFSET
^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x44 = 0x10000044`


    .. wavedrom::
        :caption: ANALYZER_STORAGE_OFFSET

        {
            "reg": [
                {"name": "storage_offset[9:0]", "bits": 10},
                {"bits": 22},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_STORAGE_MEM_LEVEL
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x48 = 0x10000048`


    .. wavedrom::
        :caption: ANALYZER_STORAGE_MEM_LEVEL

        {
            "reg": [
                {"name": "storage_mem_level[9:0]", "bits": 10},
                {"bits": 22},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


ANALYZER_STORAGE_MEM_DATA
^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x10000000 + 0x4c = 0x1000004c`


    .. wavedrom::
        :caption: ANALYZER_STORAGE_MEM_DATA

        {
            "reg": [
                {"name": "storage_mem_data[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


