mol_gl, canv_gl = (0, 0)
dict_of_aroma_bonds, type_bond_gl = ({}, 0)
three_valencies = set()
#from aroma import*

def for_circle(x, y, radius):
    return [x-radius, y-radius, x+radius, y+radius]

def into_center(scale, center):
    global mol_gl
    summa, num, x_y_0 = ([0, 0], [0, 0], [0, 0])
    for atom in mol_gl.atom_block:
        for i in 0, 1:
            summa[i] += atom[i]
            num[i] += 1
    for i in 0, 1:
        x_y_0[i] = summa[i] / num[i]
    for num_atom in range(len(mol_gl.atom_block)):
        atom = mol_gl.atom_block[num_atom]
        for i in 0, 1:
            atom[i] -= x_y_0[i]
            atom[i] *= scale
            atom[i] += center
            
'''def callFriends(vertex):
    three_valencies.add(vertex)
    for friend in dict_of_aroma_bonds[vertex]:
        if friend not in three_valencies:
            weight=dict_of_aroma_bonds[vertex][friend]
            start=vertex
            finish=friend
            if start not in spTree:
                spTree[start] = {finish:weight}
            else:
                spTree[start][finish] = weight
            if finish not in spTree:
                spTree[finish] = {start:weight}
            else:
                spTree[finish][start] = weight
            callFriends(friend)
'''
'''def dfs_aroma(atom):
    
    pass

def draw_aroma_bonds():
    #print("draw_aroma_bonds works")
    pass
'''
def double_line(bond, ro=1):
    import math
    dist = 2
    double_bond = [[0 for i in range(4)] for j in [0, 1]]
    dist *= ro
    k_znam = bond[2] - bond[0]
    if k_znam == 0:
        almost_x_y = [dist, 0]
    else:
        k = (bond[3] - bond[1]) / k_znam
        if k == 0:
            almost_x_y = [0, dist]
        else:
            sign_k = k / abs(k)
            k *= k
            almost_x_y = [dist/math.sqrt(1/k + 1), -dist/math.sqrt(k + 1)*sign_k]
    for bond_i in [0, 1]:
        for coord_i in [0, 1, 2, 3]:
            double_bond[bond_i][coord_i] = (2*bond_i - 1) * almost_x_y[coord_i%2] + bond[coord_i]
    for i in [0, 1]:
        canv_gl.create_line(*double_bond[i],width=2,tag=str(bond[4]))
 
def draw_bond(num_atom1, num_atom2, type_bond):
    ro = 3
    atom1 = mol_gl.atom_block[int(num_atom1)-1][:2]
    atom2 = mol_gl.atom_block[int(num_atom2)-1][:2]
    bond = []
    bond.extend(atom1)
    bond.extend(atom2)
    bond.append(type_bond)
    if type_bond == 1:
        canv_gl.create_line(*bond[:4],width=2,tag=str(type_bond))
    elif type_bond == 2:
        double_line(bond)
    elif type_bond == 3:
        double_line(bond, ro=ro)
        canv_gl.create_line(*bond[:4],width=2,tag=str(type_bond))
    else:
        canv_gl.create_line(*bond[:4],width=2,tag=str(type_bond), fill="red")
'''def printAsListOfArcs(tree):
    for start in tree:
        for finish in tree[start]:
            print(start, finish, tree[start][finish])'''
'''def jk():
    dict_of_aroma_bonds = into_aroma_dict()
    three_valencies = set()
    spTree = {}
    numOfComp = 0
    for key in dict_of_aroma_bonds:
        if key in called:
            continue
        else:
            callFriends(key)
            printAsListOfArcs(spTree)
            spTree = {}
            print()
            numOfComp += 1
        

    print("Number of components:",numOfComp)
'''
def draw_mol(mol, canv, scale=70, center=400):
    global mol_gl, canv_gl, dict_of_aroma_bonds, type_bond_gl, three_valencies
    dict_of_aroma_bonds, type_bond_gl = ({}, 0)
    three_valencies = set()
    import copy
    mol_gl = copy.deepcopy(mol)
    canv_gl = canv

    into_center(scale, center)
    for num_bond in range(len(mol_gl.bond_block)):
        bond = mol_gl.bond_block[num_bond][:3]
        if bond[2] == 4:
            bond[2] = 1
            into_aroma_dict(*bond)
        else:
            draw_bond(*bond)
    create_sp_trees()
    for atom in dict_of_aroma_bonds:
        for near_atom in dict_of_aroma_bonds[atom]:
            bond = [atom, near_atom, dict_of_aroma_bonds[atom][near_atom]]
            draw_bond(*bond)
    #print("dict_of_aroma_bonds:\n", dict_of_aroma_bonds)
    
    #print("dict_of_aroma_bonds:\n", dict_of_aroma_bonds)
    '''if dict_of_aroma_bonds != []:
        for atom in dict_of_aroma_bonds:
            dfs_aroma(atom)
            draw_aroma_bonds()
    '''   
    for atom in mol_gl.atom_block:
        x_y = atom[:2]
        x_y_r = for_circle(*x_y, radius=7)
        canv_gl.create_oval(*x_y_r, fill="lightyellow", outline="lightyellow")
        canv_gl.create_text(*x_y, text=atom[3],font="Verdana 12",fill="red")
    #обнуление глобальных переменных
    #mol_gl, canv_gl = (0, 0)
    #three_valencies = set()

def into_aroma_dict(start, finish, weight):
    global dict_of_aroma_bonds
    if start not in dict_of_aroma_bonds:
        dict_of_aroma_bonds[start] = {finish:weight}
    else:
        dict_of_aroma_bonds[start][finish] = weight
    if finish not in dict_of_aroma_bonds:
        dict_of_aroma_bonds[finish] = {start:weight}
    else:
        dict_of_aroma_bonds[finish][start] = weight
    #return dict_of_aroma_bonds

def create_sp_trees():
    global three_valencies, type_bond_gl, dict_of_aroma_bonds #, spTree
    '''print("three_valencies:", three_valencies, "type_bond_gl:",\
           type_bond_gl, "dict_of_aroma_bonds:", \
          dict_of_aroma_bonds, "spTree:", spTree, sep='\n')'''
    #num_of_spanning_trees = 0
    for atom in dict_of_aroma_bonds:
        if atom not in three_valencies:
            type_bond_gl = 0
            #spTree.append([])
            #print("spTree:\n", spTree)
            last_atom = dfs_aroma(atom) #, num_of_spanning_trees)
            type_bond_l = 2 - type_bond_gl % 2
            '''if type_bond_l == 2:
                print("Not aromatic")
                #FIX_ME : it's neсessary to exit with error!!!
            elif type_bond_l == 1:
                dict_of_aroma_bonds[atom][last_atom] = type_bond_l
                dict_of_aroma_bonds[last_atom][atom] = type_bond_l
            '''
            '''print("last_atom:\n", last_atom)
            print("dict_of_aroma_bonds: \n", dict_of_aroma_bonds)
            print("spTree:", spTree, "num_of_spanning_trees:", \
                  num_of_spanning_trees, sep='\n')'''
            #num_of_spanning_trees += 1
def dfs_aroma(atom): #, num_of_spanning_trees):
    global three_valencies, type_bond_gl, dict_of_aroma_bonds
    three_valencies.add(atom)
    '''print("call dfs_aroma()")
    print("atom:", atom, "three_valencies:", three_valencies, sep='\n')'''
    #spTree[num_of_spanning_trees].append(atom)
    #print(spTree)
    for near_atom in dict_of_aroma_bonds[atom]:
        '''print("dict_of_aroma_bonds[atom]:", dict_of_aroma_bonds[atom],\
              "near_atom:", near_atom, sep='\n')
        print(near_atom not in three_valencies)'''
        last_atom = near_atom
        if near_atom not in three_valencies:
            type_bond_l = 2 - type_bond_gl % 2
            #print("type_bond_gl, type_bond_l: ", type_bond_gl, type_bond_l)
            dict_of_aroma_bonds[atom][near_atom] = type_bond_l
            dict_of_aroma_bonds[near_atom][atom] = type_bond_l
            #why twice add, when list?
            #print("dict_of_aroma_bonds: \n", dict_of_aroma_bonds)
            type_bond_gl += 1
            last_atom = dfs_aroma(near_atom) #, num_of_spanning_trees)
    return last_atom 
    '''if len(three_valencies) == len(dict_of_aroma_bonds):
        for near_atom in dict_of_aroma_bonds[atom]:
            if len(dict_of_aroma_bonds[atom][near_atom]) == 1:
                print("fail")
                break
        cheque_fail.append(dict_of_aroma_bonds[atom][near_atom][1])
    if cheque_fail == [1, 1, 1]:
        print'''
        


    
    
