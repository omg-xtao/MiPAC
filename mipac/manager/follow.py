from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from mipac.abstract.manager import AbstractManager
from mipac.actions.follow import FollowActions, FollowRequestActions
from mipac.http import HTTPClient

if TYPE_CHECKING:
    from mipac.client import ClientActions

__all__ = ('FollowManager', 'FollowRequestManager')


class FollowManager(AbstractManager):
    def __init__(
        self,
        user_id: Optional[str] = None,
        *,
        session: HTTPClient,
        client: ClientActions
    ):
        self.__user_id: Optional[str] = user_id
        self.__session: HTTPClient = session
        self.__client: ClientActions = client
        self.request: FollowRequestManager = FollowRequestManager(
            user_id=user_id, session=session, client=client
        )

    @property
    def action(self) -> FollowActions:
        return FollowActions(
            user_id=self.__user_id,
            session=self.__session,
            client=self.__client,
        )


class FollowRequestManager(AbstractManager):
    def __init__(
        self,
        user_id: Optional[str] = None,
        *,
        session: HTTPClient,
        client: ClientActions
    ):
        self.__user_id: Optional[str] = user_id
        self.__session: HTTPClient = session
        self.__client: ClientActions = client

    @property
    def action(self) -> FollowRequestActions:
        return FollowRequestActions(
            user_id=self.__user_id,
            session=self.__session,
            client=self.__client,
        )
