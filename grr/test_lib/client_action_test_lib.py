#!/usr/bin/env python
"""Test classes for clients actions-related testing."""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from grr_response_client import client_actions
from grr_response_client.client_actions import registry_init


class WithAllClientActionsMixin(object):
  """Mixin that ensures that all client actions are registered."""

  def setUp(self):
    """Sets up the client actions registry."""

    super(WithAllClientActionsMixin, self).setUp()

    registry_copy = client_actions.REGISTRY.copy()
    registry_init.RegisterClientActions()

    def stop():
      for k in list(client_actions.REGISTRY.keys()):
        del client_actions.REGISTRY[k]

      for k, v in registry_copy.items():
        client_actions.REGISTRY[k] = v

    self.addCleanup(stop)
