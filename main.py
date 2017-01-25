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

class MainHandler(webapp2.RequestHandler):

    def write_form(self, username_error="", pword_error="", email_error=""):

        header = "<h1>User Signup</h1>"

        form = """
        <form action="/" method="post">
            <lable>
            Username:
            </lable>
            <br>
            <input type="text" name="username"/>
            <div style="color: red">{}</div>
            <br>
            <lable>
            Password:
            </lable>
            <br>
            <input type="text" name="password"/>
            <br>
            <lable>
            Verify Password:
            </label>
            <br>
            <input type="text" name="password_verify"/>
            <div style="color: red">{}</div>
            <br>
            <lable>
            *Email:
            </lable>
            <br>
            <input type="text" name="email">
            <div style="color: red">{}</div>
            <br>
            <input type="submit" value="submit">
        </form>
        """.format(username_error, pword_error, email_error)

        return header + form

    def get(self):

        content = self.write_form()
        self.response.write(content)

    def post(self):

        username = self.request.get("username")
        password = self.request.get("password")

        if username and password:
            self.response.write("Welcome, " + username + "!")
        if not username:
            content = self.write_form("Please enter a valid username.")
            self.response.write(content)
        #error: find way to select errors without duplicating form. 
        #if not password:
        #     content = self.write_form("", "Please enter a valid password.")
        #     self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
