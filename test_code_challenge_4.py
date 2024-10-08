import unittest
from code_challenge_4 import * 

class TestCodeChallenge3(unittest.TestCase):


  print("   IN TEST FILE    ")
  ################## List tests #######################


  def test_create_list(self):
    a = create_list()
    self.assertEqual(a, [])

  def test_append_list(self):
    a = append_list()
    print(a)
    self.assertEqual(len(a), 3)
    self.assertIsInstance(a[0], str)
    self.assertIsInstance(a[1], str)
    self.assertIsInstance(a[2], str)

  def test_copy_list(self):
    l = ['one','two','three']
    self.assertEqual(copy_list(l), l)

  def test_count_length(self):
    l = [15,11,43,32,11,23,11]
    self.assertEqual(count_list_length(l), l.count(11))
    self.assertEqual(count_list_length(l), 3)

  def test_sort_list(self):
    l = ["pear", "apple", "peaches", "pineapple", "bananas", "cherries", "oranges", "kiwi"]
    c = ["pear", "apple", "peaches", "pineapple", "bananas", "cherries", "oranges", "kiwi"]
    c.sort()
    self.assertEqual(sort_list(l), c)

  def test_reverse_list(self):
    l = ["pear", "apple", "peaches", "pineapple", "bananas", "cherries", "oranges", "kiwi"]
    a = ["pear", "apple", "peaches", "pineapple", "bananas", "cherries", "oranges", "kiwi"]
    a.sort()
    a.reverse()
    
    self.assertEqual(reverse_list(l), a)


  def test_insert_papaya(self):
    l = ["pear", "apple", "peaches", "pineapple", "bananas", "cherries", "oranges", "kiwi"]
    self.assertEqual(insert_papaya(l), ['pear', 'apple', 'papaya', 'peaches', 'pineapple', 'bananas', 'cherries', 'oranges', 'kiwi'])


  def test_pop_five_(self):
    l =  ['pear', 'apple', 'papaya', 'peaches', 'pineapple', 'bananas', 'cherries', 'oranges', 'kiwi']
    
    self.assertEqual(pop_five(l), ['pear', 'apple', 'papaya', 'peaches', 'bananas', 'cherries', 'oranges', 'kiwi'])


  def test_pop_element(self):
    l = ['pear', 'apple', 'papaya', 'peaches', 'pineapple', 'bananas', 'cherries', 'oranges', 'kiwi']

    self.assertEqual(pop_element(l,4), ['pear', 'apple', 'papaya', 'peaches', 'bananas', 'cherries', 'oranges', 'kiwi'])
                                    
    self.assertEqual(pop_element(l,2), ['pear', 'apple', 'peaches', 'pineapple', 'bananas', 'cherries', 'oranges', 'kiwi'])



  ###################  Dictionary Tests #######################
  def test_update_(self):
    myDict = {
      'Alabama': 'Southeast',
      'California': 'West',
      'Maine': 'New England',
      'Ohio': 'Midwest',
      'Arizona': 'South'
    }

    updatedDict = {
      'Alabama': 'Southeast',
      'California': 'West',
      'Maine': 'New England',
      'Ohio': 'Midwest',
      'Arizona': 'Southwest'
    }
    
    self.assertEqual(update_dict(myDict, 'Arizona', 'Southwest'),  updatedDict)


  def test_get_value(self):
    myDict = {
      'Alabama': 'Southeast',
      'California': 'West',
      'Maine': 'New England',
      'Ohio': 'Midwest',
      'Arizona': 'South'
    }

    self.assertEqual(get_value(myDict, 'Maine'), myDict['Maine'])

  def test_get_keys_(self):
    myDict = {
    'Alabama': 'Southeast',
    'California': 'West',
    'Maine': 'New England',
    'Ohio': 'Midwest',
    'Arizona': 'South'
    }
    self.assertEqual(get_keys(myDict), myDict.keys())


if __name__ == '__main__':
    unittest.main()