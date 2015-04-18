from molecules_list import *

file = open('sdf_list.sdf', 'tr')

lm = extract_molecules_list_from_sdf(file, 'Source')
file.close()

print('lm dict:\n', lm.mol_list[-1].fields_dict)
