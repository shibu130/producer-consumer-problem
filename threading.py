from threading import Thread,currentThread,current_thread,Lock
import threading
from multiprocessing import Process
import multiprocessing
from time import sleep
import concurrent.futures as cf
from queue import Queue
from random import randint
import os
import requests
from time import perf_counter
# multiprocessing.set_start_method('spawn')
#
qu=Queue(maxsize=5)



# lock=Lock()

def read_thread(q):
    with open("test.txt","r") as  filep:
        for i in filep:
            try:
                # sleep(5)
                print("pushing {} item into queue".format(i.strip()))
                q.put(i.strip())
            except Exception:
                            while(True):
                                        if(q.full==False):
                                            print("queue freeagain")
                                            break
        else:
            pass






def process_thread(q):
    while(True):
        # lock.acquire()
        try:
            # sleep(2)
            
            
            item=q.get(block=False)
            q.task_done()
            print("-------------------------")
            print(str(item)+" consumed by"+"thread "+threading.current_thread().name)
            # print("{} consumed".format(str(item)))
            print("-------------------------")
            sleep(1)
        except Exception:
                        if(producerThread.is_alive()==False):
                            print(threading.current_thread().name+" stopped")
                            break
        


# 1 producer and many consumer thread

if __name__ == "__main__":
    stop=True
    
    
    producerThread=Thread(name='pr',target=read_thread,args=(qu,))
    producerThread.start()


    array_of_threads=[]
   
    start=perf_counter()
    array=[Thread(name=str(i),target=process_thread,args=(qu,)) for i in range(3)]

    for i in array:
        i.start()



    for i in array:
        i.join()
  
    producerThread.join()

    end=perf_counter()

    print(end-start)
    # p1.join()
    # p2.join()
    # p3.join()


    # print(producerThread.is_alive)
    
    qu.join()
    
                                  
                                                        
                                                        
                                                        



