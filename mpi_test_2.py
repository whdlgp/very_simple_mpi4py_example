#Test send and recv of MPI
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    msg = 'hello, world'
    comm.send(msg, dest=1)
elif rank == 1:
    s = comm.recv()
    print("rank %d: %s" % (rank, s))

#MPI Init is called when mpi4py is imported
#MPI Finalize is called when the script exits