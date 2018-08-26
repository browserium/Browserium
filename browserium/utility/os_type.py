# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The agenda for this documentation is to explain the utility for the class "OS_type".
# This class is used mainly to get the details of the respective environment based on your system.
# This information would help getting the required driver package or binaries based on your preferences.

import sys
import platform
import subprocess
from browserium.utility.utility import Utility
from subprocess import call

class OS_type(Utility):
    LINUX = "linux"
    MAC = "macos"
    WIN = "windows"

    # Get the required OS name
    @staticmethod
    def os_name():
        pl = sys.platform
        if "linux" in pl:
            return OS_type.LINUX
        if pl == "darwin":
            return OS_type.MAC
        if pl == "windows":
            return OS_type.WIN

    # Get OS architecture type
    @staticmethod
    def os_architecture():
        arch = platform.machine()
        if arch.endswith('64'):
            return 64
        else:
            return 32

    # Get the required OS type
    @staticmethod
    def os_type():
        return OS_type.os_name() + str(OS_type.os_architecture)

    # Get platform distribution type
    @staticmethod
    def distribution_type():
        dist_type = ""
        output = subprocess.check_output("cat /etc/*release | grep 'ID_LIKE'")
        if "debian" in output:
            dist_type = "debian"
        if "rhel fedora" in output:
            dist_type = "RHEL"
        return dist_type