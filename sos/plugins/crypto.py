# Copyright (C) 2017 Red Hat, Inc., Bryn M. Reeves <bmr@redhat.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from sos.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin


class Crypto(Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin):
    """ System crypto services information
    """

    plugin_name = 'crypto'
    profiles = ('system', 'hardware')

    def setup(self):
        self.add_copy_spec([
            "/proc/crypto",
            "/proc/sys/crypto/fips_enabled"
        ])

# vim: et ts=4 sw=4
