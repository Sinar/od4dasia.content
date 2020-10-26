# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import od4dasia.content


class Od4DasiaContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=od4dasia.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'od4dasia.content:default')


OD4DASIA_CONTENT_FIXTURE = Od4DasiaContentLayer()


OD4DASIA_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(OD4DASIA_CONTENT_FIXTURE,),
    name='Od4DasiaContentLayer:IntegrationTesting',
)


OD4DASIA_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OD4DASIA_CONTENT_FIXTURE,),
    name='Od4DasiaContentLayer:FunctionalTesting',
)


OD4DASIA_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        OD4DASIA_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='Od4DasiaContentLayer:AcceptanceTesting',
)
