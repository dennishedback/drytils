#! /usr/bin/env python3

# drytils - Don't-Repeat-Yourself collection of utility functions using only the Python
# standard library as dependency.
#
# Copyright (C) 2022  Dennis Hedback
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Input utilites."""


import sys
from typing import Callable, TextIO


def yes_or_no(
    prompt: str = "Continue?",
    default: bool = False,
    print_callback: Callable[[str], None] = None,
    file_: TextIO = sys.stdout,
) -> bool:
    """Prompts the user for yes/no or variants such as YES, y, Y.

    ### Arguments:

    `prompt`: The message to show.

    `default`: True if yes is default, False if no is default.

    `print_callback`: Supply a custom callback on the form func(x: str). Use print()
                      if None.

    `file_`: File-like resource to use in calls to print(). If print_callback is
             specified, this will be ignored.

    ### Returns:

    Boolean indicating whether the user answered yes or no. True is yes,
    False is no.
    """
    default_str = "Y/n" if default else "y/N"
    print_str = "{0} [{1}]".format(prompt, default_str)
    if not print_callback:
        print(print_str, end=" ", file=file_)
    else:
        print_callback(print_str)
    answer = input()
    if len(answer) == 0:
        return default
    return answer.strip().lower()[0] == "y"
