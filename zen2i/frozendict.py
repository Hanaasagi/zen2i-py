import collections

# flake8 will complain Optional imported but not used
from typing import Hashable, Iterator, TypeVar, Any, Optional  # noqa


T = TypeVar('T', bound='frozendict')

class frozendict(collections.Mapping):  # noqa

    dict_cls = dict

    def __init__(self, *args, **kwargs) -> None:  # type: ignore
        self._dict = self.dict_cls(*args, **kwargs)
        self._hash: Optional[int] = None

    def __getitem__(self, key: Hashable) -> Any:
        return self._dict[key]

    def __contains__(self, key: Hashable) -> bool:
        return key in self._dict

    def copy(self: T, **add_or_replace) -> T:  # type: ignore
        return self.__class__(self, **add_or_replace)

    def __iter__(self) -> Iterator:
        return iter(self._dict)

    def __len__(self) -> int:
        return len(self._dict)

    def __repr__(self) -> str:
        return '<%s %r>' % (self.__class__.__name__, self._dict)

    def __hash__(self) -> int:
        if self._hash is None:
            h = 0
            for key, value in self._dict.items():
                h ^= hash((key, value))
            self._hash = h
        return self._hash


__all__ = [
    'frozendict'
]
