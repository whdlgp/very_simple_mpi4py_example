# Simply display current proc's information
from mpi4py import MPI

comm = MPI.COMM_WORLD
print("%d of %d" % (comm.Get_rank(), comm.Get_size()))

#MPI Init is called when mpi4py is imported
#MPI Finalize is called when the script exits