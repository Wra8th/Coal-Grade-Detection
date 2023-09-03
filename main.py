import splitfolders

input_folder = 'coal/'

splitfolders.ratio(input_folder, output = "coal2", seed=42, ratio=(.7,.2,.1), group_prefix =None)