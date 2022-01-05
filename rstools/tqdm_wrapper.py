""" Author: Ryo Suzuki, Python Version: 3.8 """
import re

try:
    from tqdm import tqdm
except ImportError:
    print('TQDMWrapper bindings requires "tqdm" package.')
    print('Install it via command:')
    print('    pip install tqdm')
    raise


class TQDMWrapper(tqdm):
    bar_format = "{l_bar}{bar}| {n_fmt}/{total_fmt} [ {elapsed}<{remaining}, {rate_fmt}{postfix}]"
    desc = "processing progress"

    def __init__(self, iterable=None, desc=None, total=None, leave=True, file=None, ncols=None, mininterval=0.1,
                 maxinterval=10.0, miniters=None, ascii=None, disable=False, unit='it', unit_scale=False,
                 dynamic_ncols=False, smoothing=0.3, bar_format=bar_format, initial=0, position=None, postfix=None,
                 unit_divisor=1000, write_bytes=None, lock_args=None, nrows=None, colour=None, delay=0, gui=False,
                 suffix_length=50, **kwargs):
        self.__suffix_length = suffix_length

        super().__init__(iterable, desc, total, leave, file, ncols, mininterval, maxinterval, miniters, ascii, disable,
                         unit, unit_scale, dynamic_ncols, smoothing, bar_format, initial, position, postfix,
                         unit_divisor, write_bytes, lock_args, nrows, colour, delay, gui, **kwargs)

    @property
    def suffix_length(self):
        return self.__suffix_length

    @suffix_length.setter
    def suffix_length(self, suffix_length: (str, int)):
        self.__suffix_length = suffix_length

    def set_postfix_str_wrap(self, s='', refresh=True):
        if len(s) > self.__suffix_length:
            prefix = ".."
        else:
            prefix = "  "
        res_str = "[" + prefix + "{} ]".format(
            re.findall(".{" + str(self.__suffix_length) + "}$", s.ljust(self.__suffix_length))[0])
        super(TQDMWrapper, self).set_postfix_str(res_str, refresh=refresh)
