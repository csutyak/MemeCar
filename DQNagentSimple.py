import torch as T
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

class DeepQNetwork(nn.Module):
    def __init__(self, lr, input_dims, fc1_dims, fc2_dims, n_actions):
        super(DeepQNetwork, self).__init__()
        self.input_dims = input_dims
        self.fc1_dims = fc1_dims
        self.fc2_dims = fc2_dims
        self.n_actions = n_actions
        self.fc1 = nn.Linear(*self.input_dims, self.fc1_dims)
        self.fc2 = nn.Linear(self.fc1_dims, self.fc2_dims)
        self.fc3 = nn.Linear(self.fc2_dims, n_actions)
        self.optimizer = optim.Adam(self.parameters(), lr=lr)
        self.loss = nn.MSELoss()
        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
        self.to(self.device)

    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        actions = self.fc3(x)

        return actions

class Agent():
    def __init__ (self, gamma, epsilon, lr, input_dims, batch_size, n_actions, 
            mem_size =1000000, eps_end=0.01, eps_dec=5e-7, replace = 1000):
        self.gamma = gamma
        self.epsilon = epsilon
        self.eps_min = eps_end
        self.eps_dec = eps_dec
        self.lr = lr
        self.action_space = [i for i in range(n_actions)]
        self.batch_size = batch_size 
        self.mem_cntr = 0
        self.replace_target_cnt = replace
        self.learn_step_counter = 0

        self.memory = replayBuffer(mem_size, input_dims, n_actions)

        self.Q_eval = DeepQNetwork(self.lr, n_actions=n_actions, input_dims=input_dims, fc1_dims=256, fc2_dims=256)
        self.Q_next = DeepQNetwork(self.lr, n_actions=n_actions, input_dims=input_dims, fc1_dims=256, fc2_dims=256)

    def choose_action(self, observation):
        if np.random.random() > self.epsilon:
            state = T.tensor([observation]).to(self.Q_eval.device)
            actions = self.Q_eval.forward(state)
            action = T.argmax(actions).item()
        else:
            action = np.random.choice(self.action_space)
        
        return action
    
    def store_transition(self, state, action, reward, newState, done):
        self.memory.store_transition(state, action, reward, newState, done)
    
    def  sample_memory(self):
        state, action, reward, new_state, done = self.memory.sample_buffer(self.batch_size)

        states = T.tensor(state).to(self.Q_eval.device)
        actions = T.tensor(action).to(self.Q_eval.device)
        rewards = T.tensor(reward).to(self.Q_eval.device)
        new_states = T.tensor(new_state).to(self.Q_eval.device)
        dones = T.tensor(done).to(self.Q_eval.device)

        return states, actions, rewards, new_states, dones

    def replace_target_network(self):
        if self.learn_step_counter % self.replace_target_cnt == 0:
            self.Q_next.load_state_dict(self.Q_eval.state_dict())

    
    def decrement_epsilon(self):
        self.epsilon = self.epsilon - self.eps_dec if self.epsilon > self.eps_min \
                        else self.eps_min
    
    def learn(self):
        if self.memory.mem_ctr < self.batch_size:
            return
        
        self.Q_eval.optimizer.zero_grad()

        self.replace_target_network()

        states, actions, rewards, newStates, dones = self.sample_memory()

        indicies = np.arange(self.batch_size)
        q_pred = self.Q_eval.forward(states)[indicies, actions]
        q_next = self.Q_next.forward(newStates).max(dim=1)[0]

        q_next[dones] = 0.0
        q_target = rewards + self.gamma*q_next

        loss = self.Q_eval.loss(q_target, q_pred).to(self.Q_eval.device)
        loss.backward()
        self.Q_eval.optimizer.step()
        self.learn_step_counter += 1

        self.decrement_epsilon()


    
    def save(self, gameCtr):
        PATH = "output/state_dict_model"+ str(gameCtr) + ".pt"
        PATH2 = "output/state_dict_model2"+ str(gameCtr) + ".pt"

        # Save
        T.save(self.Q_eval.state_dict(), PATH)
        T.save(self.Q_next.state_dict(), PATH)

class replayBuffer():
    def __init__ (self, max_size, input_shape, n_actions):
        self.mem_size = max_size
        self.mem_ctr = 0
        self.state_memory = np.zeros((self.mem_size, *input_shape), dtype=np.float32)
        self.new_state_memory = np.zeros((self.mem_size, *input_shape), dtype=np.float32)
        self.action_memory = np.zeros(self.mem_size, dtype=np.int64)
        self.reward_memory = np.zeros(self.mem_size, dtype=np.float32)
        self.terminal_memory = np.zeros(self.mem_size, dtype=np.bool)
    
    def store_transition(self, currentState, action, reward, newState, done):
        index = self.mem_ctr % self.mem_size
        self.state_memory[index] = currentState
        self.action_memory[index] = action
        self.reward_memory[index] = reward
        self.new_state_memory[index] = newState
        self.terminal_memory[index] = done

        self.mem_ctr += 1

    def sample_buffer(self, batch_size):
        max_mem = min(self.mem_ctr, self.mem_size)
        batch = np.random.choice(max_mem, batch_size, replace = False)

        states = self.state_memory[batch]
        actions = self.action_memory[batch]
        rewards = self.reward_memory[batch]
        newState = self.new_state_memory[batch]
        dones = self.terminal_memory[batch]

        return states, actions, rewards, newState, dones