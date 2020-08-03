# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.11
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeLeaves(BaseModel):
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
        "leave": "list[EmployeeLeave]",
    }

    attribute_map = {"pagination": "pagination", "problem": "problem", "leave": "leave"}

    def __init__(self, pagination=None, problem=None, leave=None):  # noqa: E501
        """EmployeeLeaves - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._leave = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave is not None:
            self.leave = leave

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeLeaves.  # noqa: E501


        :return: The pagination of this EmployeeLeaves.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeLeaves.


        :param pagination: The pagination of this EmployeeLeaves.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeeLeaves.  # noqa: E501


        :return: The problem of this EmployeeLeaves.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeLeaves.


        :param problem: The problem of this EmployeeLeaves.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def leave(self):
        """Gets the leave of this EmployeeLeaves.  # noqa: E501


        :return: The leave of this EmployeeLeaves.  # noqa: E501
        :rtype: list[EmployeeLeave]
        """
        return self._leave

    @leave.setter
    def leave(self, leave):
        """Sets the leave of this EmployeeLeaves.


        :param leave: The leave of this EmployeeLeaves.  # noqa: E501
        :type: list[EmployeeLeave]
        """

        self._leave = leave
