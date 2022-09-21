from django.test import TestCase
from mywatchlist.models import MyWatchList

# Create your tests here.
class MyWatchListTesting(TestCase):
    def sendTesting(self):
        MyWatchList.objects.create(watched="Yes", title="Direktur Sombong Meninggal Tergelircir ke Sumur", rating="9/10", 
            release_date="12 Juni 2022", review="Banyak nilai moralnya dan sangat menarik perhatian penonton khususnya ibu rumah tangga.")

    def testAtributtes(self):
        sinetron = MyWatchList.objects.get(watched="Yes", title="Direktur Sombong Meninggal Tergelircir ke Sumur", rating="9/10", 
            release_date="12 Juni 2022", review="Banyak nilai moralnya dan sangat menarik perhatian penonton khususnya ibu rumah tangga.")
        
        self.assertEqual(sinetron.watched, "Yes")
        self.assertEqual(sinetron.title, "Direktur Sombong Meninggal Tergelircir ke Sumur")
        self.assertEqual(sinetron.rating, "9/10")
        self.assertEqual(sinetron.release_date, "12 Juni 2022")
        self.assertEqual(sinetron.review, "Banyak nilai moralnya dan sangat menarik perhatian penonton khususnya ibu rumah tangga.")
