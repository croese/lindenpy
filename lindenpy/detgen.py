from typing import Dict


class DetGen:
    def __init__(self, axiom: str, rules: Dict[str, str]) -> None:
        self.axiom = axiom
        self.tr_table = str.maketrans(rules)

    def gen(self, n: int) -> str:
        cur = self.axiom
        for i in range(n):
            cur = cur.translate(self.tr_table)

        return cur
