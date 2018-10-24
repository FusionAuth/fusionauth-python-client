#
# Copyright (c) 2016-2017, Inversoft Inc., All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#

from com.inversoft.rest_client import RESTClient

class PassportClient:
    """The PassportClient provides easy access to the Passport API."""

    def __init__(self, api_key, base_url):
        """Constructs a new PassportClient.

        Attributes:
            api_key: A string representing the API used to authenticate the API call to Passport
            base_url: A string representing the URL use to access Passport
        """
        self.api_key = api_key
        self.base_url = base_url

    def action_user(actionee_user_id, request):
        """
        Takes an action on a user. The user being actioned is called the "actionee" and the user taking the action is called the
        "actioner". Both user ids are required. You pass the actionee's user id into the method and the actioner's is put into the
        request object.

        Attributes:
            actionee_user_id: The actionee's user id.
            request: The action request that includes all of the information about the action being taken including
                    the id of the action, any options and the duration (if applicable).
        """
        return self.start().uri('/api/user/action') \
                .url_segment(actionee_user_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def cancel_action(action_id, request):
        """
        Cancels the user action.

        Attributes:
            action_id: The action id of the action to cancel.
            request: The action request that contains the information about the cancellation.
        """
        return self.start().uri('/api/user/action') \
                .url_segment(action_id) \
                .body_handler(JSONBodyHandler(request)) \
                .delete() \
                .go()

    def change_password(verification_id, request):
        """
        Changes a user's password using the verification id. This usually occurs after an email has been sent to the user
        and they clicked on a link to reset their password.

        Attributes:
            verification_id: The verification id used to find the user.
            request: The change password request that contains all of the information used to change the password.
        """
        return self.start().uri('/api/user/change-password') \
                .url_segment(verification_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def change_password_by_identity(request):
        """
        Changes a user's password using their identity (login id and password). Using a loginId instead of the verificationId
        bypasses the email verification and allows a password to be changed directly without first calling the #forgotPassword
        method.

        Attributes:
            request: The change password request that contains all of the information used to change the password.
        """
        return self.start().uri('/api/user/change-password') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def comment_on_user(request):
        """
        Adds a comment to the user's account.

        Attributes:
            request: The comment request that contains all of the information used to add the comment to the user.
        """
        return self.start().uri('/api/user/comment') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def create_application(application_id, request):
        """
        Creates an application. You can optionally specify an id for the application, but this is not required.

        Attributes:
            application_id: (Optional) The id to use for the application.
            request: The application request that contains all of the information used to create the application.
        """
        return self.start().uri('/api/application') \
                .url_segment(application_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def create_application_role(application_id, role_id, request):
        """
        Creates a new role for an application. You must specify the id of the application you are creating the role for.
        You can optionally specify an id for the role inside the ApplicationRole object itself, but this is not required.

        Attributes:
            application_id: The id of the application to create the role on.
            role_id: (Optional) The id of the role. Defaults to a secure UUID.
            request: The application request that contains all of the information used to create the role.
        """
        return self.start().uri('/api/application') \
                .url_segment(application_id) \
                .url_segment("role") \
                .url_segment(role_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def create_audit_log(request):
        """
        Creates an audit log with the message and user name (usually an email). Audit logs should be written anytime you
        make changes to the Passport database. When using the Passport Backend web interface, any changes are automatically
        written to the audit log. However, if you are accessing the API, you must write the audit logs yourself.

        Attributes:
            request: The audit log request that contains all of the information used to create the audit log entry.
        """
        return self.start().uri('/api/system/audit-log') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def create_email_template(email_template_id, request):
        """
        Creates an email template. You can optionally specify an id for the email template when calling this method, but it
        is not required.

        Attributes:
            email_template_id: (Optional) The id for the template.
            request: The email template request that contains all of the information used to create the email template.
        """
        return self.start().uri('/api/email/template') \
                .url_segment(email_template_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def create_user(user_id, request):
        """
        Creates a user with an optional id.

        Attributes:
            user_id: (Optional) The id for the user.
            request: The user request that contains all of the information used to create the user.
        """
        return self.start().uri('/api/user') \
                .url_segment(user_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def create_user_action(user_action_id, request):
        """
        Creates a user action. This action cannot be taken on a user until this call successfully returns. Anytime after
        that the user action can be applied to any user.

        Attributes:
            user_action_id: (Optional) The id for the user action.
            request: The user action request that contains all of the information used to create the user action.
        """
        return self.start().uri('/api/user-action') \
                .url_segment(user_action_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def create_user_action_reason(user_action_reason_id, request):
        """
        Creates a user reason. This user action reason cannot be used when actioning a user until this call completes
        successfully. Anytime after that the user action reason can be used.

        Attributes:
            user_action_reason_id: (Optional) The id for the user action reason.
            request: The user action reason request that contains all of the information used to create the user action reason.
        """
        return self.start().uri('/api/user-action-reason') \
                .url_segment(user_action_reason_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def create_webhook(webhook_id, request):
        """
        Creates a webhook. You can optionally specify an id for the webhook when calling this method, but it is not required.

        Attributes:
            webhook_id: (Optional) The id for the webhook.
            request: The webhook request that contains all of the information used to create the webhook.
        """
        return self.start().uri('/api/webhook') \
                .url_segment(webhook_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def deactivate_application(application_id):
        """
        Deactivates the application with the given id.

        Attributes:
            application_id: The id of the application to deactivate.
        """
        return self.start().uri('/api/application') \
                .url_segment(application_id) \
                .delete() \
                .go()

    def deactivate_user(user_id):
        """
        Deactivates the user with the given id.

        Attributes:
            user_id: The id of the user to deactivate.
        """
        return self.start().uri('/api/user') \
                .url_segment(user_id) \
                .delete() \
                .go()

    def deactivate_user_action(user_action_id):
        """
        Deactivates the user action with the given id.

        Attributes:
            user_action_id: The id of the user action to deactivate.
        """
        return self.start().uri('/api/user-action') \
                .url_segment(user_action_id) \
                .delete() \
                .go()

    def deactivate_users(user_ids):
        """
        Deactivates the users with the given ids.

        Attributes:
            user_ids: The ids of the users to deactivate.
        """
        return self.start().uri('/api/user/bulk') \
                .url_parameter('userId', user_ids) \
                .delete() \
                .go()

    def delete_application(application_id):
        """
        Hard deletes an application. This is a dangerous operation and should not be used in most circumstances. This will
        delete the application, any registrations for that application, metrics and reports for the application, all the
        roles for the application, and any other data associated with the application. This operation could take a very
        long time, depending on the amount of data in your database.

        Attributes:
            application_id: The id of the application to delete.
        """
        return self.start().uri('/api/application') \
                .url_segment(application_id) \
                .url_parameter('hardDelete', true) \
                .delete() \
                .go()

    def delete_application_role(application_id, role_id):
        """
        Hard deletes an application role. This is a dangerous operation and should not be used in most circumstances. This
        permanently removes the given role from all users that had it.

        Attributes:
            application_id: The id of the application to deactivate.
            role_id: The id of the role to delete.
        """
        return self.start().uri('/api/application') \
                .url_segment(application_id) \
                .url_segment("role") \
                .url_segment(role_id) \
                .delete() \
                .go()

    def delete_email_template(email_template_id):
        """
        Deletes the email template for the given id.

        Attributes:
            email_template_id: The id of the email template to delete.
        """
        return self.start().uri('/api/email/template') \
                .url_segment(email_template_id) \
                .delete() \
                .go()

    def delete_registration(user_id, application_id):
        """
        Deletes the user registration for the given user and application.

        Attributes:
            user_id: The id of the user whose registration is being deleted.
            application_id: The id of the application to remove the registration for.
        """
        return self.start().uri('/api/user/registration') \
                .url_segment(user_id) \
                .url_segment(application_id) \
                .delete() \
                .go()

    def delete_user(user_id):
        """
        Deletes the user for the given id. This permanently deletes all information, metrics, reports and data associated
        with the user.

        Attributes:
            user_id: The id of the user to delete.
        """
        return self.start().uri('/api/user') \
                .url_segment(user_id) \
                .url_parameter('hardDelete', true) \
                .delete() \
                .go()

    def delete_user_action(user_action_id):
        """
        Deletes the user action for the given id. This permanently deletes the user action and also any history and logs of
        the action being applied to any users.

        Attributes:
            user_action_id: The id of the user action to delete.
        """
        return self.start().uri('/api/user-action') \
                .url_segment(user_action_id) \
                .url_parameter('hardDelete', true) \
                .delete() \
                .go()

    def delete_user_action_reason(user_action_reason_id):
        """
        Deletes the user action reason for the given id.

        Attributes:
            user_action_reason_id: The id of the user action reason to delete.
        """
        return self.start().uri('/api/user-action-reason') \
                .url_segment(user_action_reason_id) \
                .delete() \
                .go()

    def delete_users(user_ids):
        """
        Deletes the users with the given ids.

        Attributes:
            user_ids: The ids of the users to delete.
        """
        return self.start().uri('/api/user/bulk') \
                .url_parameter('userId', user_ids) \
                .url_parameter('hardDelete', true) \
                .delete() \
                .go()

    def delete_webhook(webhook_id):
        """
        Deletes the webhook for the given id.

        Attributes:
            webhook_id: The id of the webhook to delete.
        """
        return self.start().uri('/api/webhook') \
                .url_segment(webhook_id) \
                .delete() \
                .go()

    def exchange_refresh_token_for_access_token(request):
        """
        Exchange a refresh token for a new Access Token (JWT).

        Attributes:
            request: The refresh request.
        """
        return self.start().uri('/api/jwt/refresh') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def forgot_password(request):
        """
        Begins the forgot password sequence, which kicks off an email to the user so that they can reset their password.

        Attributes:
            request: The request that contains the information about the user so that they can be emailed.
        """
        return self.start().uri('/api/user/forgot-password') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def import_users(request):
        """
        Bulk imports multiple users. This does some validation, but then tries to run batch inserts of users. This reduces
        latency when inserting lots of users. Therefore, the error response might contain some information about failures,
        but it will likely be pretty generic.

        Attributes:
            request: The request that contains all of the information about all of the users to import.
        """
        return self.start().uri('/api/user/import') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def issue_access_token(application_id, encoded_jwt):
        """
        Issue a new access token (JWT) for the requested Application after ensuring the provided JWT is valid. A valid
        access token is properly signed and not expired.
        <p/>
        This API may be used in an SSO configuration to issue new tokens for another application after the user has
        obtained a valid token from authentication.

        Attributes:
            application_id: The Application Id for which you are requesting a new access token be issued.
            encoded_jwt: The encoded JWT (access token).
        """
        return self.start().uri('/api/jwt/issue') \
                .authorization("JWT " + encodedJWT)
                .url_parameter('applicationId', application_id) \
                .get() \
                .go()

    def login(request):
        """
        Logs a user in.

        Attributes:
            request: The login request that contains the user credentials used to log them in.
        """
        return self.start().uri('/api/login') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def login_ping(user_id, application_id, caller_ip_address):
        """
        Sends a ping to Passport indicating that the user was automatically logged into an application. When using
        Passport's SSO or your own, you should call this if the user is already logged in centrally, but accesses an
        application where they no longer have a session. This helps correctly track login counts, times and helps with
        reporting.

        Attributes:
            user_id: The id of the user that was logged in.
            application_id: The id of the application that they logged into.
            caller_ip_address: (Optional) The IP address of the end-user that is logging in. If a null value is provided
                    the IP address will be that of the client or last proxy that sent the request.
        """
        return self.start().uri('/api/login') \
                .url_segment(user_id) \
                .url_segment(application_id) \
                .url_parameter('ipAddress', caller_ip_address) \
                .put() \
                .go()

    def logout(global, refresh_token):
        """
        The Logout API is intended to be used to remove the refresh token and access token cookies if they exist on the
        client and revoke the refresh token stored. This API does nothing if the request does not contain an access
        token or refresh token cookies.

        Attributes:
            global: When this value is set to true all of the refresh tokens issued to the owner of the
                    provided token will be revoked.
            refresh_token: (Optional) The refresh_token as a request parameter instead of coming in via a cookie.
                    If provided this takes precedence over the cookie.
        """
        return self.start().uri('/api/logout') \
                .url_parameter('global', global) \
                .url_parameter('refreshToken', refresh_token) \
                .post() \
                .go()

    def modify_action(action_id, request):
        """
        Modifies a temporal user action by changing the expiration of the action and optionally adding a comment to the
        action.

        Attributes:
            action_id: The id of the action to modify. This is technically the user action log id.
            request: The request that contains all of the information about the modification.
        """
        return self.start().uri('/api/user/action') \
                .url_segment(action_id) \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def reactivate_application(application_id):
        """
        Reactivates the application with the given id.

        Attributes:
            application_id: The id of the application to reactivate.
        """
        return self.start().uri('/api/application') \
                .url_segment(application_id) \
                .url_parameter('reactivate', true) \
                .put() \
                .go()

    def reactivate_user(user_id):
        """
        Reactivates the user with the given id.

        Attributes:
            user_id: The id of the user to reactivate.
        """
        return self.start().uri('/api/user') \
                .url_segment(user_id) \
                .url_parameter('reactivate', true) \
                .put() \
                .go()

    def reactivate_user_action(user_action_id):
        """
        Reactivates the user action with the given id.

        Attributes:
            user_action_id: The id of the user action to reactivate.
        """
        return self.start().uri('/api/user-action') \
                .url_segment(user_action_id) \
                .url_parameter('reactivate', true) \
                .put() \
                .go()

    def register(user_id, request):
        """
        Registers a user for an application. If you provide the User and the UserRegistration object on this request, it
        will create the user as well as register them for the application. This is called a Full Registration. However, if
        you only provide the UserRegistration object, then the user must already exist and they will be registered for the
        application. The user id can also be provided and it will either be used to look up an existing user or it will be
        used for the newly created User.

        Attributes:
            user_id: (Optional) The id of the user being registered for the application and optionally created.
            request: The request that optionally contains the User and must contain the UserRegistration.
        """
        return self.start().uri('/api/user/registration') \
                .url_segment(user_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def resend_email_verification(email):
        """
        Re-sends the verification email to the user.

        Attributes:
            email: The email address of the user that needs a new verification email.
        """
        return self.start().uri('/api/user/verify-email') \
                .url_parameter('email', email) \
                .put() \
                .go()

    def retrieve_action(action_id):
        """
        Retrieves a single action log (the log of a user action that was taken on a user previously) for the given id.

        Attributes:
            action_id: The id of the action to retrieve.
        """
        return self.start().uri('/api/user/action') \
                .url_segment(action_id) \
                .get() \
                .go()

    def retrieve_actions(user_id):
        """
        Retrieves all of the actions for the user with the given id.

        Attributes:
            user_id: The id of the user to fetch the actions for.
        """
        return self.start().uri('/api/user/action') \
                .url_parameter('userId', user_id) \
                .get() \
                .go()

    def retrieve_application(application_id):
        """
        Retrieves the application for the given id or all of the applications if the id is null.

        Attributes:
            application_id: (Optional) The application id.
        """
        return self.start().uri('/api/application') \
                .url_segment(application_id) \
                .get() \
                .go()

    def retrieve_applications():
        """
        Retrieves all of the applications.

        Attributes:
        """
        return self.start().uri('/api/application') \
                .get() \
                .go()

    def retrieve_audit_log(audit_log_id):
        """
        Retrieves a single audit log for the given id.

        Attributes:
            audit_log_id: The id of the audit log to retrieve.
        """
        return self.start().uri('/api/system/audit-log') \
                .url_segment(audit_log_id) \
                .get() \
                .go()

    def retrieve_daily_active_report(application_id, start, end):
        """
        Retrieves the daily active user report between the two instants. If you specify an application id, it will only
        return the daily active counts for that application.

        Attributes:
            application_id: (Optional) The application id.
            start: The start instant as UTC milliseconds since Epoch.
            end: The end instant as UTC milliseconds since Epoch.
        """
        return self.start().uri('/api/report/daily-active-user') \
                .url_parameter('applicationId', application_id) \
                .url_parameter('start', start) \
                .url_parameter('end', end) \
                .get() \
                .go()

    def retrieve_email_template(email_template_id):
        """
        Retrieves the email template for the given id. If you don't specify the id, this will return all of the email templates.

        Attributes:
            email_template_id: (Optional) The id of the email template.
        """
        return self.start().uri('/api/email/template') \
                .url_segment(email_template_id) \
                .get() \
                .go()

    def retrieve_email_template_preview(request):
        """
        Creates a preview of the email template provided in the request. This allows you to preview an email template that
        hasn't been saved to the database yet. The entire email template does not need to be provided on the request. This
        will create the preview based on whatever is given.

        Attributes:
            request: The request that contains the email template and optionally a locale to render it in.
        """
        return self.start().uri('/api/email/template/preview') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def retrieve_email_templates():
        """
        Retrieves all of the email templates.

        Attributes:
        """
        return self.start().uri('/api/email/template') \
                .get() \
                .go()

    def retrieve_inactive_applications():
        """
        Retrieves all of the applications that are currently inactive.

        Attributes:
        """
        return self.start().uri('/api/application') \
                .url_parameter('inactive', true) \
                .get() \
                .go()

    def retrieve_inactive_user_actions():
        """
        Retrieves all of the user actions that are currently inactive.

        Attributes:
        """
        return self.start().uri('/api/user-action') \
                .url_parameter('inactive', true) \
                .get() \
                .go()

    def retrieve_integration():
        """
        Retrieves the available integrations.

        Attributes:
        """
        return self.start().uri('/api/integration') \
                .get() \
                .go()

    def retrieve_jwt_public_key(key_id):
        """
        Retrieves the Public Key configured for verifying JSON Web Tokens (JWT) by the key Id. If the key Id is provided a
        single public key will be returned if one is found by that id. If the optional parameter key Id is not provided all
        public keys will be returned.

        Attributes:
            key_id: (Optional) The id of the public key.
        """
        return self.start().uri('/api/jwt/public-key') \
                .url_segment(key_id) \
                .get() \
                .go()

    def retrieve_jwt_public_keys():
        """
        Retrieves all Public Keys configured for verifying JSON Web Tokens (JWT).

        Attributes:
        """
        return self.start().uri('/api/jwt/public-key') \
                .get() \
                .go()

    def retrieve_login_report(application_id, start, end):
        """
        Retrieves the login report between the two instants. If you specify an application id, it will only return the
        login counts for that application.

        Attributes:
            application_id: (Optional) The application id.
            start: The start instant as UTC milliseconds since Epoch.
            end: The end instant as UTC milliseconds since Epoch.
        """
        return self.start().uri('/api/report/login') \
                .url_parameter('applicationId', application_id) \
                .url_parameter('start', start) \
                .url_parameter('end', end) \
                .get() \
                .go()

    def retrieve_monthly_active_report(application_id, start, end):
        """
        Retrieves the monthly active user report between the two instants. If you specify an application id, it will only
        return the monthly active counts for that application.

        Attributes:
            application_id: (Optional) The application id.
            start: The start instant as UTC milliseconds since Epoch.
            end: The end instant as UTC milliseconds since Epoch.
        """
        return self.start().uri('/api/report/monthly-active-user') \
                .url_parameter('applicationId', application_id) \
                .url_parameter('start', start) \
                .url_parameter('end', end) \
                .get() \
                .go()

    def retrieve_refresh_tokens(user_id):
        """
        Retrieves the refresh tokens that belong to the user with the given id.

        Attributes:
            user_id: The id of the user.
        """
        return self.start().uri('/api/jwt/refresh') \
                .url_parameter('userId', user_id) \
                .get() \
                .go()

    def retrieve_registration(user_id, application_id):
        """
        Retrieves the user registration for the user with the given id and the given application id.

        Attributes:
            user_id: The id of the user.
            application_id: The id of the application.
        """
        return self.start().uri('/api/user/registration') \
                .url_segment(user_id) \
                .url_segment(application_id) \
                .get() \
                .go()

    def retrieve_registration_report(application_id, start, end):
        """
        Retrieves the registration report between the two instants. If you specify an application id, it will only return
        the registration counts for that application.

        Attributes:
            application_id: (Optional) The application id.
            start: The start instant as UTC milliseconds since Epoch.
            end: The end instant as UTC milliseconds since Epoch.
        """
        return self.start().uri('/api/report/registration') \
                .url_parameter('applicationId', application_id) \
                .url_parameter('start', start) \
                .url_parameter('end', end) \
                .get() \
                .go()

    def retrieve_system_configuration():
        """
        Retrieves the system configuration.

        Attributes:
        """
        return self.start().uri('/api/system-configuration') \
                .get() \
                .go()

    def retrieve_total_report():
        """
        Retrieves the totals report. This contains all of the total counts for each application and the global registration
        count.

        Attributes:
        """
        return self.start().uri('/api/report/totals') \
                .get() \
                .go()

    def retrieve_user(user_id):
        """
        Retrieves the user for the given id.

        Attributes:
            user_id: The id of the user.
        """
        return self.start().uri('/api/user') \
                .url_segment(user_id) \
                .get() \
                .go()

    def retrieve_user_action(user_action_id):
        """
        Retrieves the user action for the given id. If you pass in null for the id, this will return all of the user
        actions.

        Attributes:
            user_action_id: (Optional) The id of the user action.
        """
        return self.start().uri('/api/user-action') \
                .url_segment(user_action_id) \
                .get() \
                .go()

    def retrieve_user_action_reason(user_action_reason_id):
        """
        Retrieves the user action reason for the given id. If you pass in null for the id, this will return all of the user
        action reasons.

        Attributes:
            user_action_reason_id: (Optional) The id of the user action reason.
        """
        return self.start().uri('/api/user-action-reason') \
                .url_segment(user_action_reason_id) \
                .get() \
                .go()

    def retrieve_user_action_reasons():
        """
        Retrieves all the user action reasons.

        Attributes:
        """
        return self.start().uri('/api/user-action-reason') \
                .get() \
                .go()

    def retrieve_user_actions():
        """
        Retrieves all of the user actions.

        Attributes:
        """
        return self.start().uri('/api/user-action') \
                .get() \
                .go()

    def retrieve_user_by_email(email):
        """
        Retrieves the user for the given email.

        Attributes:
            email: The email of the user.
        """
        return self.start().uri('/api/user') \
                .url_parameter('email', email) \
                .get() \
                .go()

    def retrieve_user_by_login_id(login_id):
        """
        Retrieves the user for the loginId. The loginId can be either the username or the email.

        Attributes:
            login_id: The email or username of the user.
        """
        return self.start().uri('/api/user') \
                .url_parameter('loginId', login_id) \
                .get() \
                .go()

    def retrieve_user_by_username(username):
        """
        Retrieves the user for the given username.

        Attributes:
            username: The username of the user.
        """
        return self.start().uri('/api/user') \
                .url_parameter('username', username) \
                .get() \
                .go()

    def retrieve_user_comments(user_id):
        """
        Retrieves all of the comments for the user with the given id.

        Attributes:
            user_id: The id of the user.
        """
        return self.start().uri('/api/user/comment') \
                .url_segment(user_id) \
                .get() \
                .go()

    def retrieve_user_login_report(user_id, offset, limit):
        """
        Retrieves the last number of login records for a user.

        Attributes:
            user_id: The id of the user.
            offset: The initial record. e.g. 0 is the last login, 100 will be the 100th most recent login.
            limit: (Optional, defaults to 10) The number of records to retrieve.
        """
        return self.start().uri('/api/report/user-login') \
                .url_parameter('userId', user_id) \
                .url_parameter('offset', offset) \
                .url_parameter('limit', limit) \
                .get() \
                .go()

    def retrieve_webhook(webhook_id):
        """
        Retrieves the webhook for the given id. If you pass in null for the id, this will return all the webhooks.

        Attributes:
            webhook_id: (Optional) The id of the webhook.
        """
        return self.start().uri('/api/webhook') \
                .url_segment(webhook_id) \
                .get() \
                .go()

    def retrieve_webhooks():
        """
        Retrieves all the webhooks.

        Attributes:
        """
        return self.start().uri('/api/webhook') \
                .get() \
                .go()

    def revoke_refresh_token(token, user_id, application_id):
        """
        Revokes a single refresh token, all tokens for a user or all tokens for an application. If you provide a user id
        and an application id, this will delete all the refresh tokens for that user for that application.

        Attributes:
            token: (Optional) The refresh token to delete.
            user_id: (Optional) The user id whose tokens to delete.
            application_id: (Optional) The application id of the tokens to delete.
        """
        return self.start().uri('/api/jwt/refresh') \
                .url_parameter('token', token) \
                .url_parameter('userId', user_id) \
                .url_parameter('applicationId', application_id) \
                .delete() \
                .go()

    def search_audit_logs(request):
        """
        Searches the audit logs with the specified criteria and pagination.

        Attributes:
            request: The search criteria and pagination information.
        """
        return self.start().uri('/api/system/audit-log/search') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def search_users(ids):
        """
        Retrieves the users for the given ids. If any id is invalid, it is ignored.

        Attributes:
            ids: The user ids to search for.
        """
        return self.start().uri('/api/user/search') \
                .url_parameter('ids', ids) \
                .get() \
                .go()

    def search_users_by_query_string(request):
        """
        Retrieves the users for the given search criteria and pagination.

        Attributes:
            request: The search criteria and pagination constraints. Fields used: queryString, numberOfResults, startRow,
                    and sort fields.
        """
        return self.start().uri('/api/user/search') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def send_email(email_template_id, request):
        """
        Send an email using an email template id. You can optionally provide <code>requestData</code> to access key value
        pairs in the email template.

        Attributes:
            email_template_id: The id for the template.
            request: The send email request that contains all of the information used to send the email.
        """
        return self.start().uri('/api/email/send') \
                .url_segment(email_template_id) \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def update_application(application_id, request):
        """
        Updates the application with the given id.

        Attributes:
            application_id: The id of the application to update.
            request: The request that contains all of the new application information.
        """
        return self.start().uri('/api/application') \
                .url_segment(application_id) \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def update_application_role(application_id, role_id, request):
        """
        Updates the application role with the given id for the application.

        Attributes:
            application_id: The id of the application that the role belongs to.
            role_id: The id of the role to update.
            request: The request that contains all of the new role information.
        """
        return self.start().uri('/api/application') \
                .url_segment(application_id) \
                .url_segment("role") \
                .url_segment(role_id) \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def update_email_template(email_template_id, request):
        """
        Updates the email template with the given id.

        Attributes:
            email_template_id: The id of the email template to update.
            request: The request that contains all of the new email template information.
        """
        return self.start().uri('/api/email/template') \
                .url_segment(email_template_id) \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def update_integrations(request):
        """
        Updates the available integrations.

        Attributes:
            request: The request that contains all of the new integration information.
        """
        return self.start().uri('/api/integration') \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def update_registration(user_id, request):
        """
        Updates the registration for the user with the given id and the application defined in the request.

        Attributes:
            user_id: The id of the user whose registration is going to be updated.
            request: The request that contains all of the new registration information.
        """
        return self.start().uri('/api/user/registration') \
                .url_segment(user_id) \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def update_system_configuration(request):
        """
        Updates the system configuration.

        Attributes:
            request: The request that contains all of the new system configuration information.
        """
        return self.start().uri('/api/system-configuration') \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def update_user(user_id, request):
        """
        Updates the user with the given id.

        Attributes:
            user_id: The id of the user to update.
            request: The request that contains all of the new user information.
        """
        return self.start().uri('/api/user') \
                .url_segment(user_id) \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def update_user_action(user_action_id, request):
        """
        Updates the user action with the given id.

        Attributes:
            user_action_id: The id of the user action to update.
            request: The request that contains all of the new user action information.
        """
        return self.start().uri('/api/user-action') \
                .url_segment(user_action_id) \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def update_user_action_reason(user_action_reason_id, request):
        """
        Updates the user action reason with the given id.

        Attributes:
            user_action_reason_id: The id of the user action reason to update.
            request: The request that contains all of the new user action reason information.
        """
        return self.start().uri('/api/user-action-reason') \
                .url_segment(user_action_reason_id) \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def update_webhook(webhook_id, request):
        """
        Updates the webhook with the given id.

        Attributes:
            webhook_id: The id of the webhook to update.
            request: The request that contains all of the new webhook information.
        """
        return self.start().uri('/api/webhook') \
                .url_segment(webhook_id) \
                .body_handler(JSONBodyHandler(request)) \
                .put() \
                .go()

    def validate_access_token(encoded_jwt):
        """
        Validates the provided JWT (encoded JWT string) to ensure the token is valid. A valid access token is properly
        signed and not expired.
        <p/>
        This API may be used to verify the JWT as well as decode the encoded JWT into human readable identity claims.

        Attributes:
            encoded_jwt: The encoded JWT (access token).
        """
        return self.start().uri('/api/jwt/validate') \
                .authorization("JWT " + encodedJWT)
                .get() \
                .go()

    def verify_email(verification_id):
        """
        Confirms a email verification. The id given is usually from an email sent to the user.

        Attributes:
            verification_id: The verification id sent to the user.
        """
        return self.start().uri('/api/user/verify-email') \
                .url_segment(verification_id) \
                .post() \
                .go()

    def verify_two_factor(request):
        """
        Confirms a two factor authentication code.

        Attributes:
            request: The two factor request information.
        """
        return self.start().uri('/api/two-factor') \
                .body_handler(JSONBodyHandler(request)) \
                .post() \
                .go()

    def start(self):
        return RESTClient().authorization(self.api_key).url(self.base_url)
