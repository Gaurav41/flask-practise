# python -m unittest test.py

from logging import debug
from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    # Ensuring flask setup correctly and working
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/login",content_type="html/text")
        self.assertEqual(response.status_code,200)

    # Ensure the login page loads correctly
    def test_login_page_loading(self):
        tester = app.test_client(self)
        response = tester.get("/login",content_type="html/text")
        self.assertTrue(b'Login'in response.data)

    #login test
    def test_login(self):
        tester = app.test_client(self)
        response = tester.post(
            "/login",
            data = dict(username="g",password="123"),
            follow_redirects = True)
        self.assertTrue(b'email' in response.data)

    #login failed test
    def test_login_fail(self):
        tester = app.test_client(self)
        response = tester.post(
            "/login",
            data = dict(username="ga",password="xyzz"),
            follow_redirects = True)
        self.assertTrue(b'Login' in response.data)
    

    # Ensure the login page loads correctly
    def test_signup_page_loading(self):
        tester = app.test_client(self)
        response = tester.get("/signup",content_type="html/text")
        self.assertTrue(b'Signup form'in response.data)


    def test_signup(self):
        tester = app.test_client(self)
        response = tester.post(
            "/signup",
            data = dict(username="test1",password="123",email="test1@gmail.com"),
            follow_redirects = True)
        self.assertTrue(b'Login' in response.data)

    #signup failed test
    def test_signup_fail(self):
        tester = app.test_client(self)
        response = tester.post(
            "/signup",
            data = dict(username="g",password="xyzz",email="anything@gmail.com"),
            follow_redirects = True)
        self.assertTrue(b'signup' in response.data)


if __name__ == "main":
    unittest.main()


# ----------------------------------------------------------------------
# Ran 7 tests in 0.226s
# 
# OK