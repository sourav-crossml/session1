from django.test import TestCase
from .models import candidate_data


class CandidateDataTest(TestCase):

    '''
        this class is created to test the post method. 
        we will create a post from here and check the response.
    '''

    def setUp(self):
        self.candidate_data = candidate_data()

        def test_details(self):
            # response = self.candidate_data.get('/details/')
            # self.assertEqual(response, 200)

            response = self.candidate_data.post('/', {'candidate_name':'Abc', 'resume_portfolio_link':'http://abc.com', 'primary_skills':'Ruby','secondary_skills':'html', 'candidate_experince':2})
            self.assertEqual(response, 200)