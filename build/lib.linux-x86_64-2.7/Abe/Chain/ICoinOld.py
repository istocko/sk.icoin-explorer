# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .LtcScryptChain import LtcScryptChain

class ICoinOld(LtcScryptChain):
    def __init__(chain, **kwargs):
	chain.name = "ICoin"
	chain.code3 = "ICN"
        chain.address_version = "\x30"
        chain.script_addr_vers = "\x05"
        chain.magic = "\xfb\xc0\xb6\xdb"
	#super(ICoin, chain).__init__(**kwargs)	
	LtcScryptChain.__init__(chain, **kwargs)

    datadir_conf_file_name = "icoin.conf"
    datadir_rpcport = 9209
    datadir_p2pport = 9208
