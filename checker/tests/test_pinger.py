import pytest
from checker.Pinger import Pinger
import unittest

class TestPinger():
    @pytest.mark.parametrize('url', ['https://www.microsoft.com/'])
    def test_ping_url(self, url):
        pinger = Pinger()
        assert pinger.ping_site(url=url) == True
