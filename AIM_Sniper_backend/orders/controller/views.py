from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.repository.profile_repository_impl import ProfileRepositoryImpl
from account.service.account_service_impl import AccountServiceImpl
from orders.repository.orders_item_repository_impl import OrdersItemRepositoryImpl
from orders.service.orders_service_impl import OrdersServiceImpl
from redis_service.service.redis_service_impl import RedisServiceImpl
from product.repository.product_repository_impl import ProductRepositoryImpl

from datetime import datetime

class OrdersView(viewsets.ViewSet):
    ordersService = OrdersServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    productRepository = ProductRepositoryImpl.getInstance()
    profileRepository = ProfileRepositoryImpl.getInstance()
    ordersItemRepository = OrdersItemRepositoryImpl.getInstance()

    def createCartOrders(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')

            accountId = self.redisService.getValueByKey(userToken)
            if not accountId:
                raise ValueError('Invalid userToken')

            account = self.accountService.findAccountById(accountId)

            orderItemList = data.get('items')
            print(f"orderItemList: {orderItemList}")

            orderId = self.ordersService.createCartOrder(account, orderItemList)
            return Response(orderId, status=status.HTTP_200_OK)

        except Exception as e:
            print("주문 과정 중 문제 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def createProductOrders(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid userToken')

            account = self.accountService.findAccountById(accountId)
            productId = data.get('productId')
            product = self.productRepository.findByProductId(productId)
            productPrice = data.get('productPrice')
            quantity = 1

            orderItem = {"product": product,
                         "productPrice": productPrice,
                         "quantity": quantity}

            orderId = self.ordersService.createProductOrder(account, orderItem)
            return Response(orderId, status=status.HTTP_200_OK)

        except Exception as e:
            print("주문 과정 중 문제 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def checkOrderItemDuplication(self, request):
        userToken = request.data['payload']['userToken']
        productId = request.data['payload']['productId']

        accountId = self.redisService.getValueByKey(userToken)
        ordersList = self.ordersService.findAllByAccountId(accountId)
        ordersIdList = [orders.id for orders in ordersList]
        allOrdersItemList = [self.ordersItemRepository.findAllByOrdersId(ordersId) for ordersId in ordersIdList]
        isDuplicate = self.ordersItemRepository.checkDuplication(allOrdersItemList, productId)
        print(f"isDuplicate: {isDuplicate}")
        return Response(isDuplicate, status=status.HTTP_200_OK)