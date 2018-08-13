""""""""Inheritance class""""""""""""""""""""

class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

my_file = open("text.txt", "r")
print (my_file.readline())
print (my_file.readline())

my_file.close()



# lloyd = {"wine": "Lloyd", "homework": [], "quizzes": [], "tests":[]}
# alice = {"name": "Alice", "homework": [], "quizzes": [], "tests": []}
# tyler = {"name": "Tyler", "homework": [], "quizzes": [], "tests":[]}
# #checks who paid more
