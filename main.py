#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re



class MainHandler(webapp2.RequestHandler):

    def write_form(self, username_error="", pword_error="", verify_error="", email_error="",
                   username="", email=""):

        header = "<h1>Signup</h1>"
    #TODO:
    #
    #implement username=username, username_error=error, etc in .format tuple
    #
        form = """
        <title>Signup</title>

        <form action="/" method="post">
            <table>
                <tbody>
                    <tr>
                        <td class="lable" style="text-align: right">
                        Username
                        </td>
                            <td>
                            <input type="text" name="username" value="{username}"/>
                        </td>
                        <td class="error" style="color: red">
                        {username_error}
                        </td>
                    </tr>
                    <tr>
                        <td class="lable" style="text-align: right">
                        Password
                        </td>
                            <td>
                                <input type="password" name="password"/>
                        </td>
                        <td class="error" style="color: red">
                        {pword_error}
                        </td>
                    </tr>
                    <tr>
                        <td class="label" style="text-align: right">
                        Verify Password
                        </td>
                            <td>
                                <input type="password" name="password2"/>
                        </td>
                        <td class="error" style="color: red">
                        {verify_error}
                        </td>
                    </tr>
                    <tr>
                        <td class="label" style="text-align: right">
                        Email (optional)
                        </td>
                            <td>
                                <input type="text" name="email" value="{email}"/>
                        </td>
                        <td class="error" style="color: red">
                        {email_error}
                        </td>
                    </tr>
                </tbody>
        </table>
        <input type="submit" value="submit">
        </form>
        """.format(
                username=username, username_error=username_error,
                pword_error=pword_error, verify_error=verify_error,
                email_error=email_error, email=email)

        return header + form

    def get(self):
        content = self.write_form()
        self.response.write(content)

    #TODO:
    #write valid_username:
    def valid_username(self, username):
        user_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return user_RE.match(username)

    #TODO:
    #write valid_password:
    def valid_password(self, password):
        user_PW = re.compile(r"^.{3,20}$")
        return user_PW.match(password)

    #TODO:
    #write valide_email:
    def valid_email(self, email):
        user_EM = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        return user_EM.match(email)

    #TODO:
    #write getUsernameError:
    def getUsernameError(self, username):
        if not self.valid_username(username):
            username_error = "Please enter valid username"
        else:
            username_error = None

        return username_error

    #TODO:
    #wite getPasswordError:
    def getPasswordError(self, password):
        if not self.valid_password(password) or not password:
            pword_error = "Please enter valid password"
        else:
            pword_error = None

        return pword_error

    #TODO:
    #write getVerifyError:
    def getVerifyError(self, password, password2):
        if password2:
            if not self.valid_password(password2):
                pword_error = "Verification is not valid"
            if not password == password2:
                    pword_error = "Passwords do not match"
            if self.valid_password(password) and password == password2:
                pword_error = None
        else:
            pword_error = "Please verify password"

        return pword_error

    #TODO:
    #write getEmailError:
    def getEmailError(self, email):
        if email:
            if not self.valid_email(email):
                email_error = "Please enter valid email"
            else:
                email_error = None
        else:
            email_error = None

        return email_error

    def error_gen(self, username, password, password2, email=""):
        #TODO:
        #incorporate dictionary (per Brian's advice)
        error_dict = {}

        username_error = self.getUsernameError(username)
        pword_error = self.getPasswordError(password)
        verify_error = self.getVerifyError(password, password2)
        email_error = self.getEmailError(email)

        if username_error:
            error_dict['username_error'] = username_error
        if pword_error:
            error_dict['pword_error'] = pword_error
        if verify_error:
            error_dict['verify_error'] = verify_error
        if email_error:
            error_dict['email_error'] = email_error
        if not error_dict:
            return None
        else:
            error_dict['username'] = username
            error_dict['email'] = email

            return error_dict

    def post(self):

        username = self.request.get("username")
        password = self.request.get("password")
        password2 = self.request.get("password2")
        email = self.request.get("email")
        #TODO:
        #write valdiation function that returns list of error messages for write_form():
        #error_list = error_gen(username, password, password2, email)
        #TODO:
        #implement error_dict
        error_dict = self.error_gen(username, password, password2, email)
        #**dict unpackages dictionary
        if error_dict:
            content = self.write_form(**error_dict)
            self.response.write(content)
        else:

            self.redirect('/thanks?username={username}'.format(username=username))

class SuccessHandler(webapp2.RequestHandler):

    def get(self):
        username = self.request.get("username")
        self.response.write("Welcome, {}!".format(username))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', SuccessHandler)
], debug=True)
