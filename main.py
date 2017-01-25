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
            <input type="text" name="password2"/>
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

    #TODO:
    #write valid_username:
    

    #TODO:
    #write valid_password:

    #TODO:
    #write valide_email:

    def validate(self, username, password, password2, email=""):
        error_list = []
        if not username:
            username_error = "Pleaase enter a valid username."
            error_list.append(username_error)
        if password and password2:
            if not password == password2:
                pword_error = "Passwords do not match."
                if error_list:
                    error_list.append(pword_error)
                else:
                    error_list.append("")
                    error_list.append(pword_error)
        if not password or not password2:
            pword_error = "Please verify password."
            if error_list:
                error_list.append(pword_error)
            else:
                error_list.append("")
                error_list.append(pword_error)
        if email:
            if not valid_email:
                email_error = "Please enter valid email."
                if error_list:
                    error_list.append(email_error)
                else:
                    error_list = ["" for i in range(2)]
                    error_list.append(email_error)

        return error_list


    def post(self):

        username = self.request.get("username")
        password = self.request.get("password")
        password2 = self.request.get("password2")


        #TODO:
        #write valdiation function that returns list of error messages for write_form():
        #error_list = validate(username, password, password2, email)
        #if error_list:
        #    content = self.write_form(error_list)
        #else:
        #    redirect to success page
        error_list = self.validate(username, password, password2)

        if error_list:
            content = self.write_form(*error_list)
            self.response.write(content)
        else:
            content = "Woohoo! That worked!"
            self.response.write(content)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
