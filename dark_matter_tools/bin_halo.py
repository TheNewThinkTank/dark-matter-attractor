# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import numpy as np
from typing import List
from tqdm import tqdm

from load_halo import LoadHalo


@dataclass
class BinHalo(LoadHalo):
    """Divide halo into bins."""
    nr_bins: int = 102
    r_middle: float = 10 ** 1.3
    r_cut_min: float = -1.5
    r_cut_max: float = np.log10(500.0)
    R: np.ndarray = field(init=False, repr=False)
    r_arr: List = field(init=False, repr=False, default_factory=list)
    sigma2_arr: List = field(init=False, repr=False)

    def __post_init__(self):
        super().__post_init__()
        self.R = self.get_moduli(self.x, self.y, self.z)
        # self.r_bin_automatic()
        self.binning_loop()

    def get_moduli(self, *args) -> np.ndarray:
        """Moduli of vector of arbitrary size."""
        return np.array(list(map(lambda x: sum(y ** 2 for y in x) ** .5, zip(*args))))

    def binning_loop(self):
        self.r_arr = []
        self.sigma2_arr = []

        bin_arr = np.logspace(self.r_cut_min, self.r_cut_max, self.nr_bins)
        for i in tqdm(range(self.nr_bins - 2)):
            min_r_i = bin_arr[i]
            max_r_i = bin_arr[i + 1]
            pos_r_par_i = np.where((min_r_i < self.R) * (self.R < max_r_i))
            nr_par_i = len(pos_r_par_i[0])
            if nr_par_i == 0:
                continue
            x = self.x[pos_r_par_i]
            y = self.y[pos_r_par_i]
            z = self.z[pos_r_par_i]
            vx = self.vx[pos_r_par_i]
            vy = self.vy[pos_r_par_i]
            vz = self.vz[pos_r_par_i]
            v = self.get_moduli(vx, vy, vz)
            v2_i = v ** 2

            # sigma2 total
            self.sigma2_arr.append(self.mean_velocity_slice(nr_par_i, v2_i))
            r_i = self.get_moduli(x, y, z)
            self.r_arr.append(r_i)
        self.sigma2_arr = np.array(self.sigma2_arr)
        self.r_arr = np.array(self.r_arr)

    def mean_velocity_slice(self, nr_par_bin, v):
        return (1. / (nr_par_bin + 1.)) * np.sum(v)

    def r_bin_automatic(self) -> None:
        """Make R_limit_min and R_limit_max selection automatic."""
        self.r_cut_min, self.r_cut_max = self.r_middle
        a = 0
        x0 = self.x
        while len(x0) < 10_000 or a == 0:
            self.r_cut_min -= .000_005
            self.r_cut_max += .000_005
            a = 1
            good_ids = np.where((self.R < self.r_cut_max) * (self.R > self.r_cut_min))
            x0 = self.x[good_ids[0]]


def main():
    halo = BinHalo('0G00_IC_000.hdf5')
    print(f"halo.filename: {halo.filename}")
    print(f"halo.sigma2_arr: {halo.sigma2_arr}")


if __name__ == '__main__':
    main()
