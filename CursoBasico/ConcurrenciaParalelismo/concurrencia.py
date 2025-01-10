import threading
import time

#Función que simula el procesamiento de una solicitud
def process_request(request_id):
    print(f"Processing request {request_id}")
    time.sleep(3)
    print(f'Request {request_id} completed')

threads = []

for i in range(3):
    thread = threading.Thread(target=process_request, args=(i,)) #Los parametros de args van en una tupla
    threads.append(thread)
    thread.start()

#Esperar a que todos los hilos terminen
for th in threads:
    th.join()