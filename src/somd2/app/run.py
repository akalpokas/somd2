######################################################################
# SOMD2: GPU accelerated alchemical free-energy engine.
#
# Copyright: 2023
#
# Authors: The OpenBioSim Team <team@openbiosim.org>
#
# SOMD2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SOMD2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SOMD2. If not, see <http://www.gnu.org/licenses/>.
#####################################################################

#!/usr/bin/env python

"""
The somd2 command line program.

Usage:
    To get the help for this program and list all of the
    arguments (with defaults) use:

    somd2 --help
"""


def cli():
    """
    SOMD2: Command-line interface.
    """

    from somd2.config import Config
    from somd2.runner import Runner

    # Generate the parser.
    parser = Config._create_parser()

    # Parse the arguments into a dictionary.
    args = vars(parser.parse_args())

    # Pop config and system from the arguments dictionary.
    config = args.pop("config")
    system = args.pop("system")

    # Instantiate a Config object to validate the arguments.
    config = Config(**args)

    # Instantiate a Runner object to run the simulation.
    runner = Runner(system, config)

    # Run the simulation.
    runner.run()
