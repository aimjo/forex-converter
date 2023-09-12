### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  ### Javascript: uses {} to define code blocks

  ### python: used indentation for code blocks

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you can try to get a missing key (like "c") _without_ your programming crashing.

      my_dict = {"a": 1, "b": 2}
      result = my_dict.get("c", "Key not found")

      or

      my_dict = {"a": 1, "b": 2}

      if "c" in my_dict:
          result = my_dict["c"]
      else:
          result = "Key not found"

- What is a unit test?

  ### it's a way to test individual components of code to make sure the code works

- What is an integration test?

  ### it's a way to verify that the code works together

- What is the role of web application framework, like Flask?

  ### it provides a way to build, deploy and maintain software or databases

- You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?

  ### 'foods?type=pretzel' lets you pass paramaters without affecting the url structure and without hard coding it

- How do you collect data from a URL placeholder parameter using Flask?

      @app.route('/foods/<food_name>')
      def get_food(food_name):
          return f"You selected food: {food_name}"

- How do you collect data from the query string using Flask?

      @app.route('/search')
      def search():
          query = request.args.get('q')
          page = request.args.get('page')

          result = f'Search Query: {query}, Page: {page}'
          return result

- How do you collect data from the body of the request using Flask?

      @app.route('/submit', methods=['POST'])
      def submit():
          request_data = request.data
          form_data = request.form

          result = f'Request Data: {request_data}, Form Data: {form_data}'
          return result

- What is a cookie and what kinds of things are they commonly used for?

  stores user specific data to let the user personalize their settings or experience

- What is the session object in Flask?

  its a way to track info for a specific user, such as authentication

- What does Flask's `jsonify()` do?

  turns python dictionaries into Json
