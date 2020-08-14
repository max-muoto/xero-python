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


class EmployeeStatutoryLeavesSummaries(BaseModel):
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
        "statutory_leaves": "list[EmployeeStatutoryLeaveSummary]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "statutory_leaves": "statutoryLeaves",
    }

    def __init__(
        self, pagination=None, problem=None, statutory_leaves=None
    ):  # noqa: E501
        """EmployeeStatutoryLeavesSummaries - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._statutory_leaves = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if statutory_leaves is not None:
            self.statutory_leaves = statutory_leaves

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeStatutoryLeavesSummaries.  # noqa: E501


        :return: The pagination of this EmployeeStatutoryLeavesSummaries.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeStatutoryLeavesSummaries.


        :param pagination: The pagination of this EmployeeStatutoryLeavesSummaries.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeeStatutoryLeavesSummaries.  # noqa: E501


        :return: The problem of this EmployeeStatutoryLeavesSummaries.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeStatutoryLeavesSummaries.


        :param problem: The problem of this EmployeeStatutoryLeavesSummaries.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def statutory_leaves(self):
        """Gets the statutory_leaves of this EmployeeStatutoryLeavesSummaries.  # noqa: E501


        :return: The statutory_leaves of this EmployeeStatutoryLeavesSummaries.  # noqa: E501
        :rtype: list[EmployeeStatutoryLeaveSummary]
        """
        return self._statutory_leaves

    @statutory_leaves.setter
    def statutory_leaves(self, statutory_leaves):
        """Sets the statutory_leaves of this EmployeeStatutoryLeavesSummaries.


        :param statutory_leaves: The statutory_leaves of this EmployeeStatutoryLeavesSummaries.  # noqa: E501
        :type: list[EmployeeStatutoryLeaveSummary]
        """

        self._statutory_leaves = statutory_leaves
