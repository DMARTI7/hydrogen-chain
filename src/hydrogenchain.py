"""Function for building a hydrogen chain."""

def create_diatomic_molecule_geometry(num_of_hatoms, bond_length):
    """Create a molecular geometry for a hydrogen chain, along the x-axis

    Args:
        num_of_atoms (int): number of atoms in the chain
        bond_length (float): bond distance.

    Returns:
        dict: a dictionary containing the coordinates of the hydrogen atoms.
    """
   
    xyz_coords = []
    for i in range(num_of_hatoms):
        xyz_coords.append({'species': 'H', 'x': i * bond_length, 'y': 0, 'z': 0})
       
    geometry = {'sites': xyz_coords}
   
    return geometry
