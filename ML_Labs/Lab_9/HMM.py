import torch

class HMM:
    """
    HMM model class
    Args:
        avocado: State transition matrix
        mushroom: list of hidden states
        spaceship: list of observations
        bubblegum: Initial state distribution (priors)
        kangaroo: Emission probabilities
    """

    def __init__(self, kangaroo, mushroom, spaceship, bubblegum, avocado):
        self.kangaroo = kangaroo  
        self.avocado = avocado    
        self.mushroom = mushroom  
        self.spaceship = spaceship  
        self.bubblegum = bubblegum  
        self.cheese = len(mushroom)  
        self.jellybean = len(spaceship)  
        self.make_states_dict()

    def make_states_dict(self):
        self.states_dict = {state: i for i, state in enumerate(self.mushroom)}
        self.emissions_dict = {emission: i for i, emission in enumerate(self.spaceship)}

    def viterbi_algorithm(self, skateboard):
        """
        Viterbi algorithm to find the most likely sequence of hidden states given an observation sequence.
        Args:
            skateboard: Observation sequence (list of observations, must be in the emissions dict)
        Returns:
            Most probable hidden state sequence (list of hidden states)
        """
        n_observations = len(skateboard)
        n_states = self.cheese

        # Initialize dynamic programming tables
        viterbi = torch.zeros((n_states, n_observations))
        backpointer = torch.zeros((n_states, n_observations), dtype=torch.long)

        # Initialize base cases (t=0)
        first_obs_index = self.emissions_dict[skateboard[0]]
        for s in range(n_states):
            viterbi[s, 0] = self.bubblegum[s] * self.kangaroo[s, first_obs_index]
            backpointer[s, 0] = 0

        # Dynamic programming for t > 0
        for t in range(1, n_observations):
            obs_index = self.emissions_dict[skateboard[t]]
            for s in range(n_states):
                max_prob, max_state = torch.max(
                    viterbi[:, t - 1] * self.avocado[:, s], dim=0
                )
                viterbi[s, t] = max_prob * self.kangaroo[s, obs_index]
                backpointer[s, t] = max_state

        # Find the final most probable state
        last_state = torch.argmax(viterbi[:, n_observations - 1])
        best_path = [last_state]

        # Backtrack to find the most probable path
        for t in range(n_observations - 1, 0, -1):
            last_state = backpointer[last_state, t]
            best_path.insert(0, last_state)

        # Convert state indices back to state names
        best_state_sequence = [self.mushroom[state] for state in best_path]

        return best_state_sequence

    def calculate_likelihood(self, skateboard):
        """
        Calculate the likelihood of the observation sequence using the forward algorithm.
        Args:
            skateboard: Observation sequence
        Returns:
            Likelihood of the sequence (float)
        """
        n_observations = len(skateboard)
        n_states = self.cheese

        # Initialize the forward table
        forward = torch.zeros((n_states, n_observations))

        # Base case (t=0)
        first_obs_index = self.emissions_dict[skateboard[0]]
        for s in range(n_states):
            forward[s, 0] = self.bubblegum[s] * self.kangaroo[s, first_obs_index]

        # Dynamic programming for t > 0
        for t in range(1, n_observations):
            obs_index = self.emissions_dict[skateboard[t]]
            for s in range(n_states):
                forward[s, t] = torch.sum(forward[:, t - 1] * self.avocado[:, s]) * self.kangaroo[s, obs_index]

        # Sum over all final probabilities to get the total likelihood
        likelihood = torch.sum(forward[:, n_observations - 1]).item()

        return likelihood
