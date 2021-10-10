from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.core.cache import caches
import requests
from django.views.decorators.csrf import csrf_exempt
import time
import random
import threading
from threading import Thread
import json
import queue

foods = [{
"id": 1,
"name": "pizza",
"preparation-time": 20 ,
"complexity": 2 ,
"cooking-apparatus": "oven"
},
 {
"id": 2,
"name": "salad",
"preparation-time": 10 ,
"complexity": 1 ,
"cooking-apparatus": "null"
},
{
"id": 3,
"name": "zeama",
"preparation-time": 7 ,
"complexity": 1 ,
"cooking-apparatus": "stove"
},
{
"id": 4,
"name": "Scallop Sashimi with Meyer Lemon Confit",
"preparation-time": 32 ,
"complexity": 3 ,
"cooking-apparatus": "null"
},
{
"id": 5,
"name": "Island Duck with Mulberry Mustard",
"preparation-time": 35 ,
"complexity": 3 ,
"cooking-apparatus": "oven"
},
{
"id": 6,
"name": "Waffles",
"preparation-time": 10 ,
"complexity": 1 ,
"cooking-apparatus": "stove"
},
{
"id": 7,
"name": "Aubergine",
"preparation-time": 20 ,
"complexity": 2 ,
"cooking-apparatus": "null"
},
{
"id": 8,
"name": "Lasagna",
"preparation-time": 30 ,
"complexity": 2 ,
"cooking-apparatus": "oven"
},
{
"id": 9,
"name": "Burger",
"preparation-time": 15 ,
"complexity": 1 ,
"cooking-apparatus": "oven"
},
{
"id": 10,
"name": "Gyros",
"preparation-time": 15 ,
"complexity": 1 ,
"cooking-apparatus": "null"
}]

# global exitFlag
# global waiter_semaphore
# waiter_semaphore = 0
# global waiters
# waiters = []

# class myTable (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print ("Generating order at " + self.name)
#         process_data_by_table(self.name, self.q)
#         print (self.name + " gets the order")
#
# def process_data_by_table(threadName, q):
#     print("     Enter function process_data_by_table")
#     # print('!!!!!!!!!!!!!!!!')
#     generate_order("http://127.0.0.2:8000/kitchen/")
#     call_waiter(threadName)

        # threadID += 1

    # call waiter
    # get order

# def call_waiter(threadName):
#     global waiter_semaphore
#     global waiters
#     print('THREADNAME = ', threadName)
#     if (waiter_semaphore < 5):
#         waiter_semaphore +=1
#         print("Number of waiters busy: " + str(waiter_semaphore))
#         thread_waiter = myWaiter(threadName)
#         # time.sleep(0.5)
#         thread_waiter.start()
#         print('.run()!!!!!!!!!!!!!!!!!!!!!!')
#         thread_waiter.run(threadName)
#         waiters.append(thread_waiter)
#         waiter_semaphore -= 1
#     else:
#         time.sleep(1)
#         call_waiter(threadName)

    # exitFlag = 1 #???????
    # while not exitFlag:
    #     queueLock.acquire()
    #     if (not workQueue.empty()):
    #         data = q.get()
    #         queueLock.release()
    #         print ("%s processing %s" % (threadName, data))
    #     else:
    #         queueLock.release()
    #         time.sleep(1)


# class myWaiter(threading.Thread):
#     def __init__(self, threadName):
#         threading.Thread.__init__(self)
#         # self.threadID = threadID
#         # self.name = name
#         # self.q = q
#         self.threadName = threadName
#     def run(self, threadName):
#         # print ("Picking order by " + self.name)
#         # process_data_by_waiter(self.name, self.q)
#         time.sleep(2)
#         print ("Order of " + threadName + " was sent to the Kitchen")


#
# def table_status(request):
#     table_list = []
#     for i in range (1, 11):
#         table_list.append("Table " + str(i))
#
#     waiter_list = []
#     for i in range (1, 6):
#         waiter_list.append("Waiter " + str(i))
#
#     threads = []
#     waiters = []
#     # nameList = ["One", "Two", "Three", "Four", "Five"]
#     queueLock = threading.Lock()
#     workQueue = queue.Queue(10)
#     threadID = 1
#
#     # Create new threads
#     # while (True):
#     for tName in table_list:
#        thread = myTable(threadID, tName, workQueue)
#        # time.sleep(0.5)
#        thread.start()
#        threads.append(thread)
#        threadID += 1
#
#     # Fill the queue
#     queueLock.acquire()
#     # for word in nameList:
#     #    workQueue.put(word)
#     queueLock.release()
#
#     # Wait for queue to empty
#     while not workQueue.empty():
#        pass
#
#     # Notify threads it's time to exit
#     # exitFlag = 1
#
#     # Wait for all threads to complete
#     for t in threads:
#        t.join()
#     print ("Exiting Main Thread")


    # table_list = []

    # threads = []
    # global variables
    # global table_number
    # table_number = 5
    # waiters = table_number // 2
    #
    # dict_key = ['thread%s' % variable for variable in range(table_number)]
    # dict_value = [1 for x in range(5)]
    # variables = dict(zip(dict_key, dict_value))
    # check_status()
    # for table in range(table_number):
        # table_list.append("Table " + str(table + 1))

        # thread = Thread()
        # thread.start()
        # threads.append(thread)
        # print(threads)
        # check_status(threads[table])
    # print(table_list)
    # print('THREADS:', thread0, thread1, thread2, thread3, thread4)
    # return HttpResponse(threads, waiters)


# def check_status():
#     random_time = random.randint(1, 8)
#     for table in range(table_number):
#         if variables["thread%s" % str(table)] == 1:
#             time.sleep(random_time)
#             print('Table %s' % table, 'is now occupied!')
#     return generate_order('http://127.0.0.1:8000/dinning/orders/')



# def generate_order(request):
#     print("     Entering function generate_order")
#     items = []
#     random_counter = random.randint(1, 10)
#     for i in range(random_counter):
#         random_id = random.randint(1, 10) #see in json file Foods
#         items.append(random_id)
#         items.append(' ')
#     order_priority = random.randint(1, 5)
#     max_wait = random.randint(15, 25)
#     time.sleep(max_wait)

    #
    #
    # return HttpResponse(items)

global number_of_tables
global number_of_waiters
global waiter_semaphore
global table_name
global order_id
global table_queue

waiter_semaphore = 0
number_of_tables = 10
number_of_waiters = 5
order_id = 0
table_queue = []

lock = threading.Lock()


def table(table_name, status, number):
    order = ""
    print(table_name + " is generating an order")
    order = generate_order()
    call_waiter(table_name, order)
    table_queue[number] = 0
    print(table_name + " is free now!!!")

def generate_order():
    global order_id

    # print("     Entering function generate_order")
    items = []

    id = order_id
    lock.acquire()
    order_id += 1
    lock.release()
    random_counter = random.randint(1, 11)
    max_wait = 0
    order_priority = '0'

    for dish in range(random_counter):
        random_id = random.randint(1, 10) #see in json file Foods
        items.append(random_id)
        if max_wait < foods[int(random_id - 1)]["preparation-time"]:
            max_wait = foods[int(random_id - 1)]["preparation-time"]
    if max_wait == 35:
        order_priority = '5'
    elif max_wait == 32:
        order_priority = '4'
    elif max_wait == 30:
        order_priority = '3'
    elif max_wait == 20:
        order_priority = '2'
    else:
        order_priority = '1'


    max_wait *= 1.3



        # items.append(' ')

    # order_priority = random.randint(1, 5)
    # max_wait = random.randint(15, 25)
    # time.sleep(max_wait-2)
    # print(items, max_wait, order_priority, order_id, 'ITEMS + MAX WAIT + ORDER PR + ORDER ID')

    print("Order of " + table_name + " is ready")

    # return ('''
    # {{
    # "id": {},
    # "items": {},
    # "priority": {},
    # "max_wait": {}
    # }}'''.format(order_id, items, order_priority, max_wait - 2))
    order = {"id" : order_id, "items": items, "priority": order_priority, "max_wait": max_wait - 2}
    print(order)
    return order



def call_waiter(table_name, order):
    # global table_name
    global waiter_semaphore

    if waiter_semaphore < number_of_waiters:
        # lock.acquire()
        waiter_semaphore += 1
        print(str(waiter_semaphore) + " waiters are busy now")
        # lock.release()
        waiter_name = table_name + " waiter"
        thread_waiter = threading.Thread(target=waiter, name=waiter_name, args=('http://127.0.0.2:8000/kitchen/', order,))
        thread_waiter.start()
    else:
        time.sleep(1)
        call_waiter(table_name, order)


def waiter(request, order):
    global waiter_semaphore

    time.sleep(2)
    # lock.acquire()
    waiter_semaphore -= 1
    # lock.release()
    # print("Order of " + table_name + " is ready") here will be a request
    headers = {'Content-Type' : 'application/json'}
    # # lock.acquire()
    response = requests.post('http://127.0.0.2:8000/kitchen/', data=json.dumps(order), headers = headers)
    print(response.content)
    time.sleep(10)
    # if response.status_code == 200:
    #     return HttpResponse(response.content, content_type = 'application/json')
    # else:
    #     print("Express dostavka")
    # return HttpResponse({'a': '2'})
    # lock.release()
    # print(response.status_code)
    return HttpResponse(order)

def main(request):
    global table_name
    global table_queue

    for i in range(0, number_of_tables):
        table_queue.append(0)

    # while True:
    #     time.sleep(1)
    for i in range (0, number_of_tables):
        if (table_queue[i] == 0):
            table_queue[i] = 1
            status = 1
            table_name = "Table " + str(i+1)
            thread_table = threading.Thread(target=table, name=table_name, args=(table_name, 1, i))
            thread_table.start()
    return HttpResponse("Ready!!!!!!!!!!!")

# def index(request):
#     x = requests.get('http://127.0.0.2:8000/kitchen/')
#     return HttpResponse(x)
