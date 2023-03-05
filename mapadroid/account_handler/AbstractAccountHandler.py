import datetime
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

from mapadroid.db.model import SettingsPogoauth
from mapadroid.utils.collections import Location


class AccountPurpose(Enum):
    LEVEL = "level"
    QUEST = "quest"
    IV = "iv"
    MON_RAID = "mon_raid"


class BurnType(Enum):
    BAN = "ban"
    MAINTENANCE = "maintenance"


class AbstractAccountHandler(ABC):
    @abstractmethod
    def get_account(self, device_id: int, purpose: AccountPurpose,
                    location_to_scan: Location, including_google: bool = True) -> Optional[SettingsPogoauth]:
        """
        Searches for an available (i.e., known to not be cooling down) account in the settings_pogoauth table
        Returns: a pogoauth entry to be used to which the worker can try to log in

        """

    @abstractmethod
    def mark_burnt(self, device_id: int, burn_type: Optional[BurnType]) -> None:
        """
        Marks the account to which the device identified by the device_id is bound to as burnt with the time of calling
        Returns:

        """

    @abstractmethod
    def set_last_softban_action(self, device_id: int, time_of_action: datetime.datetime,
                                location_of_action: Location) -> None:
        """
        Stores the information on when the last softban action for the account currently associated to device was
        performed.
        Args:
            device_id:
            time_of_action:
            location_of_action:

        Returns:

        """
