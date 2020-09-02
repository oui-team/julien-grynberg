from typing import List

from pandas import DataFrame


class ProductionSumer:
    def __init__(self, dfs: List[DataFrame]) -> None:
        self.dfs = dfs

    def sum(self) -> DataFrame:
        merged_df = self.dfs[0]
        for df in self.dfs[1:]:
            merged_df = merged_df.append(df, ignore_index=True)
        return merged_df.groupby(['start', 'end']).sum()


def sum_ppp(dfs: List[DataFrame]) -> DataFrame:
    return ProductionSumer(dfs).sum().reset_index()
