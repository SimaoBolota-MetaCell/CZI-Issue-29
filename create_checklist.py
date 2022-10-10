from rich import print
from rich.progress import track


from rich.console import Console
from rich.table import Table

checked_element = u'\u2713'
non_checked_element = u'\u2717'

checked_style = 'green'
unchecked_style = 'red'

table = Table(title="Napari Documentation Checklist")

table.add_column("Author Names", justify="right", style=checked_style, no_wrap=True)
table.add_column("Summary Sentence", justify="right", style=unchecked_style)
table.add_column("Intro Paragraph", justify="right", style="green")
table.add_column("Intro Video/Screenshot", justify="right", style=unchecked_style)
table.add_column("Usage Overview", justify="right", style=unchecked_style)
table.add_column("Source Code Link", justify="right", style=checked_style)
table.add_column("Support Channel Link", justify="right", style="green")
table.add_column("Issue Submission Link", justify="right", style="green")
table.add_column("Display Name", justify="right", style="green")

table.add_row(checked_element, non_checked_element, checked_element, non_checked_element, non_checked_element,checked_element ,checked_element,checked_element,checked_element )

console = Console()
console.print(table, justify="center")




console.print("=========DOCUMENTATION CHECKLIST============\n", style = 'blue')

console.print('- Author name ' u'\u2713', style = "green")
console.print('- Summary Sentence ' u'\u2713', style = "green")
console.print('- Intro Paragraph ' u'\u2717', style = "red")
console.print('- Intro Video ' u'\u2717', style = "red")
console.print('- Intro Screenshot ' u'\u2717', style = "red")
console.print('- Usage Overview ' u'\u2713', style = "green")
console.print('- Source Code Link ' u'\u2713', style = "green")
console.print('- Support Channel Link ' u'\u2717', style = "red")
console.print('- Issue Submission Link ' u'\u2717', style = "red")
console.print('- Display Name ' u'\u2713', style = "green")



