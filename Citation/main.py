import calendar
from metaphor_python import Metaphor
from datetime import datetime

#Below Method to convert date format
def convert_date(date_string):
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    month_number = date_obj.month
    month_name = calendar.month_name[month_number]

    new_date_format = date_obj.strftime("%d {} %Y".format(month_name))

    return  new_date_format


def get_citation(citation_string):
    METAPHOR_API_KEY ="METAPHOR_API_KEY"# replace METAPHOR_API_KEY
    metaphor = Metaphor(METAPHOR_API_KEY)

    response = metaphor.search(
          citation_string,
          num_results=10,
          use_autoprompt=True,
        )
    current_date = datetime.now().strftime("%Y-%m-%d")
    converted_current_date = convert_date(current_date)
    print(f"Citation Format")
    print(f"Author. Title, Published Date, URL ,Accessed on")
    print("\n")
    for result in response.results:
        if result.published_date:
            converted_date = convert_date(result.published_date)
        else:
            converted_date = "None"
        print(f"{result.author}. {result.title}, {converted_date}, {result.url} ,Accessed {converted_current_date}")

get_citation("AI")
