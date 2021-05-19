import torch
from torch import nn
from torch.nn import functional as F
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"

class Network(nn.Module):
	def __init__(self, 
				 input_vars, 
				 ex_vars, 
				 device, 
				 hyper_parameters,
				 max_x3_len=19,
				 unrestricted=True):
			
		super(Network, self).__init__()	 
		self.input_vars = input_vars #Number of variables at each step of input sequence
		self.ex_vars = ex_vars #Number of variables appended to lstm output
		self.num_fc_layers = hyper_parameters['fc_layers']
		self.fc_units = hyper_parameters['fc_units'] #Number of units in each fully connected layer
		self.r_units = hyper_parameters['r_units'] #Number of units in each LSTM
		self.bs = hyper_parameters['batch_size'] #Batch size
		self.dropout_rate = hyper_parameters['dropout']
		self.max_x3_len = max_x3_len #Max length of the prediction window
		self.unrestricted = unrestricted
		self.device = device
		
		self.lstm1 = nn.LSTM(self.input_vars, 
							 self.r_units, 
							 num_layers=1,
							 batch_first=True,
							 bidirectional=True)			
		
		self.map_h = nn.Linear((2 * self.r_units), self.r_units)
		
		self.map_c = nn.Linear((2 * self.r_units), self.r_units)
				 
		self.lstm2 = nn.LSTM(self.input_vars - 1,
							 self.r_units,
							 num_layers=1,
							 batch_first=True,
							 bidirectional=False)
		
		self.fc_layers = nn.ModuleList()
		if self.unrestricted:
			if self.num_fc_layers == 1:
				self.fc_layers.append(nn.Linear((self.r_units * 3) + self.ex_vars, 1))
			else:
				self.fc_layers.append(nn.Linear((self.r_units * 3) + self.ex_vars, self.fc_units))
		else:
			if self.num_fc_layers == 1:
				self.fc_layers.append(nn.Linear((self.r_units * 2) + self.ex_vars, 1))
			else:
				self.fc_layers.append(nn.Linear((self.r_units * 2) + self.ex_vars, self.fc_units))
			
		if self.num_fc_layers > 2:
			for i in range(2, self.num_fc_layers):
				self.fc_layers.append(nn.Linear(self.fc_units, self.fc_units))
			
		if self.num_fc_layers >= 2:
			self.fc_layers.append(nn.Linear(self.fc_units, 1))
		
		self.tanh = nn.Tanh()
		
		self.relu = nn.ReLU()
		
		self.dropout = nn.Dropout(self.dropout_rate)
		
		self.h_0 = torch.zeros((2, self.bs, self.r_units)).to(self.device)
		self.c_0 = torch.zeros((2, self.bs, self.r_units)).to(self.device)
		
		
	def forward(self, x, x2, x3=None):
		samples = x.shape[0]
		if samples < self.bs:
			x = F.pad(input=x, pad=(0, 0, 0, 0, 0, self.bs - samples), mode='constant', value=0)
			x2 = F.pad(input=x2, pad=(0, 0, 0, self.bs - samples), mode='constant', value=0)
			if x3 is not None:
				x3 = F.pad(input=x3, pad=(0, 0, 0, 0, 0, self.bs - samples), mode='constant', value=0)
				
		self.h_0 = self.h_0.data
		self.c_0 = self.c_0.data
	
		lstm1_out, (self.h_0, self.c_0) = self.lstm1(x, (self.h_0, self.c_0))
		
		lstm1_out = self.dropout(lstm1_out)
		
		if x3 is not None:
			h2_0 = self.h_0.data.permute(1, 0, 2).flatten(1)
			c2_0 = self.c_0.data.permute(1, 0, 2).flatten(1)
			
			h2_0 = self.tanh(self.map_h(h2_0))
			c2_0 = self.tanh(self.map_c(c2_0))
			
			h2_0 = h2_0.reshape((self.bs, 1, self.r_units)).permute(1, 0, 2).data.contiguous()
			c2_0 = c2_0.reshape((self.bs, 1, self.r_units)).permute(1, 0, 2).data.contiguous()
			
			sequence_lengths = (x2[:, 1] * self.max_x3_len)
			sequence_lengths = sequence_lengths.type(torch.long).data
			
			batch_indicies = [i for i in range(self.bs)]
			time_indicies = [l for l in sequence_lengths]

			lstm2_out, _ = self.lstm2(x3, (h2_0, c2_0))
			
			lstm2_out = lstm2_out[batch_indicies, time_indicies, :].unsqueeze(1)
			
			lstm2_out = self.dropout(lstm2_out)
		
		if x3 is not None:
			lstm_out = torch.cat((lstm1_out[:, -1, :], lstm2_out[:, -1, :]), dim=1)
		else:
			lstm_out = lstm1_out[:, -1, :]	
			
		x_ = torch.cat((lstm_out, x2), dim=1)
		
		for i in range(len(self.fc_layers) - 1):
			x_ = self.fc_layers[i](x_)
			x_ = self.relu(x_)
			x_ = self.dropout(x_)
			
		x_ = self.fc_layers[len(self.fc_layers) - 1](x_)
		
		return x_[:samples, :]
