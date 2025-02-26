from __future__ import annotations
from datetime import datetime

from typing import TYPE_CHECKING

from mipac.models.user import UserDetailedNotMe
from mipac.types.mute import IMutedUser
from mipac.utils.format import str_to_datetime

if TYPE_CHECKING:
    from mipac.manager.client import ClientManager


class MutedUser:
    def __init__(self, raw_mute_user: IMutedUser, *, client: ClientManager) -> None:
        self.__raw_mute_user: IMutedUser = raw_mute_user
        self.__client: ClientManager = client

    @property
    def id(self) -> str:
        return self.__raw_mute_user["id"]

    @property
    def created_at(self) -> str:
        return self.__raw_mute_user["created_at"]

    @property
    def expires_at(self) -> datetime | None:
        return (
            str_to_datetime(self.__raw_mute_user["expires_at"])
            if self.__raw_mute_user["expires_at"]
            else None
        )

    @property
    def mutee_id(self) -> str:
        return self.__raw_mute_user["mutee_id"]

    @property
    def mutee(self) -> UserDetailedNotMe:
        return UserDetailedNotMe(self.__raw_mute_user["mutee"], client=self.__client)

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, MutedUser) and self.id == __value.id

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
