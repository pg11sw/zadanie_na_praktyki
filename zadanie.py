import requests

nr_file = open("nr.txt", 'r')
numbers = []

for line in nr_file.readlines():
    numbers.append(line.strip())

print(numbers)

def get_image_link(nr):
    response = requests.get(f"https://xkcd.com/{nr}/info.0.json")
    if response.status_code == 200:
        return response.json()["img"]
    else:
        return None

numers_with_links = {}
for number in numbers:
    link = get_image_link(number)
    if link:
        print(f"Obrazek nr {number}: {link}")
        numers_with_links[number] = link
    else:
        print(f"Nie udało się załadować linku obrazka nr {number}")

html = ''''''
for number, link in numers_with_links.items():
    html += f'''
    <div class="px-4 pt-5 my-5 text-center border-bottom">
      <h1 class="display-4 text-body-emphasis">Obrazek nr {number}</h1>
      <div class="col-lg-6 mx-auto">
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center mb-5">
        </div>
      </div>
    <div class="overflow-hidden">
      <div class="container px-5">
        <img src={link} class="img-fluid border rounded-3 shadow-lg mb-4" width=50% alt="Example image" loading="lazy">
      </div>
    </div>
  </div>

  <div class="b-example-divider"></div>
'''
html_template_file = open("heroes/index.html", 'r')
html_template = html_template_file.read()

new_html = html_template.replace("images_to_be_placed", html)

new_html_file = open("heroes/obrazki.html", "w")
new_html_file.write(new_html)
