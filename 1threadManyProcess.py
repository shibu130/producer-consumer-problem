import multiprocessing
from threading import Thread

from time import perf_counter,sleep
def read_thread(q):
    with open("test.txt","r") as  filep:
        for i in filep:
                # sleep(5)
                print("pushing {} item into queue".format(i.strip()))
                q.put(i.strip())
        else:
            #to stop the process when the filepointer reaches end of file
            q.put(None)
            # sleep(1)
            q.put(None)
            q.put(None)


def consume(q):
    while(True):
        try:
            item=q.get(block=False)
            if(item==None):
                print(multiprocessing.current_process().name+" exited")
                break

            

            print("process "+multiprocessing.current_process().name+" consumed "+item)
        except Exception:
                         pass
                        # print("empty")
               


if __name__ == "__main__":
    qu=multiprocessing.Queue(maxsize=5)
    P=Thread(name='p',target=read_thread,args=(qu,))
    P.start()
 
    
    start=perf_counter()
    
    C1=multiprocessing.Process(name='c1',target=consume,args=(qu,))
    C1.start()

    C2=multiprocessing.Process(name='c2',target=consume,args=(qu,))
    C2.start()

    C3=multiprocessing.Process(name='c3',target=consume,args=(qu,))
    C3.start()


    P.join()
    C1.join()
    C2.join()
    C3.join()

    end=perf_counter()

    print(end-start)
    
