from rich import print
from rich.progress import track


from rich.console import Console
from rich.table import Table

checked_element = u'\u2713'
non_checked_element = u'\u2717'

checked_style = 'green'
unchecked_style = 'red'

console = Console()

console.print("===Napari Plugin - Documentation Checklist===\n", style = 'blue')

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



