# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TransferRecurringAddRequestRecurringOptionsFrequencyDuration(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, until_stop: str=None, until_date: float=None, number_of_transfers: float=None):  # noqa: E501
        """TransferRecurringAddRequestRecurringOptionsFrequencyDuration - a model defined in Swagger

        :param until_stop: The until_stop of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.  # noqa: E501
        :type until_stop: str
        :param until_date: The until_date of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.  # noqa: E501
        :type until_date: float
        :param number_of_transfers: The number_of_transfers of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.  # noqa: E501
        :type number_of_transfers: float
        """
        self.swagger_types = {
            'until_stop': str,
            'until_date': float,
            'number_of_transfers': float
        }

        self.attribute_map = {
            'until_stop': 'untilStop',
            'until_date': 'untilDate',
            'number_of_transfers': 'numberOfTransfers'
        }
        self._until_stop = until_stop
        self._until_date = until_date
        self._number_of_transfers = number_of_transfers

    @classmethod
    def from_dict(cls, dikt) -> 'TransferRecurringAddRequestRecurringOptionsFrequencyDuration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The transferRecurringAddRequest_recurringOptions_frequency_duration of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.  # noqa: E501
        :rtype: TransferRecurringAddRequestRecurringOptionsFrequencyDuration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def until_stop(self) -> str:
        """Gets the until_stop of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.


        :return: The until_stop of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.
        :rtype: str
        """
        return self._until_stop

    @until_stop.setter
    def until_stop(self, until_stop: str):
        """Sets the until_stop of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.


        :param until_stop: The until_stop of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.
        :type until_stop: str
        """

        self._until_stop = until_stop

    @property
    def until_date(self) -> float:
        """Gets the until_date of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.


        :return: The until_date of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.
        :rtype: float
        """
        return self._until_date

    @until_date.setter
    def until_date(self, until_date: float):
        """Sets the until_date of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.


        :param until_date: The until_date of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.
        :type until_date: float
        """

        self._until_date = until_date

    @property
    def number_of_transfers(self) -> float:
        """Gets the number_of_transfers of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.


        :return: The number_of_transfers of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.
        :rtype: float
        """
        return self._number_of_transfers

    @number_of_transfers.setter
    def number_of_transfers(self, number_of_transfers: float):
        """Sets the number_of_transfers of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.


        :param number_of_transfers: The number_of_transfers of this TransferRecurringAddRequestRecurringOptionsFrequencyDuration.
        :type number_of_transfers: float
        """

        self._number_of_transfers = number_of_transfers