from datetime import datetime
from django.test import TestCase
from landman.models import Well, WellStatus

# Create your tests here.

class WellTestCase(TestCase):
    def setUp(self) -> None:
        active_well_status = WellStatus.objects.create(code='A', description='Active')
        test_well = Well.objects.create(
            name='Test Well',
            status=active_well_status,
            latitude=0,
            longitude=0
        )

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_well_str(self):
        test_well = Well.objects.first()
        self.assertEqual(f"{test_well.name} ({test_well.status.description})", str(test_well))