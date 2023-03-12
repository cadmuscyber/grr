#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from absl.testing import absltest
from typing import Text

from grr_response_core.lib import rdfvalue
from grr_response_server.databases import db as abstract_db
from grr.test_lib import db_test_lib


class WithDatabaseTest(absltest.TestCase):

  def testDatabaseIsProvided(self):

    @db_test_lib.WithDatabase
    def TestMethod(db: abstract_db.Database):
      self.assertIsInstance(db, abstract_db.Database)

    TestMethod()  # pylint: disable=no-value-for-parameter

  def testDatabaseWorks(self):
    now = rdfvalue.RDFDatetime.Now()

    @db_test_lib.WithDatabase
    def TestMethod(self, db: abstract_db.Database):
      client_id = "C.0123456789abcdef"
      db.WriteClientMetadata(client_id, first_seen=now)

      client = db.ReadClientFullInfo(client_id)
      self.assertEqual(client.metadata.first_seen, now)

    TestMethod(self)  # pylint: disable=no-value-for-parameter

  def testDatabaseIsFresh(self):

    @db_test_lib.WithDatabase
    def TestMethod(db: abstract_db.Database):
      self.assertEqual(db.CountGRRUsers(), 0)

      db.WriteGRRUser("foo")
      self.assertEqual(db.CountGRRUsers(), 1)

    # We execute test method twice to ensure that each time the database is
    # really empty.
    TestMethod()  # pylint: disable=no-value-for-parameter
    TestMethod()  # pylint: disable=no-value-for-parameter

  def testPassesArguments(self):

    @db_test_lib.WithDatabase
    def TestMethod(self, username: Text, db: abstract_db.Database):
      db.WriteGRRUser(username)

      user = db.ReadGRRUser(username)
      self.assertEqual(user.username, username)

    TestMethod(self, "foo")  # pylint: disable=no-value-for-parameter
    TestMethod(self, "bar")  # pylint: disable=no-value-for-parameter


if __name__ == "__main__":
  absltest.main()
