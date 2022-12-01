# threads run on a single cpu
# processes run on separate cpu
import os
print( os.cpu_count() ) # 16
# NB each processor can run many threads (a pool of threads)