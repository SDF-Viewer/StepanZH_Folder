from molecule import *

class MoleculesList:
    """Список молекул
    """
    
    mol_list = []
    """Список экземпляров класса Molecule
    """
    name = ''

    def __init__(self, name):
        """Конструктор класса
        """
        self.name = name
    
    def append_molecule(self, molecule_copy):
        """Добавляет новый экземпляр класса Molecule в конец списка self.mol_list
        """
        self.mol_list.append(molecule_copy)
    

def extract_molecules_list_from_sdf(file, name = 'Source'):
    """Преобразует sdf в класс MoleculeList

    Возвращет экземпляр класса 'Cписок молекул' по sdf. В случае пустого/не sdf возвращает None.
    """
    file_as_string = file.read()
    molecules_count = file_as_string.count('$$$$')
    if molecules_count != 0:
        OutputClass = MoleculesList(name)
        string_list = file_as_string.split('\n$$$$\n', molecules_count-1)
        #print(string_list)
        #рассплитили на строчки с информацией об отдельной молекуле
        last_string = string_list[-1]
        f = last_string.find('$$$$')
        if f != -1:
            last_string = last_string[:f]
            string_list[-1] = last_string
        #в последней строчке может содержаться "$$$$"
        for molecule_string in string_list:
            molecule_copy = extract_molecule_by_string(molecule_string)
            #получаем экземпляр класса Molecule
            OutputClass.append_molecule(molecule_copy)
        return OutputClass
    else:
        return None

