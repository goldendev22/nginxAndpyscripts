#-------------------Multi process -------------------------------

# import time
# from multiprocessing import Process
#
#
# def run_process(pid):
#     for j in range(100):
#         print("{}".format(pid))
#         time.sleep(0)
#
# if __name__ == '__main__':
#     processes = []
#     for num in range(20):
#         p = Process(target=run_process, args=(num,))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#         p.close()
#
#     # only get here once all processes have finished.
#     print('finished!')


#----------------------Read Json Data and Parse -----------------------------

import json


def parseJson(jsonData):
    product_name = jsonData['product_info']['name']
    product_image = jsonData['product_info']['image']
    product_sku = jsonData['product_info']['sku']
    product_msrp = jsonData['product_info']['msrp']
    store_ids = []
    prices = []
    # pickups = []
    quans = []

    for index, store in enumerate(jsonData['products']):
        # print('{0} : store_id: {1}, price: {2}, pickup: {3}, quan: {4}'.format(index, store['store_id'], store['price'],
        #                                                                        store['pickup'], store['quan']))

        if store['pickup'] == "1":
            print('{0} : store_id: {1}, price: {2}, pickup: {3}, quan: {4}'.format(index, store['store_id'],
                                                                                   store['price'], store['pickup'],
                                                                                   store['quan']))
            store_ids.append(store['store_id'])
            prices.append(store['price'])
            # pickups.append(store['pickup'])
            quans.append(store['quan'])
            # stores.append([store['store_id'], store['price'], store['pickup'], store['quan']])
            if len(store_ids)==10:
                break

    store_data = [product_name, product_image, product_sku, product_msrp, store_ids, prices, quans]
    return store_data

with open('D:\Apollo\Python\json scrapping\jsonviewer.json') as json_data:
    d = json.loads(json_data.read())
    json_data.close()
    print(d)
    parseJson(d)
