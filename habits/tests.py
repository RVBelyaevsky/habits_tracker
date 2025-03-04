from rest_framework import status
from rest_framework.test import APITestCase


class HabitsTestCase(APITestCase):
    def setUp(self):
        pass

    def test_list_habits(self):
        """Тестирование списка привычек."""

        response = self.client.get("/habits/public/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(), {"count": 0, "next": None, "previous": None, "results": []}
        )
