from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from mipac.types.user import IUserDetailed


class IMutedUser(TypedDict):
    id: str
    created_at: str
    expires_at: str | None
    mutee_id: str
    mutee: IUserDetailed
