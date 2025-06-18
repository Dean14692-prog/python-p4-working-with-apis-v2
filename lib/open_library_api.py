import requests
import json


class Search:

    def get_search_results(self):
        # Fixed search term
        search_term = "the lord of the rings"

        # Format the search term for use in a URL (spaces become +)
        search_term_formatted = search_term.replace(" ", "+")

        # Specify fields to include in the response
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        # Construct the API endpoint URL
        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        # Make GET request to the API
        response = requests.get(URL)

        # Return raw content (bytes)
        return response.content

    def get_search_results_json(self):
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        print("Requesting URL:", URL)

        response = requests.get(URL)

        # Return JSON-parsed response (Python dict)
        return response.json()

    def get_user_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL).json()

        # Check if any results were found
        if response["docs"]:
            title = response["docs"][0].get("title", "No title available")
            author = response["docs"][0].get("author_name", ["Unknown author"])[0]
            response_formatted = f"Title: {title}\nAuthor: {author}"
        else:
            response_formatted = "No results found for your search."

        return response_formatted


# -------- Uncomment any one of the following for testing --------

# 1. Raw byte output
# results = Search().get_search_results()
# print(results)

# 2. Nicely formatted JSON output
# results_json = Search().get_search_results_json()
# print(json.dumps(results_json, indent=1))

# 3. Dynamic user input
search_term = input("Enter a book title: ")
result = Search().get_user_search_results(search_term)
print("\nSearch Result:\n")
print(result)
