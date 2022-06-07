"""
File to handle command line arguements
"""

from argparse import Namespace, ArgumentParser, HelpFormatter
from operator import attrgetter


name: str = "SSL Version Utility"
authors: list = ["Nicholas M. Synovic"]

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
        actions = sorted(actions, key=attrgetter('option_strings'))
        super(SortingHelpFormatter, self).add_arguments(actions)


def mainArgs()  ->  Namespace:
    """
    mainArgs _summary_

    _extended_summary_

    :return: _description_
    :rtype: Namespace
    """
    parser: ArgumentParser = ArgumentParser(prog="SSL Version Utility", usage="Utility tool to handle versions of Software and Systems Laboratory (SSL) projects", description="This utility is meant to be used as a development dependency to version bump a project, or to retrieve the version number for a SSL project.", epilog=f"Author(s): {', '.join(authors)}", formatter_class=SortingHelpFormatter)

    return parser.parse_args()
