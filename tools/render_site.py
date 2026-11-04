# -*- coding: utf-8 -*-
"""Render the GitHub Pages version of the daily brief.
Usage: python3 render_site.py TODAY_JSON [PAST_JSON ...] OUT_HTML
Stable favorites key 'aiBriefFavs', rich records, no cycle resets, optional export/import."""
import json, sys

def render(today_path, past_paths, out_path):
    today = json.load(open(today_path))
    archive = [json.load(open(p)) for p in past_paths]
    LABEL = today["label"]
    SECNAMES = {"ai":"AI","creative":"Creativita AI","videotech":"Video Tech","streaming":"Video Streaming"}
    data = {"today": today, "archive": archive, "secnames": SECNAMES}
    TPL = open("template.html", encoding="utf-8").read()
    html = (TPL.replace("__LABEL__", LABEL)
               .replace("__DATA__", json.dumps(data, ensure_ascii=False)))
    open(out_path, "w", encoding="utf-8").write(html)
    import os; print(out_path, os.path.getsize(out_path))

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2:-1], sys.argv[-1])
