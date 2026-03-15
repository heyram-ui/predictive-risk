import ast, os, re

src = open('app.py', encoding='utf-8').read()
try:
    ast.parse(src)
    print('[OK] app.py syntax valid')
except SyntaxError as e:
    print(f'[SYNTAX ERROR] {e}')

used = [m.group(1) for m in re.finditer(r"render_template\(['\"]([^'\"]+)['\"]", src)]
print(f'\nTemplates referenced in app.py: {len(used)}')

all_html = []
for root, dirs, files in os.walk('templates'):
    for f in files:
        if f.endswith('.html'):
            rel = os.path.join(root, f).replace('\\', '/').replace('templates/', '', 1)
            all_html.append(rel)

print(f'Total HTML files: {len(all_html)}\n')
print('=== TEMPLATE USAGE ===')
for h in sorted(all_html):
    is_used = any(h in u or h.replace('/', '\\') in u for u in used)
    print(('[USED]   ' if is_used else '[UNUSED] ') + h)

print('\n=== ROOT PYTHON FILES ===')
for f in sorted(os.listdir('.')):
    if f.endswith('.py') and f not in ['app.py', 'train_ml.py']:
        imported = f.replace('.py', '') in src
        print(('[USED]     ' if imported else '[NOT USED] ') + f)
