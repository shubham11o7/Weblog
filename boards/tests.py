from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home,board_topics
from .models import Board

# Create your tests here.

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django',description='its django')
        url = reverse(home)
        self.response = self.client.get(url)

    def test_home_view_get_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func,home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))