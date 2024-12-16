"""
MIT License

Copyright (c) 2023-Present cxdzc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class UnknownError(Exception):  # 0
    """
    Error code 0
    Unhandled error, should not occur.
    """
    pass

class EmptyKey(Exception):  # 1
    """
    Error code 1
    Private key is empty in the current request.
    """
    pass

class InvalidKey(Exception):  # 2
    """
    Error code 2
    Private key is wrong/incorrect format.
    """
    pass

class WrongType(Exception):  # 3
    """
    Error code 3
    Requesting an incorrect basic type.
    """
    pass

class WrongFields(Exception):  # 4
    """
    Error code 4
    Requesting incorrect section fields.
    """
    pass

class TooManyRequests(Exception):  # 5
    """
    Error code 5
    Requests are blocked for a small period of time because
    of too many requests per user (max 100 per minute).
    """
    pass

class IncorrectID(Exception):  # 6
    """
    Error code 6
    Wrong ID value.
    """
    pass

class InvalidIDRelation(Exception):  # 7
    """
    Error code 7
    A requested selection is private (For example, personal data of another user / faction).
    """
    pass

class IPBlock(Exception):  # 8
    """
    Error code 8
    Current IP is banned for a small period of time because of abuse.
    """
    pass

class APIDisabled(Exception):  # 9
    """
    Error code 9
    API is disabled currently.
    """
    pass

class FederalJail(Exception):  # 10
    """
    Error code 10
    The owner is in federal jail.
    """
    pass

class KeyChangeError(Exception):  # 11
    """
    Error code 11
    You can only change your API key once every 60 seconds.
    """
    pass

class KeyReadError(Exception):  # 12
    """
    Error code 12
    Error reading key from database.
    """
    pass

class OwnerInactive(Exception):  # 13
    """
    Error code 13
    The key owner hasn't been online for more than 7 days.
    """
    pass

class DailyReadLimit(Exception):  # 14
    """
    Error code 14
    Daily read limit reached.
    """
    pass

class TemporaryError(Exception):  # 15
    """
    Error code 15
    AN error code specifically for testing purposes.
    """
    pass

class LowAccessLevel(Exception):  # 16
    """
    Error code 16
    A selection is being called which this key doesn't have permissions for.
    """
    pass

class BackendError(Exception):  # 17
    """
    Error code 17
    Backend error.
    """
    pass

class KeyPaused(Exception):  # 18
    """
    Error code 18
    Key is paused by the owner.
    """
    pass

class OtherError(Exception):
    """
    There is some error that likely isn't related to the API.
    """
    pass


class errored:
    def handler(self, response) -> dict:
        data = response.json()
        if "error" in data:
            error_code = data["error"]["code"]
            
            if error_code == 0:
                raise UnknownError("Unhandled error, shouldn't occur.")
            
            elif error_code == 1:
                raise EmptyKey("Private key is empty in current request.")
            
            elif error_code == 2:
                raise InvalidKey("Private key is wrong/incorrect format.")
            
            elif error_code == 3:
                raise WrongType("Requesting an incorrect basic type.")
            
            elif error_code == 4:
                raise WrongFields("Requesting incorrect selection fields.")
            
            elif error_code == 5:
                raise TooManyRequests("Requests are blocked for a small period of time because of too many requests per user (max 100 per minute).")
            
            elif error_code == 6:
                raise IncorrectID("Wrong ID value.")
            
            elif error_code == 7:
                raise InvalidIDRelation("A requested selection is private (For example, personal data of another user / faction).")
            
            elif error_code == 8:
                raise IPBlock("Current IP is banned for a small period of time because of abuse.")
            
            elif error_code == 9:
                raise APIDisabled("API is disabled for a small period of time because of abuse.")
            
            elif error_code == 10:
                raise FederalJail("User is in federal jail.")
            
            elif error_code == 11:
                raise KeyChangeError("Private key is changed in current request.")
            
            elif error_code == 12:
                raise KeyReadError("Private key is not read in current request.")
            
            elif error_code == 13:
                raise OwnerInactive("Owner is inactive.")
            
            elif error_code == 14:
                raise DailyReadLimit("Daily read limit reached.")
            
            elif error_code == 15:
                raise TemporaryError("Temporary error.")
            
            elif error_code == 16:
                raise LowAccessLevel("Access level is too low.")
            
            elif error_code == 17:
                raise BackendError("Backend error.")
            
            elif error_code == 18:
                raise KeyPaused("Key is paused.")
            
            
            else:
                raise OtherError("Unhandled error, shouldn't occur.")
            
        return data