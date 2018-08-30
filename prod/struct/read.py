i_file = "unitcell.xyz"
o_file = "unitcell_ase.xyz"

with open(i_file,"rb") as f:
	content = f.readlines()

content = [x.strip() for x in content]
