from zen2i.frozendict import frozendict


KANNUM = frozendict({
    '〇': 0,
    '零': 0,
    '':   1,  # noqa
    '一': 1,
    '壱': 1,
    '二': 2,
    '弐': 2,
    '三': 3,
    '参': 3,
    '四': 4,
    '肆': 4,
    '五': 5,
    '伍': 5,
    '六': 6,
    '陸': 6,
    '七': 7,
    '漆': 7,
    '八': 8,
    '捌': 8,
    '九': 9,
    '玖': 9
})

KANORDER = frozendict({
    ''  : 1,  # noqa
    '十': 10,
    '拾': 10,
    '百': 100,
    '陌': 100,
    '佰': 100,
    '千': 1000,
    '阡': 1000,
    '仟': 1000
})

KANORDER_F = frozendict({
    '':   1,  # noqa
    '万': 10**4,
    '萬': 10**4,
    '億': 10**8,
    '兆': 10**12
})

ALL_KANSUUJI = sum(
    [list(d.keys()) for d in (KANNUM, KANORDER, KANORDER_F)],
    []
)

MAX_LOOP = 100
