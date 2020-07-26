from multiprocessing import Queue


class QueueSet():
    __gindex = 0
    __pindex = 0
    __queues = []
    __quantity = 0

    def __init__(self, quantity=2):
        self.__quantity = quantity
        for q in range(self.__quantity):
            q = Queue()
            self.__queues.append(q)

    def get_data(self):
        if self.__gindex == self.__quantity:
            self.__gindex = 0

        #print("get index at this time: ", self.__gindex)
        obj = self.__queues[self.__gindex].get()
        #print("value got : ", obj)
        self.__gindex += 1
        return obj

    def put_data(self, obj):
        if self.__pindex == self.__quantity:
            self.__pindex = 0

        #print("put index at this time: ", self.__pindex)
        #print("value putting : ", obj)
        self.__queues[self.__pindex].put(obj)
        self.__pindex += 1

    # def get_queue_set(self):
    #     return self.__queues
    #
    #
    # def get_queue_set_size(self, queue_set):
    #     qssize = 0
    #
    #     print("&&&&&&&&&&&&&&&&&&&")
    #     for ind in queue_set:
    #         #size = cQ.qsize()
    #
    #         print(" it have elem",ind.qsize())
    #
    #     return qssize