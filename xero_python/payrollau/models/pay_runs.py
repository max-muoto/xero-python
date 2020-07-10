# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.2.7
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayRuns(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"pay_runs": "list[PayRun]"}

    attribute_map = {"pay_runs": "PayRuns"}

    def __init__(self, pay_runs=None):  # noqa: E501
        """PayRuns - a model defined in OpenAPI"""  # noqa: E501

        self._pay_runs = None
        self.discriminator = None

        if pay_runs is not None:
            self.pay_runs = pay_runs

    @property
    def pay_runs(self):
        """Gets the pay_runs of this PayRuns.  # noqa: E501


        :return: The pay_runs of this PayRuns.  # noqa: E501
        :rtype: list[PayRun]
        """
        return self._pay_runs

    @pay_runs.setter
    def pay_runs(self, pay_runs):
        """Sets the pay_runs of this PayRuns.


        :param pay_runs: The pay_runs of this PayRuns.  # noqa: E501
        :type: list[PayRun]
        """

        self._pay_runs = pay_runs
