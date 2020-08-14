# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.12
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Payslips(BaseModel):
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
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_slips": "list[Payslip]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_slips": "paySlips",
    }

    def __init__(self, pagination=None, problem=None, pay_slips=None):  # noqa: E501
        """Payslips - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._pay_slips = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_slips is not None:
            self.pay_slips = pay_slips

    @property
    def pagination(self):
        """Gets the pagination of this Payslips.  # noqa: E501


        :return: The pagination of this Payslips.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this Payslips.


        :param pagination: The pagination of this Payslips.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this Payslips.  # noqa: E501


        :return: The problem of this Payslips.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this Payslips.


        :param problem: The problem of this Payslips.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def pay_slips(self):
        """Gets the pay_slips of this Payslips.  # noqa: E501


        :return: The pay_slips of this Payslips.  # noqa: E501
        :rtype: list[Payslip]
        """
        return self._pay_slips

    @pay_slips.setter
    def pay_slips(self, pay_slips):
        """Sets the pay_slips of this Payslips.


        :param pay_slips: The pay_slips of this Payslips.  # noqa: E501
        :type: list[Payslip]
        """

        self._pay_slips = pay_slips
