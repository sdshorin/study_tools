
# pip3 install genanki
# https://github.com/kerrickstaley/genanki
# https://apple.stackexchange.com/questions/209497/anki-latex-not-working-i-have-installed-basictex-dvipng
import genanki

INPUT_FILE = "input.tex"

with open(INPUT_FILE, "r") as f:
	latex_source = f.read()

latex_source.replace("\\begin{lemma}", "")


headers, document = latex_source.split("\\begin{document}")
headers += "\n\\begin{document}\n"


my_deck = genanki.Deck(
  258746587,
  'generated latex desk')

my_model = genanki.Model(
  167392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  	],
	latex_pre = headers)


while document.find("\\begin{theorem}") != -1:
	theorem_start = document.find("\\begin{theorem}")
	theorem_end = document.find("\\end{theorem}")
	proof_start = document.find("\\begin{proof}")
	proof_end = document.find("\\end{proof}")
	theorem = "[latex]" + document[theorem_start: theorem_end] + "\\end{theorem}\n[/latex]"
	proof = "[latex]" + document[proof_start: proof_end] + "\\end{proof}\n[/latex]"
	document = document[proof_end + 1:]

	# print("\n\n\n----THEOREM-----\n", theorem)
	# print("\n----PROOF-----\n", proof)
	my_note = genanki.Note(
  		model=my_model,
  		fields=[theorem, proof])

	my_deck.add_note(my_note)


genanki.Package(my_deck).write_to_file('output.apkg')

