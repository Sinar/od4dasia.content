# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from od4dasia.content.testing import OD4DASIA_CONTENT_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that od4dasia.content is properly installed."""

    layer = OD4DASIA_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if od4dasia.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'od4dasia.content'))

    def test_browserlayer(self):
        """Test that IOd4DasiaContentLayer is registered."""
        from od4dasia.content.interfaces import (
            IOd4DasiaContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IOd4DasiaContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = OD4DASIA_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['od4dasia.content'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if od4dasia.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'od4dasia.content'))

    def test_browserlayer_removed(self):
        """Test that IOd4DasiaContentLayer is removed."""
        from od4dasia.content.interfaces import \
            IOd4DasiaContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IOd4DasiaContentLayer,
            utils.registered_layers())
