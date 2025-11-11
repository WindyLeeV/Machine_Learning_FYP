import torch.nn as nn
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

# Define the FatGCN model
class FatGCN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(FatGCN, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x

# Define the MLP model
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.features = nn.Sequential(
            nn.Linear(3, 30), # 3 input, first layer 20 neurons
            nn.ReLU(inplace=True),
            # nn.Tanh(),
            nn.Linear(30, 10),  # second layer 10 neurons
            nn.ReLU(inplace=True),
            # nn.Tanh(),
            nn.Linear(10,1), # 1 output
        )


    def forward(self, x):
        x = self.features(x)
        # print(x)
        x = x.squeeze(-1)
        return x

    # def _initialize_weights(self):
    #     for m in self.modules():
    #         if isinstance(m, nn.Conv2d):
    #             nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
    #             if m.bias is not None:
    #                 nn.init.constant_(m.bias, 0)
    #         elif isinstance(m, nn.Linear):
    #             nn.init.normal_(m.weight, 0, 0.01)
    #             nn.init.constant_(m.bias, 0)


