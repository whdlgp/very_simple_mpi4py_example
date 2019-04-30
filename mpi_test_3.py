#Test send and recv of MPI
#send massage to next prcess, recv massage from previouse process
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

s = range(1000)
src = rank - 1 if rank != 0 else size - 1
dst = rank + 1 if rank != size - 1 else 0

if rank % 2 == 0:
    comm.send(s, dest=dst)
    m = comm.recv(source=src)
else:
    m = comm.recv(source=src)
    comm.send(s, dest=dst)
