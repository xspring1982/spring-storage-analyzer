import io
import json
import os
import unittest
import importlib.util


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVER_PATH = os.path.join(ROOT, "scripts", "server.py")


def load_server_module():
    spec = importlib.util.spec_from_file_location("storage_report_server", SERVER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FakeHandlerMixin:
    def _send(self, code, body, ctype="application/json"):
        self.sent = {
            "code": code,
            "body": json.loads(body) if ctype == "application/json" else body,
        }


class ServerSafetyTest(unittest.TestCase):
    def setUp(self):
        self.server = load_server_module()
        self.app_path = "/Applications/Example.app"
        self.server.RM_ALLOW = {self.app_path}
        self.server.TRASH_ALLOW = {self.app_path}
        self.server.OPEN_ALLOW = {self.app_path}

    def make_handler(self, mode):
        class FakeHandler(FakeHandlerMixin, self.server.Handler):
            pass

        body = json.dumps({
            "token": self.server.TOKEN,
            "mode": mode,
            "paths": [self.app_path],
        }).encode("utf-8")
        handler = object.__new__(FakeHandler)
        handler.path = "/action"
        handler.headers = {
            "Host": "127.0.0.1",
            "Content-Length": str(len(body)),
        }
        handler.rfile = io.BytesIO(body)
        return handler

    def test_rm_rejects_applications_even_if_allowlisted(self):
        handler = self.make_handler("rm")

        handler.do_POST()

        self.assertEqual(handler.sent["code"], 403)
        self.assertIn("路径越界", handler.sent["body"]["error"])

    def test_trash_rejects_applications_even_if_allowlisted(self):
        handler = self.make_handler("trash")

        handler.do_POST()

        self.assertEqual(handler.sent["code"], 403)
        self.assertIn("路径越界", handler.sent["body"]["error"])

    def test_open_allows_applications_for_manual_uninstall(self):
        opened = []
        self.server.open_in_file_manager = opened.append
        handler = self.make_handler("open")

        handler.do_POST()

        self.assertEqual(handler.sent["code"], 200)
        self.assertEqual(opened, [self.app_path])


if __name__ == "__main__":
    unittest.main()
