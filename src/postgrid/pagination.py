# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncSkipLimit", "AsyncSkipLimit"]

_T = TypeVar("_T")


class SyncSkipLimit(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("skip") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "skip" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"skip": current_count})

        return None


class AsyncSkipLimit(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("skip") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "skip" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"skip": current_count})

        return None
