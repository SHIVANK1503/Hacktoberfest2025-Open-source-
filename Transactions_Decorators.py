#!/bin/python3

import math
import os
import random
import re
import sys


def filter_transactions(threshold=50):
    def decor(func):
        def wrapper(transactions):
            transactions = [i for i in transactions if i[1] >= threshold or i[1] < 0]
            return func(transactions)
        return wrapper
    return decor


def combine_transactions(f):
    def wrapper(transactions):
        d = {}
        for i in transactions:
            if i[0] not in d:
                d[i[0]] = i[1]
            else:
                d[i[0]] += i[1]
        transactions = [(k, v) for k, v in d.items()]
        return f(transactions)
    return wrapper


def sort_transactions(f):
    def wrapper(transactions):
        transactions = list(sorted(transactions, key=lambda x: x[1], reverse=True))
        return f(transactions)
    return wrapper

# Driver code
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())
    transactions = []
    for i in range(n):
        transaction = input().split(' ')
        transactions.append((transaction[0], int(transaction[1])))
    
    
    @filter_transactions(threshold=50)
    @combine_transactions
    @sort_transactions    
    def display_total_transactions(transactions):
        for person, total_amount in transactions:
            amount_str=f"${total_amount}" if total_amount>=0 else f"-${total_amount*-1}"
            fptr.write(f"{person}: {amount_str}\n")
    display_total_transactions(transactions)
    fptr.close()


