from queries import *
from jsonifier import *


def merge_tables( table1 = '',table2 = '' ):
	if table1 and table2:
		use( table1 )
	else:
		print("  Inadequate tables to merge.")
		return
	f	=	op()
	data	=	f.readlines()
	f.close()
	use(table2)
	f2	=	op()
	data2	=	f2.readlines()
	f2.seek(0,2)
	f2.writelines(data[1:])
	f2.close()

	use(table1)
	f1	=	op(append=True)
	f1.writelines(data2[1:])
	f1.close()

	print(" Data merge successful!")

