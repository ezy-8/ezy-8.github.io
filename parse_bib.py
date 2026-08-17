import re
import sys

bib_file = r'c:\Users\Ethan\Desktop\ezy-8.github.io\Papers\Exported Items.bib'
with open(bib_file, 'r', encoding='utf-8') as f: content = f.read()

entries = content.split('@')[1:]
html = []
html.append('<ul class="clean-list">')

for entry in entries:
    lines = entry.split('\n')
    entry_type_and_id = lines[0].strip()
    if '{' not in entry_type_and_id: continue
    
    fields = {}
    current_field = None
    current_value = ''
    for line in lines[1:]:
        line = line.strip()
        if not line or line == '}':
            if current_field: fields[current_field] = current_value.strip().strip(',').strip('}').strip('{').strip()
            continue
        match = re.match(r'^([a-zA-Z0-9_]+)\s*=\s*(.*)', line)
        if match:
            if current_field: fields[current_field] = current_value.strip().strip(',').strip('}').strip('{').strip()
            current_field = match.group(1).lower()
            current_value = match.group(2)
        else:
            if current_field: current_value += ' ' + line
    if current_field: fields[current_field] = current_value.strip().strip(',').strip('}').strip('{').strip()

    authors = fields.get('author', 'Unknown').replace('{', '').replace('}', '')
    author_list = authors.split(' and ')
    formatted_authors = []
    for a in author_list:
        parts = a.split(',')
        if len(parts) == 2:
            last = parts[0].strip()
            firsts = parts[1].strip().split()
            first_initials = ' '.join([f[0] + '.' for f in firsts if f])
            formatted_authors.append(f'{last}, {first_initials}')
        else:
            formatted_authors.append(a.strip())
    if len(formatted_authors) > 1:
        if len(formatted_authors) > 20:
             authors_str = ", ".join(formatted_authors[:19]) + ", ... " + formatted_authors[-1]
        else:
             authors_str = ", ".join(formatted_authors[:-1]) + ", & " + formatted_authors[-1]
    elif len(formatted_authors) == 1:
        authors_str = formatted_authors[0]
    else: authors_str = 'Unknown'

    year = fields.get('year', 'n.d.').strip('{}')
    title = fields.get('title', '').replace('{', '').replace('}', '')
    journal = fields.get('journal', fields.get('booktitle', fields.get('publisher', ''))).replace('{', '').replace('}', '')
    volume = fields.get('volume', '')
    issue = fields.get('number', '')
    pages = fields.get('pages', '').replace('--', '-')
    doi = fields.get('doi', '')

    apa = f'{authors_str} ({year}). {title}.'
    if journal:
        apa += f' <em>{journal}</em>'
        if volume: apa += f', <em>{volume}</em>'
        if issue: apa += f'({issue})'
        if pages: apa += f', {pages}.'
        else: apa += '.'
    if doi: apa += f' https://doi.org/{doi}'

    html.append(f'  <li>{apa}</li>')

html.append('</ul>')

output_path = r'c:\Users\Ethan\Desktop\ezy-8.github.io\Papers\parsed_apa.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))
