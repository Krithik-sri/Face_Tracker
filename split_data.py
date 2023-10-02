import splitfolders
input_folder = 'data/'

splitfolders.ratio(input_folder,output='data',seed=42,ratio=(0.7,0.2,0.1),group_prefix=None)