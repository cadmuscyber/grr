#!/usr/bin/env python

from absl import app
from absl.testing import absltest

from grr_response_server.databases import db_events_test
from grr_response_server.databases import mysql_test
from grr.test_lib import test_lib


class MysqlEventsTest(db_events_test.DatabaseTestEventsMixin,
                      mysql_test.MysqlTestBase, absltest.TestCase):
  pass


if __name__ == "__main__":
  app.run(test_lib.main)
