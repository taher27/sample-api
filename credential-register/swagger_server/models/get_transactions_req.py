# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_transactions_req_category import GetTransactionsReqCategory  # noqa: F401,E501
from swagger_server.models.get_transactions_req_sort import GetTransactionsReqSort  # noqa: F401,E501
from swagger_server.models.get_transactions_req_transaction_amount import GetTransactionsReqTransactionAmount  # noqa: F401,E501
from swagger_server import util


class GetTransactionsReq(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, customer_id: str=None, account_number: List[str]=None, num_of_transactions: float=None, status: str=None, start_date: date=None, end_date: date=None, sort: GetTransactionsReqSort=None, transaction_amount: GetTransactionsReqTransactionAmount=None, category: List[GetTransactionsReqCategory]=None, debit_or_credit: str=None):  # noqa: E501
        """GetTransactionsReq - a model defined in Swagger

        :param customer_id: The customer_id of this GetTransactionsReq.  # noqa: E501
        :type customer_id: str
        :param account_number: The account_number of this GetTransactionsReq.  # noqa: E501
        :type account_number: List[str]
        :param num_of_transactions: The num_of_transactions of this GetTransactionsReq.  # noqa: E501
        :type num_of_transactions: float
        :param status: The status of this GetTransactionsReq.  # noqa: E501
        :type status: str
        :param start_date: The start_date of this GetTransactionsReq.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this GetTransactionsReq.  # noqa: E501
        :type end_date: date
        :param sort: The sort of this GetTransactionsReq.  # noqa: E501
        :type sort: GetTransactionsReqSort
        :param transaction_amount: The transaction_amount of this GetTransactionsReq.  # noqa: E501
        :type transaction_amount: GetTransactionsReqTransactionAmount
        :param category: The category of this GetTransactionsReq.  # noqa: E501
        :type category: List[GetTransactionsReqCategory]
        :param debit_or_credit: The debit_or_credit of this GetTransactionsReq.  # noqa: E501
        :type debit_or_credit: str
        """
        self.swagger_types = {
            'customer_id': str,
            'account_number': List[str],
            'num_of_transactions': float,
            'status': str,
            'start_date': date,
            'end_date': date,
            'sort': GetTransactionsReqSort,
            'transaction_amount': GetTransactionsReqTransactionAmount,
            'category': List[GetTransactionsReqCategory],
            'debit_or_credit': str
        }

        self.attribute_map = {
            'customer_id': 'customerId',
            'account_number': 'accountNumber',
            'num_of_transactions': 'numOfTransactions',
            'status': 'status',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'sort': 'sort',
            'transaction_amount': 'transactionAmount',
            'category': 'category',
            'debit_or_credit': 'debitOrCredit'
        }
        self._customer_id = customer_id
        self._account_number = account_number
        self._num_of_transactions = num_of_transactions
        self._status = status
        self._start_date = start_date
        self._end_date = end_date
        self._sort = sort
        self._transaction_amount = transaction_amount
        self._category = category
        self._debit_or_credit = debit_or_credit

    @classmethod
    def from_dict(cls, dikt) -> 'GetTransactionsReq':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetTransactionsReq of this GetTransactionsReq.  # noqa: E501
        :rtype: GetTransactionsReq
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_id(self) -> str:
        """Gets the customer_id of this GetTransactionsReq.


        :return: The customer_id of this GetTransactionsReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str):
        """Sets the customer_id of this GetTransactionsReq.


        :param customer_id: The customer_id of this GetTransactionsReq.
        :type customer_id: str
        """

        self._customer_id = customer_id

    @property
    def account_number(self) -> List[str]:
        """Gets the account_number of this GetTransactionsReq.


        :return: The account_number of this GetTransactionsReq.
        :rtype: List[str]
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number: List[str]):
        """Sets the account_number of this GetTransactionsReq.


        :param account_number: The account_number of this GetTransactionsReq.
        :type account_number: List[str]
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def num_of_transactions(self) -> float:
        """Gets the num_of_transactions of this GetTransactionsReq.


        :return: The num_of_transactions of this GetTransactionsReq.
        :rtype: float
        """
        return self._num_of_transactions

    @num_of_transactions.setter
    def num_of_transactions(self, num_of_transactions: float):
        """Sets the num_of_transactions of this GetTransactionsReq.


        :param num_of_transactions: The num_of_transactions of this GetTransactionsReq.
        :type num_of_transactions: float
        """

        self._num_of_transactions = num_of_transactions

    @property
    def status(self) -> str:
        """Gets the status of this GetTransactionsReq.


        :return: The status of this GetTransactionsReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this GetTransactionsReq.


        :param status: The status of this GetTransactionsReq.
        :type status: str
        """

        self._status = status

    @property
    def start_date(self) -> date:
        """Gets the start_date of this GetTransactionsReq.


        :return: The start_date of this GetTransactionsReq.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this GetTransactionsReq.


        :param start_date: The start_date of this GetTransactionsReq.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this GetTransactionsReq.


        :return: The end_date of this GetTransactionsReq.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this GetTransactionsReq.


        :param end_date: The end_date of this GetTransactionsReq.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def sort(self) -> GetTransactionsReqSort:
        """Gets the sort of this GetTransactionsReq.


        :return: The sort of this GetTransactionsReq.
        :rtype: GetTransactionsReqSort
        """
        return self._sort

    @sort.setter
    def sort(self, sort: GetTransactionsReqSort):
        """Sets the sort of this GetTransactionsReq.


        :param sort: The sort of this GetTransactionsReq.
        :type sort: GetTransactionsReqSort
        """

        self._sort = sort

    @property
    def transaction_amount(self) -> GetTransactionsReqTransactionAmount:
        """Gets the transaction_amount of this GetTransactionsReq.


        :return: The transaction_amount of this GetTransactionsReq.
        :rtype: GetTransactionsReqTransactionAmount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount: GetTransactionsReqTransactionAmount):
        """Sets the transaction_amount of this GetTransactionsReq.


        :param transaction_amount: The transaction_amount of this GetTransactionsReq.
        :type transaction_amount: GetTransactionsReqTransactionAmount
        """

        self._transaction_amount = transaction_amount

    @property
    def category(self) -> List[GetTransactionsReqCategory]:
        """Gets the category of this GetTransactionsReq.


        :return: The category of this GetTransactionsReq.
        :rtype: List[GetTransactionsReqCategory]
        """
        return self._category

    @category.setter
    def category(self, category: List[GetTransactionsReqCategory]):
        """Sets the category of this GetTransactionsReq.


        :param category: The category of this GetTransactionsReq.
        :type category: List[GetTransactionsReqCategory]
        """

        self._category = category

    @property
    def debit_or_credit(self) -> str:
        """Gets the debit_or_credit of this GetTransactionsReq.


        :return: The debit_or_credit of this GetTransactionsReq.
        :rtype: str
        """
        return self._debit_or_credit

    @debit_or_credit.setter
    def debit_or_credit(self, debit_or_credit: str):
        """Sets the debit_or_credit of this GetTransactionsReq.


        :param debit_or_credit: The debit_or_credit of this GetTransactionsReq.
        :type debit_or_credit: str
        """

        self._debit_or_credit = debit_or_credit