"""
-----------
Quota tests
-----------
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):
    """Tests for admin only."""

    @pytest.mark.idempotent_id('5b2ce43c-924c-4bae-bac0-f5d6ed69d72e')
    def test_update_defaults(self, update_defaults):
        """**Scenario:** Verify that admin can update default quotas.

        **Steps:**

        #. Update ``volumes`` parameter using UI

        **Teardown:**

        #. Restore original value for ``volumes`` parameter
        """
        update_defaults({'volumes': 100000})
