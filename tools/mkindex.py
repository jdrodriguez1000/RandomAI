"""Genera el bloque de indice de los archivos de _persistence/.

Idempotente: reemplaza cualquier bloque <!--INDEX--> ... <!--/INDEX--> previo.
Los numeros de linea se miden en dos pasadas, sobre el resultado final.
Uso:  python mkindex.py <ruta_a__persistence>
"""
import re, sys, pathlib, unicodedata

D = pathlib.Path(sys.argv[1])
START, END = "<!--INDEX-->", "<!--/INDEX-->"

EJEMPLO = {"decisions.md": "D-02", "tasks.md": "TA-0002",
           "assumptions.md": "SUP-001", "constraints.md": "RES-001",
           "lessons.md": "L-002", "debt_tec.md": "DT-003",
           "progress.md": "Que sigue"}


def anchor(text):
    t = re.sub(r'`([^`]*)`', r'\1', text.strip())
    t = re.sub(r'\*\*([^*]*)\*\*', r'\1', t).lower()
    out = [c for c in t if c.isalnum() or c in ('-', ' ', '_')
           or unicodedata.category(c).startswith('L')]
    return ''.join(out).replace(' ', '-')


def plain(text):
    t = re.sub(r'`([^`]*)`', r'\1', text)
    return re.sub(r'\*\*([^*]*)\*\*', r'\1', t).strip()


def headings(lines):
    r = []
    for i, ln in enumerate(lines):
        m = re.match(r'^(#{2,3})\s+(.*)$', ln)
        if m and plain(m.group(2)).lower() != "indice" \
                and plain(m.group(2)).lower() != "índice":
            r.append((len(m.group(1)), plain(m.group(2)), anchor(m.group(2)), i + 1))
    return r


for f in sorted(D.glob("*.md")):
    lines = f.read_text(encoding="utf-8").split("\n")

    limpio, saltar = [], False
    for ln in lines:
        if ln.strip() == START:
            saltar = True
            continue
        if ln.strip() == END:
            saltar = False
            continue
        if not saltar:
            limpio.append(ln)
    lines = limpio

    hs = headings(lines)
    if not hs:
        print(f"{f.name}: sin encabezados, omitido")
        continue

    def build(nums):
        cod = EJEMPLO.get(f.name, "-")
        idx = [START, "", "## Índice", "",
               "> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea "
               "indicada (exacta, ya contando este índice).",
               f"> Por código: `grep -n '{cod}' {f.name}`", "",
               "| Línea | Sección | Ir a |", "|---|---|---|"]
        for (lvl, title, anc, _), n in zip(hs, nums):
            sang = "" if lvl == 2 else "&nbsp;&nbsp;↳ "
            b = "**" if lvl == 2 else ""
            idx.append(f"| `{n}` | {sang}{b}{title}{b} | [↓](#{anc}) |")
        return idx + ["", END]

    pos = next((i for i, ln in enumerate(lines)
                if ln.startswith("**Última actualización:**")), None)
    if pos is None:
        pos = next(i for i, ln in enumerate(lines) if ln.startswith("# "))

    tmp = lines[:pos + 1] + [""] + build([h[3] for h in hs]) + lines[pos + 1:]
    tmp = re.sub(r'\n{3,}', '\n\n', "\n".join(tmp)).split("\n")
    reales = [h[3] for h in headings(tmp)]
    assert len(reales) == len(hs), f"{f.name}: desajuste de encabezados"

    out = lines[:pos + 1] + [""] + build(reales) + lines[pos + 1:]
    txt = re.sub(r'\n{3,}', '\n\n', "\n".join(out))
    f.write_text(txt, encoding="utf-8")

    fin = txt.split("\n")
    ok = all(fin[n - 1].startswith("#") for n in [h[3] for h in headings(fin)])
    print(f"{f.name}: {len(hs)} entradas, lineas {'OK' if ok else 'ERROR'}")
