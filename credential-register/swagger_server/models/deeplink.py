# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Deeplink(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, usecase: List[str]=None):  # noqa: E501
        """Deeplink - a model defined in Swagger

        :param usecase: The usecase of this Deeplink.  # noqa: E501
        :type usecase: List[str]
        """
        self.swagger_types = {
            'usecase': List[str]
        }

        self.attribute_map = {
            'usecase': 'usecase'
        }
        self._usecase = usecase

    @classmethod
    def from_dict(cls, dikt) -> 'Deeplink':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The deeplink of this Deeplink.  # noqa: E501
        :rtype: Deeplink
        """
        return util.deserialize_model(dikt, cls)

    @property
    def usecase(self) -> List[str]:
        """Gets the usecase of this Deeplink.

        addbeneficiary,accountclosurestatus_followup,travel_followup,fundtransferstatusinquiry,transferfunds  # noqa: E501

        :return: The usecase of this Deeplink.
        :rtype: List[str]
        """
        return self._usecase

    @usecase.setter
    def usecase(self, usecase: List[str]):
        """Sets the usecase of this Deeplink.

        addbeneficiary,accountclosurestatus_followup,travel_followup,fundtransferstatusinquiry,transferfunds  # noqa: E501

        :param usecase: The usecase of this Deeplink.
        :type usecase: List[str]
        """

        self._usecase = usecase