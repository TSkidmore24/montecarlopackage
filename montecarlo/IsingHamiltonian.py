import numpy as np
import networkx as nx
import math
import montecarlo

class IsingHamiltonian:
    """Class for an Ising Hamiltonian of arbitrary dimensionality

    .. math::
        H = \\sum_{\\left<ij\\right>} J_{ij}\\sigma_i\\sigma_j + \\sum_i\\mu_i\\sigma_i

    """

    def __init__(self, J=[[()]], mu=np.zeros(1)):
        """Constructor

        Parameters
        ----------
        J: list of lists of tuples, optional
            Strength of coupling, e.g,
            [(4, -1.1), (6, -.1)]
            [(5, -1.1), (7, -.1)]
        mu: vector, optional
            local fields
        """
        self.J = J
        self.mu = mu

        self.nodes = []
        self.js = []

        for i in range(len(self.J)):
            self.nodes.append(np.zeros(len(self.J[i]), dtype=int))
            self.js.append(np.zeros(len(self.J[i])))
            for jidx, j in enumerate(self.J[i]):
                self.nodes[i][jidx] = j[0]
                self.js[i][jidx] = j[1]
        self.mu = np.array([i for i in self.mu])
        self.N = len(self.J)

    def energy(self, config):
        """Compute energy of configuration, `config`

            .. math::
                E = \\left<\\hat{H}\\right>

        Parameters
        ----------
        config   : BitString
            input configuration

        Returns
        -------
        energy  : float
            Energy of the input configuration
        """
        if len(config.config) != len(self.J):
            raise ValueError("wrong dimension")

        e = 0.0
        for i in range(config.N):
            # print()
            # print(i)
            for j in self.J[i]:
                if j[0] < i:
                    continue
                # print(j)
                if config.config[i] == config.config[j[0]]:
                    e += j[1]
                else:
                    e -= j[1]

        e += np.dot(self.mu, 2 * config.config - 1)
        return e

    def compute_average_values(bs: montecarlo.BitString, G: nx.Graph, T: float):
        #k = 1.38064852 * math.pow(10, -23)
        k=1
        beta = 1 / (k * T)
        energy_and_mag_values = []
        possible_configs = 2 ** len(bs)
        Z = 0.0

        # Compute energies and magnetizations for all configurations
        for index in range(possible_configs):
            bs.set_int_config(index)
            en = montecarlo.energy(bs, G)
            m = bs.on() - bs.off()
            energy_and_mag_values.append((en, m))
            Z += math.exp(-beta * en)

        # Calculate probabilities and average values
        E = 0.0
        M = 0.0
        M_squared = 0.0
        E_squared = 0.0
        for energy_of_config, mag_of_config in energy_and_mag_values:
            prob_of_config = math.exp(-beta * energy_of_config) / Z
            weighted_energy = prob_of_config * energy_of_config
            weighted_mag = prob_of_config * mag_of_config
            M_squared += prob_of_config * mag_of_config**2
            E_squared += prob_of_config * energy_of_config**2
            E += weighted_energy
            M += weighted_mag

        # Additional calculations for heat capacity and magnetic susceptibility
        HC = (1/T**2) * (E_squared - E**2)
        MS = (1/T) * (M_squared - M**2)

        return E, M, HC, MS
    