import torch
import csv
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def write_csv(file_name, data):
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)
            

def read_csv(data_file_path):
    data = []
    with open(data_file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        data = np.asarray(data)
    return data


def imshow(images, labels, full_path):              
    plt.figure(figsize=(5,5))
        
    temp = images[0,:,:,:].numpy()
    temp = np.transpose(temp, [1,2,0])
    plt.imshow(temp)
    plt.title(labels[0])
    print('file_name:', full_path[0])


    
def assemble_labels(step, y_true, y_pred, label, out):
    if(step==0):
        y_true = label
        y_pred = out
    else:
#         y_true = np.concatenate((y_true, label), 0)
#         y_pred = np.concatenate((y_pred, out), 0)
        y_true = torch.cat((y_true, label), 0)
        y_pred = torch.cat((y_pred, out))
    return y_true, y_pred