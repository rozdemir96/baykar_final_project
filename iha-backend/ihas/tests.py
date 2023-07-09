from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Ihas

class IhasViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = reverse('ihas_url')
        self.detail_url = reverse('ihas_url', kwargs={'id': 1})

    def test_get_ihas_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_ihas(self):
        data = {
            'marka': 'Test Marka',
            'model': 'Test Model',
            'agirlik': 1.5,
            'kategori': 'Test Kategori'
        }

        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ihas.objects.count(), 1)
        self.assertEqual(Ihas.objects.get().marka, 'Test Marka')

    def test_create_ihas_invalid_data(self):
        data = {
            'marka': '',  # Eksik veri girişi
            'model': 'Test Model',
            'agirlik': 'abc',  # Geçersiz veri girişi
            'kategori': 'Test Kategori'
        }

        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Ihas.objects.count(), 0)

    def test_update_ihas(self):
        ihas = Ihas.objects.create(
            marka='Eski Marka',
            model='Eski Model',
            agirlik=2.0,
            kategori='Eski Kategori'
        )

        data = {
            'marka': 'Yeni Marka',
            'model': 'Yeni Model',
            'agirlik': 1.8,
            'kategori': 'Yeni Kategori'
        }

        detail_url = reverse('ihas_url', kwargs={'id': ihas.id})
        response = self.client.put(detail_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ihas.objects.get(id=ihas.id).marka, 'Yeni Marka')

    def test_delete_ihas(self):
        ihas = Ihas.objects.create(
            marka='Test Marka',
            model='Test Model',
            agirlik=1.5,
            kategori='Test Kategori'
        )

        detail_url = reverse('ihas_url', kwargs={'id': ihas.id})
        response = self.client.delete(detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ihas.objects.count(), 0)
