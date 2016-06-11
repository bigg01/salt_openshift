# -*- coding: utf-8 -*-
'''

'''
from __future__ import absolute_import

# Import python libs
import os
import datetime

# Import salt libs
import salt.utils
from salt.exceptions import CommandExecutionError


def __virtual__():
    '''
    Only load module if oc binary is present
    '''
    if salt.utils.which('oc'):
        return __virtualname__
    return (False, 'The oc execution module cannot be loaded: '
            'the oc binary is not in the path.')



def set_mindays(name, mindays):
    '''
    Set the minimum number of days between password changes. See man chage.

    CLI Example:

    .. code-block:: bash

        salt '*' shadow.set_mindays username 7
    '''
    pre_info = info(name)
    if mindays == pre_info['min']:
        return True
    cmd = 'chage -m {0} {1}'.format(mindays, name)
    __salt__['cmd.run'](cmd, python_shell=False)
    post_info = info(name)
    if post_info['min'] != pre_info['min']:
        return post_info['min'] == mindays
    return False



"""
    cmd = 'passwd -d {0}'.format(name)
    __salt__['cmd.run'](cmd, python_shell=False, output_loglevel='quiet')
"""


def set_warndays(name, warndays):
    '''
    Set the number of days of warning before a password change is required.
    See man chage.

    CLI Example:

    .. code-block:: bash

        salt '*' shadow.set_warndays username 7
    '''
    pre_info = info(name)
    if warndays == pre_info['warn']:
        return True
    cmd = 'chage -W {0} {1}'.format(warndays, name)
    __salt__['cmd.run'](cmd, python_shell=False)
    post_info = info(name)
    if post_info['warn'] != pre_info['warn']:
        return post_info['warn'] == warndays
    return False


def set_date(name, date):
    '''
    Sets the value for the date the password was last changed to days since the
    epoch (January 1, 1970). See man chage.

    CLI Example:

    .. code-block:: bash

        salt '*' shadow.set_date username 0
    '''
    cmd = 'chage -d {0} {1}'.format(date, name)
    __salt__['cmd.run'](cmd, python_shell=False)


