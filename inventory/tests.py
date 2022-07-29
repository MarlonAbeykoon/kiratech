from unittest.mock import patch

from rest_framework import status
from rest_framework.test import APITestCase


class InventoryTests(APITestCase):
    @patch('inventory.views.TodoDetailApiView.get_data', return_value=[])
    def test_get_inventory_detail_by_id_api_returns_200_status_code(self, mock_get_data):
        """
        Ensure inventory details API returns a 200 status code.
        """
        url = '/inventory/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('requests.get')
    def test_inventory_page_returns_200_status_code(self, mock_get):
        """
        Ensure inventory page returns a 200 status code.
        """
        expected = {"inventories": []}
        mock_get.return_value.json.return_value = expected

        url = '/inventory/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('inventory.views.InventoryListApiView.get_data', return_value=[])
    @patch('inventory.serializers.InventorySerializer', return_value=[])
    def test_get_inventory_api_returns_200_status_code(self, mock_get_data, mock_serializer):
        """
        Ensure inventory API returns a 200 status code.
        """
        url = '/api/inventory/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
