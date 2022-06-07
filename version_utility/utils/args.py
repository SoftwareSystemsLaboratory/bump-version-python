"""
File to handle command line arguements
"""

from argparse import ArgumentParser, HelpFormatter, Namespace
from operator import attrgetter

from version_utility.utils.self import readVersion

name: str = "SSL Version Utility"
authors: list = ["Nicholas M. Synovic"]
versionString: list = f"{name}: {readVersion()}"


class SortingHelpFormatter(HelpFormatter):
    """
    SortingHelpFormatter _summary_

    _extended_summary_

    :param HelpFormatter: _description_
    :type HelpFormatter: _type_
    """

    def add_arguments(self, actions):
        """
        add_arguments _summary_

        _extended_summary_

        :param actions: _description_
        :type actions: _type_
        """
        actions = sorted(actions, key=attrgetter("option_strings"))
        super(SortingHelpFormatter, self).add_arguments(actions)


def mainArgs() -> Namespace:
    """
    mainArgs _summary_

    _extended_summary_

    :return: _description_
    :rtype: Namespace
    """
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Version Utility",
        usage="Utility tool to handle versions of Software and Systems Laboratory (SSL) projects",
        description="This utility is meant to be used as a development dependency to version bump a project, or to retrieve the version number for a SSL project.",
        epilog=f"Author(s): {', '.join(authors)}",
        formatter_class=SortingHelpFormatter,
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Print version of the tool",
        version=versionString,
    )
    parser.add_argument(
        "-r",
        "--read-version",
        action="store_true",
        required=False,
        help="Flag to read version value from file: DEFAULT: False",
    )
    parser.add_argument(
        "-s",
        "--set-version",
        default=None,
        type=str,
        required=False,
        help="Set version of project to a value. DEFAULT: None",
    )
    parser.add_argument(
        "-f",
        "--file",
        default="pyproject.toml",
        type=str,
        required=False,
        help="Filepath to change project version. DEFAULT: pyproject.toml",
    )

    return parser.parse_args()
