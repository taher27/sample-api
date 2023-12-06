# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.err_err import ErrErr  # noqa: F401,E501
from swagger_server import util


class Err(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, err: ErrErr=None):  # noqa: E501
        """Err - a model defined in Swagger

        :param err: The err of this Err.  # noqa: E501
        :type err: ErrErr
        """
        self.swagger_types = {
            'err': ErrErr
        }

        self.attribute_map = {
            'err': 'err'
        }
        self._err = err

    @classmethod
    def from_dict(cls, dikt) -> 'Err':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The err of this Err.  # noqa: E501
        :rtype: Err
        """
        return util.deserialize_model(dikt, cls)

    @property
    def err(self) -> ErrErr:
        """Gets the err of this Err.


        :return: The err of this Err.
        :rtype: ErrErr
        """
        return self._err

    @err.setter
    def err(self, err: ErrErr):
        """Sets the err of this Err.


        :param err: The err of this Err.
        :type err: ErrErr
        """

        self._err = err