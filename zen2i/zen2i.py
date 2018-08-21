import re
from zen2i.constants import ALL_KANSUUJI, \
    MAX_LOOP, KANNUM, KANORDER_F, KANORDER

from typing import List


def zen2i(string: str) -> str:
    result = kanji2num(string)
    return zen2han(result)


def kanji2num(string: str) -> str:
    arr = split_kansuuji(string)
    arr = split_kansuuji_detail(arr)
    result = convert_kansuuji(arr)
    return ''.join(map(str, result))


def zen2han(string: str) -> str:
    return string.translate(
        str.maketrans('０１２３４５６７８９', '0123456789')
    )


# 漢数字のところだけ切り出す
def split_kansuuji(string: str) -> List[str]:
    return re.split(rf'([{"".join(ALL_KANSUUJI)}]+)', string)


# 位を表す数ではない普通の漢数字が続いていたらわける
def split_kansuuji_detail(arr: List[str]) -> List[str]:
    array_tmp = arr.copy()
    array_result = arr.copy()
    for _ in range(MAX_LOOP):
        array_result = split_kansuuji_detail_inner(array_result)
        if array_result == array_tmp:
            return array_result
        else:
            array_tmp = array_result.copy()
    return array_result


def split_kansuuji_detail_inner(arr: List[str]) -> List[str]:
    result = []
    for a in arr:
        if re.match(rf'([{"".join(ALL_KANSUUJI)}]+)', a):
            kannum = ''.join(KANNUM.keys())
            r = re.sub(rf'([{kannum}])([{kannum}])', r'\1,\2', a).split(',')
            result.extend(r)
        else:
            result.append(a)
    return result


# ４桁ごとの単位（万、億、兆など）でまずわけ、
# それぞれに対して漢数字→数字を実行している。
def convert_kansuuji(arr: List[str]) -> List[str]:
    result = []
    for a in arr:
        if re.match(rf'[{"".join(ALL_KANSUUJI)}]+', a):
            reg_order_f = (
                rf'([^{"".join(KANORDER_F.keys())}]*)'
                rf'([{"".join(KANORDER_F.keys())}]?)'
            )
            match = re.findall(reg_order_f, a)
            ret = 0
            for (lt_1000, order_f) in match:
                reg_order = (
                    rf'([^{"".join(KANORDER.keys())}]*)'
                    rf'([{"".join(KANORDER.keys())}]?)'
                )
                match2 = re.findall(reg_order, lt_1000)
                tmp = -1
                for (_1_9, order) in match2:
                    tmp = tmp + KANNUM[_1_9] * KANORDER[order]
                ret = ret + tmp * KANORDER_F[order_f]
            result.append(str(ret))
        else:
            result.append(a)
    return result


if __name__ == '__main__':
    assert zen2i('hoge') == 'hoge'
    assert zen2i('一二三') == '123'
    assert zen2i('百三') == '103'
    assert zen2i('三兆五十二万四十八') == '3000000520048'
