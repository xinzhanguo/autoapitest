import hashlib
import requests


class Browser:
    """Simulate browser request.
    :headers request headers
    :resp response
    """
    headers = None  # request headers
    resp = None  # response
    name = None  # name

    def __init__(self, headers=None):
        self.headers = headers

    def get(self, url, name: str, headers=None):
        """get request"""
        self.name = name
        data = None
        _headers = self.headers
        if headers is not None:
            _headers = headers
        self.resp = requests.get(
            url, params=data, headers=_headers, timeout=10)
        print(name, self.resp.elapsed.microseconds, url)
        return self

    def want_header(self, key: str, value: str):
        """want_header check header value."""
        got_value = self.resp.headers[key]
        if got_value != value:
            raise ValueError(
                f"{self.name} header {key} not eq want:{value}, but:{got_value}")
        print(self.name, f"{key} ok")
        return self

    def want_status(self, status_code: int):
        """want_status check status code."""
        got_value = int(self.resp.status_code)
        if got_value != int(status_code):
            raise ValueError(
                f"{self.name} status not eq want:{status_code}, but:{got_value}")
        print(self.name, "status ok")
        return self

    def want_length(self, content_length: int):
        """want_length check coentent length."""
        got_value = int(self.resp.headers['Content-Length'])
        if got_value != int(content_length):
            raise ValueError(
                f"{self.name} content length not eq want:{content_length}, but:{got_value}")
        print(self.name, "content ok")
        return self

    def want_type(self, content_type: str):
        """want_type check coentent type."""
        got_value = self.resp.headers['Content-Type']
        if got_value != content_type:
            raise ValueError(
                f"{self.name} content type not eq want:{content_type}, but:{got_value}")
        print(self.name, "type ok")
        return self

    def want_md5(self, md5val):
        """want_md5 check coentent md5."""
        got_value = hashlib.md5(self.resp.content).hexdigest()
        if got_value != md5val:
            raise ValueError(
                f"{self.name} content type not eq want:{md5val}, but:{got_value}")
        print(self.name, "md5 ok")
        return self

    """you also cant define your self check code ..."""

    def want(self, wants: dict):
        """want check."""
        for key in wants.keys():
            if key == "md5":
                self.want_md5(wants[key])
            elif key == "type":
                self.want_type(wants[key])
            elif key == "length":
                self.want_length(wants[key])
            elif key == "status":
                self.want_status(wants[key])
            else:
                self.want_header(key, wants[key])
