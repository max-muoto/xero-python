# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""

"""
    OpenAPI spec version: 2.16.6
"""

import importlib
import re  # noqa: F401

from xero_python import exceptions
from xero_python.api_client import ApiClient, ModelFinder

try:
    from .exception_handler import translate_status_exception
except ImportError:
    translate_status_exception = exceptions.translate_status_exception


class empty:
    """empty object to mark optional parameter not set"""


class FinanceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    base_url = "https://api.xero.com/finance.xro/1.0"
    models_module = importlib.import_module("xero_python.finance.models")

    def __init__(self, api_client=None, base_url=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_resource_url(self, resource_path):
        """
        Combine API base url with resource specific path
        :param str resource_path: API endpoint specific path
        :return: str full resource path
        """
        return self.base_url + resource_path

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    def get_accounting_activity_account_usage(
        self,
        xero_tenant_id,
        start_month=empty,
        end_month=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Get account usage  # noqa: E501
        OAuth2 scope: finance.accountingactivity.read
        A summary of how each account is being transacted on exposing the level of detail and amounts attributable to manual adjustments.  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str start_month: date, yyyy-MM                 If no parameter is provided, the month 12 months prior to the end month will be used.                Account usage for up to 12 months from this date will be returned.
        :param str end_month: date, yyyy-MM                 If no parameter is provided, the current month will be used.                Account usage for up to 12 months prior to this date will be returned.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: AccountUsageResponse
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_accounting_activity_account_usage`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        if start_month is not empty:
            query_params.append(("startMonth", start_month))

        if end_month is not empty:
            query_params.append(("endMonth", end_month))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/AccountingActivities/AccountUsage")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="AccountUsageResponse",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(
                error, self, "get_accounting_activity_account_usage"
            )

    def get_accounting_activity_lock_history(
        self,
        xero_tenant_id,
        end_date=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Get lock history  # noqa: E501
        OAuth2 scope: finance.accountingactivity.read
        Provides a history of locking of accounting books. Locking may be an indicator of good accounting practices that could reduce the risk of changes to accounting records in prior periods.  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str end_date: date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any changes to hard or soft lock dates that were made within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a change is visible from this API.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: LockHistoryResponse
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_accounting_activity_lock_history`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        if end_date is not empty:
            query_params.append(("endDate", end_date))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/AccountingActivities/LockHistory")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="LockHistoryResponse",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(
                error, self, "get_accounting_activity_lock_history"
            )

    def get_accounting_activity_report_history(
        self,
        xero_tenant_id,
        end_date=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Get report history  # noqa: E501
        OAuth2 scope: finance.accountingactivity.read
        For a specified organisation, provides a summary of all the reports published within a given period, which may be an indicator for good business management and oversight.  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str end_date: date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any reports that were published within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a published report is visible from this API.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: ReportHistoryResponse
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_accounting_activity_report_history`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        if end_date is not empty:
            query_params.append(("endDate", end_date))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/AccountingActivities/ReportHistory")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="ReportHistoryResponse",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(
                error, self, "get_accounting_activity_report_history"
            )

    def get_accounting_activity_user_activities(
        self,
        xero_tenant_id,
        data_month=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Get user activities  # noqa: E501
        OAuth2 scope: finance.accountingactivity.read
        For a specified organisation, provides a list of all the users registered, and a history of their accounting transactions. Also identifies the existence of an external accounting advisor and the level of interaction.  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str data_month: date, yyyy-MM                 The specified month must be complete (in the past); The current month cannot be specified since it is not complete.                If no parameter is provided, the month immediately previous to the current month will be used.                Any user activities occurring within the specified month will be returned.                Please be aware that there may be a delay of up to 3 days before a user activity is visible from this API.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: UserActivitiesResponse
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_accounting_activity_user_activities`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        if data_month is not empty:
            query_params.append(("dataMonth", data_month))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/AccountingActivities/UserActivities")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="UserActivitiesResponse",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(
                error, self, "get_accounting_activity_user_activities"
            )

    def get_cash_validation(
        self,
        xero_tenant_id,
        balance_date=empty,
        as_at_system_date=empty,
        begin_date=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Get cash validation  # noqa: E501
        OAuth2 scope: finance.cashvalidation.read
        Summarizes the total cash position for each account for an org  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str balance_date: date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘balance date’ will return transactions based on the accounting date entered by the user.  Transactions before the balanceDate will be included.  The user has discretion as to which accounting period the transaction relates to.    The ‘balance date’  will control the latest maximum date of transactions included in the aggregate numbers.  Balance date does not affect the CurrentStatement object, as this will always return the most recent statement before asAtSystemDate (if specified)
        :param str as_at_system_date: date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘as at’ date will return transactions based on the  creation date.  It reflects the date the transactions were entered into Xero, not the accounting date.  The ‘as at’ date can not be overridden by the user.  This can be used to estimate a ‘historical frequency of reconciliation’.    The ‘as at’ date will affect the current statement in the response, as any candidate statements created after this date will be filtered out.  Thus the current statement returned will be the most recent statement prior to the specified ‘as at’ date.  Be aware that neither the begin date, nor the balance date, will affect the current statement.    Note;  information is only presented when system architecture allows, meaning historical cash validation information will be an estimate. In addition, delete events are not aware of the ‘as at’ functionality in this endpoint, meaning that transactions deleted at the time the API is accessed will be considered to always have been deleted.
        :param str begin_date: date, yyyy-MM-dd     If no parameter is provided, the aggregate results will be drawn from the user’s total history.    The ‘begin date’ will return transactions based on the accounting date entered by the user. Transactions after the beginDate will be included.  The user has discretion as to which accounting period the transaction relates to.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: list[CashValidationResponse]
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_cash_validation`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        if balance_date is not empty:
            query_params.append(("balanceDate", balance_date))

        if as_at_system_date is not empty:
            query_params.append(("asAtSystemDate", as_at_system_date))

        if begin_date is not empty:
            query_params.append(("beginDate", begin_date))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/CashValidation")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="list[CashValidationResponse]",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "get_cash_validation")

    def get_financial_statement_balance_sheet(
        self,
        xero_tenant_id,
        balance_date=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Get Balance Sheet report  # noqa: E501
        OAuth2 scope: finance.statements.read
        The balance sheet report is a standard financial report which describes the financial position of an organisation at a point in time.  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str balance_date: Specifies the date for balance sheet report.    Format yyyy-MM-dd. If no parameter is provided, the current date will be used.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: BalanceSheetResponse
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_financial_statement_balance_sheet`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        if balance_date is not empty:
            query_params.append(("balanceDate", balance_date))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/FinancialStatements/BalanceSheet")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="BalanceSheetResponse",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(
                error, self, "get_financial_statement_balance_sheet"
            )

    def get_financial_statement_cashflow(
        self,
        xero_tenant_id,
        start_date=empty,
        end_date=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Get Cash flow report  # noqa: E501
        OAuth2 scope: finance.statements.read
        The statement of cash flows - direct method, provides the year to date changes in operating, financing and investing cash flow activities for an organisation. Cashflow statement is not available in US region at this stage.  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str start_date: Date e.g. yyyy-MM-dd    Specifies the start date for cash flow report.    If no parameter is provided, the date of 12 months before the end date will be used.
        :param str end_date: Date e.g. yyyy-MM-dd    Specifies the end date for cash flow report.    If no parameter is provided, the current date will be used.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: CashflowResponse
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_financial_statement_cashflow`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        if start_date is not empty:
            query_params.append(("startDate", start_date))

        if end_date is not empty:
            query_params.append(("endDate", end_date))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/FinancialStatements/Cashflow")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="CashflowResponse",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(
                error, self, "get_financial_statement_cashflow"
            )

    def get_financial_statement_profit_and_loss(
        self,
        xero_tenant_id,
        start_date=empty,
        end_date=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Get Profit & Loss report  # noqa: E501
        OAuth2 scope: finance.statements.read
        The profit and loss statement is a standard financial report providing detailed year to date income and expense detail for an organisation.  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str start_date: Date e.g. yyyy-MM-dd    Specifies the start date for profit and loss report    If no parameter is provided, the date of 12 months before the end date will be used.
        :param str end_date: Date e.g. yyyy-MM-dd    Specifies the end date for profit and loss report     If no parameter is provided, the current date will be used.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: ProfitAndLossResponse
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_financial_statement_profit_and_loss`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        if start_date is not empty:
            query_params.append(("startDate", start_date))

        if end_date is not empty:
            query_params.append(("endDate", end_date))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/FinancialStatements/ProfitAndLoss")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="ProfitAndLossResponse",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(
                error, self, "get_financial_statement_profit_and_loss"
            )

    def get_financial_statement_trial_balance(
        self,
        xero_tenant_id,
        end_date=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Get Trial Balance report  # noqa: E501
        OAuth2 scope: finance.statements.read
        The trial balance provides a detailed list of all accounts of an organisation at a point in time, with revenue and expense items being year to date.  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str end_date: Date e.g. yyyy-MM-dd     Specifies the end date for trial balance report     If no parameter is provided, the current date will be used.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: TrialBalanceResponse
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_financial_statement_trial_balance`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        if end_date is not empty:
            query_params.append(("endDate", end_date))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/FinancialStatements/TrialBalance")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="TrialBalanceResponse",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(
                error, self, "get_financial_statement_trial_balance"
            )
