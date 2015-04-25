from molecules_list import *

file = open('sdf_list.sdf', 'tr')

lm = extract_molecules_list_from_sdf(file, 'Source')
file.close()

print('lm dict:\n', lm.mol_list[0].fields_dict)
# print('--------\n', lm.mol_list[0].bond_block)
# print('--------\n', lm.mol_list[0].atom_block)