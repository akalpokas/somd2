######################################################################
# SOMD2: GPU accelerated alchemical free-energy engine.
#
# Copyright: 2023-2024
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

"""
The somd2 command line program.

Usage:
    To get the help for this program and list all of the
    arguments (with defaults) use:

    somd2 --help
"""


def cli():
    """
    SOMD2: Command line interface.
    """

    from argparse import Namespace

    from somd2 import _logger
    from somd2.config import Config
    from somd2.runner import Runner

    from somd2.io import yaml_to_dict

    # Store the somd2 version.
    from somd2._version import __version__

    # Store the sire version.
    from sire import __version__ as sire_version
    from sire import __revisionid__ as sire_revisionid

    # Generate the parser.
    parser = Config._create_parser()

    # Add simulation specific positional arguments.
    parser.add_argument(
        "system",
        type=str,
        help="Path to a stream file containing the perturbable system.",
    )

    # Parse the arguments into a dictionary.
    args = vars(parser.parse_args())

    # Pop the YAML config and system from the arguments dictionary.
    config = args.pop("config")
    system = args.pop("system")

    # If set, read the YAML config file.
    if config is not None:
        # Convert the YAML config to a dictionary.
        config = yaml_to_dict(config)

        # Reparse the command-line arguments using the existing config
        # as a Namespace. Any non-default arguments from the command line
        # will override those in the config.
        args = vars(parser.parse_args(namespace=Namespace(**config)))

        # Re-pop the YAML config and system from the arguments dictionary.
        args.pop("config")
        args.pop("system")

    # Instantiate a Config object to validate the arguments.
    config = Config(**args)

    # Log the versions of somd2 and sire.
    _logger.info(f"somd2 version: {__version__}")
    _logger.info(f"sire version: {sire_version}+{sire_revisionid}")

    # Instantiate a Runner object to run the simulation.
    runner = Runner(system, config)

    # Run the simulation.
    runner.run()
