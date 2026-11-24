# -*- coding: utf-8 -*-
"""从 data/units/*.json 与 sources.json 生成 site/ 静态站点（纯 HTML+CSS）。"""
import html
import json
import os
import re
from collections import Counter, defaultdict
from datetime import date

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = os.path.join(ROOT, "site")
TODAY = "2026-11-24"
DISCLAIMER = "本站内容仅供学习参考，不构成法律意见；法律会修订，具体问题请咨询执业律师或查阅官方现行文本。"

NAV = [
    ("index.html", "首页"),
    ("units.html", "部门法"),
    ("index-all.html", "全部条目"),
    ("cases.html", "案例"),
    ("laws.html", "法律文本"),
    ("flows.html", "程序流程"),
    ("timeline.html", "时间线"),
    ("sources.html", "来源"),
    ("coverage.html", "覆盖"),
    ("about.html", "关于"),
]

TYPE_LABEL = {"concept": "概念制度", "case": "案例", "law": "文本导读", "flow": "流程"}
IMP_CLASS = {"核心": "badge-core", "重要": "badge-imp", "补充": "badge-sup"}
LEVEL_CLASS = {"L1": "badge-l1", "L2": "badge-l2", "L3": "badge-l3"}


def esc(s):
    return html.escape(str(s or ""), quote=True)


def load():
    units = []
    for i in range(1, 12):
        p = os.path.join(ROOT, "data", "units", f"u{i:02d}.json")
        units.append(json.load(open(p, encoding="utf-8")))
    sources = json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"]
    coverage = json.load(open(os.path.join(ROOT, "coverage.json"), encoding="utf-8"))
    entries = []
    for u in units:
        for e in u["entries"]:
            e["_unit"] = u
            entries.append(e)
    by_id = {e["id"]: e for e in entries}
    return units, entries, by_id, sources, coverage


def wrap_text(text, limit=30):
    text = str(text or "")
    lines = []
    cur = ""
    for ch in text:
        if len(cur) >= limit:
            lines.append(cur)
            cur = ch
        else:
            cur += ch
    if cur:
        lines.append(cur)
    return lines


def box_svg(title, items, width=760, height=None):
    """竖向要件/流程框图，输出合法 SVG。"""
    n = max(1, len(items))
    row_h = 74
    top = 72
    h = height or (top + n * row_h + 20)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {h}" role="img" aria-label="{esc(title)}">',
             f'<text x="{width/2}" y="34" text-anchor="middle" font-size="18" font-weight="600" fill="var(--ink)">{esc(title)}</text>']
    for i, item in enumerate(items):
        y = top + i * row_h
        parts.append(f'<rect x="90" y="{y}" width="{width-180}" height="48" rx="8" fill="var(--paper-2)" stroke="var(--line)" stroke-width="1.5"/>')
        parts.append(f'<text x="{width/2}" y="{y+30}" text-anchor="middle" font-size="15" fill="var(--ink)">{esc(item)}</text>')
        if i < n - 1:
            parts.append(f'<line x1="{width/2}" y1="{y+48}" x2="{width/2}" y2="{y+row_h}" stroke="var(--accent)" stroke-width="2"/>')
            parts.append(f'<path d="M {width/2-5} {y+row_h-7} L {width/2} {y+row_h-1} L {width/2+5} {y+row_h-7}" fill="none" stroke="var(--accent)" stroke-width="2"/>')
    parts.append("</svg>")
    return "".join(parts)


def layered_svg(title, layers):
    """分层结构图：layers = [(label, [items])]"""
    width = 760
    h = 80 + len(layers) * 96
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {h}" role="img" aria-label="{esc(title)}">',
             f'<text x="{width/2}" y="34" text-anchor="middle" font-size="18" font-weight="600" fill="var(--ink)">{esc(title)}</text>']
    for i, (label, items) in enumerate(layers):
        y = 58 + i * 96
        parts.append(f'<rect x="60" y="{y}" width="{width-120}" height="70" rx="10" fill="var(--paper-2)" stroke="var(--line)"/>')
        parts.append(f'<text x="80" y="{y+24}" font-size="14" font-weight="700" fill="var(--accent)">{esc(label)}</text>')
        parts.append(f'<text x="80" y="{y+50}" font-size="14" fill="var(--ink)">{esc(" · ".join(items))}</text>')
        if i < len(layers) - 1:
            parts.append(f'<line x1="{width/2}" y1="{y+70}" x2="{width/2}" y2="{y+96}" stroke="var(--accent)" stroke-width="2"/>')
    parts.append("</svg>")
    return "".join(parts)


def page(title, body, depth=1, active="", extra_head=""):
    nav = "".join(f'<a href="{href}" class="{"active" if href == active else ""}">{esc(label)}</a>' for href, label in NAV)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — 法律知识库</title>
<link rel="stylesheet" href="style.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">跳到正文</a>
<header class="site-header">
  <div class="masthead">
    <a class="brand" href="index.html"><span class="brand-mark">法</span><span class="brand-text"><strong>法律知识库</strong><small>体系 · 制度 · 经典案例</small></span></a>
    <nav class="main-nav" aria-label="主导航">{nav}</nav>
  </div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site-footer">
  <p class="disclaimer">{esc(DISCLAIMER)}</p>
  <p class="meta">法律知识库 · 数据驱动静态站点 · 最后核对 {TODAY} · <a href="about.html">方法与边界</a></p>
</footer>
</body>
</html>
"""


def badge(e):
    return (f'<span class="badge {IMP_CLASS.get(e["importance"], "")}">{esc(e["importance"])}</span>'
            f'<span class="badge {LEVEL_CLASS.get(e.get("status", "L1"), "")}">{esc(e.get("status", "L1"))}</span>'
            f'<span class="badge badge-type">{esc(TYPE_LABEL[e["type"]])}</span>'
            f'<span class="badge badge-juris">{esc(e["jurisdiction"])}</span>')


def entry_card(e):
    return f"""<article class="entry-card">
  <div class="entry-head"><h3><a href="entry-{esc(e['id'])}.html">{esc(e['title'])}</a></h3><div class="badges">{badge(e)}</div></div>
  <p class="entry-def">{esc(e['definition'])}</p>
  <p class="entry-meta">{esc(e['era'])}</p>
</article>"""


def render_index(units, entries, sources, coverage):
    lv = coverage["levels"]
    core = [e for e in entries if e["importance"] == "核心"]
    core.sort(key=lambda e: (e["_unit"]["order"], e["title"]))
    unit_cards = "".join(
        f"""<a class="unit-card" href="unit-{u['unit_id']}.html">
  <span class="unit-num">{u['order']:02d}</span>
  <h3>{esc(u['title'])}</h3>
  <p>{esc(u['subtitle'])}</p>
  <span class="unit-count">{len(u['entries'])} 条</span>
</a>""" for u in units)
    body = f"""
<section class="hero">
  <div class="hero-copy">
    <p class="kicker">体系 · 制度 · 经典案例</p>
    <h1>把法律知识，整理成一张可以查阅的地图</h1>
    <p class="lede">从法理与法律史，到宪法、民法、刑法、程序法、商法、社会法、知识产权、环境法与数据法，再到比较法、国际法与经典案例。每个条目标明辖区、层级与来源；查不到的内容，宁可写“待核实”。</p>
    <div class="hero-actions"><a class="btn primary" href="units.html">进入部门法</a><a class="btn" href="index-all.html">全部条目</a><a class="btn ghost" href="about.html">方法与边界</a></div>
  </div>
  <div class="hero-stats">
    <div class="stat"><strong>{coverage['total']}</strong><span>条目</span></div>
    <div class="stat"><strong>{len(units)}</strong><span>单元</span></div>
    <div class="stat"><strong>{sum(1 for s in sources if s.get('verified'))}</strong><span>已核验来源</span></div>
    <div class="stat"><strong>{lv.get('L2',0)+lv.get('L3',0)}</strong><span>L2/L3 深写</span></div>
  </div>
</section>
<section class="section">
  <div class="section-head"><h2>部门法地图</h2><p>按法学知识体系划分，先骨架后深写。</p></div>
  <div class="unit-grid">{unit_cards}</div>
</section>
<section class="section">
  <div class="section-head"><h2>核心条目</h2><p>全部核心条目已达到 L2 及以上；其中少量条目进入 L3 深度研读。</p></div>
  <div class="entry-grid">{''.join(entry_card(e) for e in core[:12])}</div>
  <p class="more"><a href="index-all.html">查看全部 {coverage['total']} 条 →</a></p>
</section>
<section class="section two-col">
  <div class="panel"><h2>怎样使用</h2><ol class="clean"><li>从「部门法」进入，先看 L1 骨架。</li><li>核心条目读 L2 的固定结构：定义、要件、效果、例外、争议、图示。</li><li>看案例时先读“争议焦点”，再看“裁判理由”和“意义”。</li><li>引用前请核对页末来源与“待核实”提示。</li></ol></div>
  <div class="panel"><h2>诚实标注</h2><p>本库把“法律条文、司法解释、指导性案例、学说观点、实务经验”分开标注；对无法核实的案号、日期与条文号，统一写“待核实”，不凭记忆补全。</p><p><a href="coverage.html">查看覆盖矩阵 →</a></p></div>
</section>
"""
    return page("首页", body, active="index.html")


def render_units(units):
    rows = "".join(f"""<tr><td><a href="unit-{u['unit_id']}.html">{esc(u['title'])}</a></td><td>{len(u['entries'])}</td><td>{esc(u['subtitle'])}</td></tr>""" for u in units)
    body = f"""<div class="page-head"><p class="kicker">部门法</p><h1>十一个单元</h1><p>按“法理—公法—民法—刑法—程序—商法社会法—知识产权环境数据—比较法国际法—案例—文本—流程”的顺序组织。</p></div>
<table class="data-table"><thead><tr><th>单元</th><th>条目数</th><th>说明</th></tr></thead><tbody>{rows}</tbody></table>"""
    return page("部门法", body, active="units.html")


def render_unit(u):
    groups = [("核心", "核心条目"), ("重要", "重要条目"), ("补充", "补充条目")]
    sections = []
    for key, label in groups:
        es = [e for e in u["entries"] if e["importance"] == key]
        if es:
            sections.append(f"<h2>{label}（{len(es)}）</h2><div class='entry-grid'>{''.join(entry_card(e) for e in es)}</div>")
    body = f"""<div class="page-head"><p class="kicker">单元 {u['order']:02d}</p><h1>{esc(u['title'])}</h1><p>{esc(u['subtitle'])}</p><p class="muted">共 {len(u['entries'])} 条 · 核心 {sum(1 for e in u['entries'] if e['importance']=='核心')} 条</p></div>
{''.join(sections)}
<p class="more"><a href="units.html">← 返回部门法</a></p>"""
    return page(u["title"], body, active="units.html")


def related_html(e, by_id):
    links = []
    for rid in e.get("related", []):
        r = by_id.get(rid)
        if r:
            links.append(f'<a href="entry-{esc(rid)}.html">{esc(r["title"])}</a>')
    return "、".join(links) if links else "（暂无）"


def sources_html(e, source_map):
    items = []
    for sid in e.get("sources", []):
        s = source_map.get(sid)
        if not s:
            continue
        link = f'<a href="{esc(s["url"])}" target="_blank" rel="noopener noreferrer">{esc(s["title"])}</a>' if s.get("url") else esc(s["title"])
        status = "已核验" if s.get("verified") else "待核验"
        items.append(f"<li>{link} <span class='muted'>· {esc(s.get('author',''))} · {esc(s.get('year',''))} · {esc(s.get('type',''))} · {status}</span></li>")
    return "<ul class='source-list'>" + "".join(items) + "</ul>" if items else "<p class='muted'>暂无来源。</p>"


def render_concept(e, by_id, source_map):
    if not e.get("l2"):
        body = f"""<div class="page-head"><p class="kicker">{esc(e['_unit']['title'])} · {esc(TYPE_LABEL[e['type']])}</p><h1>{esc(e['title'])}</h1><div class="badges">{badge(e)}</div></div>
<article class="prose">
<section><h2>定义</h2><p class="lead">{esc(e['definition'])}</p></section>
<section><h2>时间或位置</h2><p>{esc(e['era'])}</p></section>
<section><h2>概述</h2><p>{esc(e['summary'])}</p></section>
<section><h2>相关条目</h2><p>{related_html(e, by_id)}</p></section>
<section><h2>来源</h2>{sources_html(e, source_map)}</section>
<section><h2>待核实</h2><p>{esc(e.get('pending_notes') or '无。')}</p></section>
</article>"""
        return page(e["title"], body, active="units.html")

    l2 = e["l2"]
    def ul(key):
        vals = l2.get(key) or []
        return "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in vals) + "</ul>" if vals else "<p class='muted'>暂无。</p>"

    cases = []
    for cid in l2.get("cases", []):
        c = by_id.get(cid)
        if c:
            cases.append(f'<li><a href="entry-{esc(cid)}.html">{esc(c["title"])}</a></li>')
    case_html = "<ul>" + "".join(cases) + "</ul>" if cases else "<p class='muted'>暂无已核实案例；相关案例类型见案例单元。</p>"

    contro = ""
    for c in l2.get("controversies", []):
        views = "".join(f"<li><strong>{esc(v.get('holder',''))}</strong>：{esc(v.get('basis',''))}</li>" for v in c.get("views", []))
        contro += f"<div class='debate'><h3>{esc(c.get('issue',''))}</h3><ul>{views}</ul></div>"
    contro = contro or "<p class='muted'>暂未整理出重大争议。</p>"

    dist = "".join(f"<li><strong>与{esc(d.get('with',''))}的区别</strong>：{esc(d.get('difference',''))}</li>" for d in l2.get("distinctions", []))
    mis = "".join(f"<li><strong>误解：</strong>{esc(m.get('claim',''))}<br><span class='muted'>纠正：{esc(m.get('correction',''))}</span></li>" for m in l2.get("misconceptions", []))
    diagram = box_svg(f"{e['title']} · 要件结构", l2.get("elements", []))
    l3_html = ""
    if e.get("l3"):
        l3 = e["l3"]
        paras = "".join(f"<p>{esc(p)}</p>" for p in l3.get("paragraphs", []))
        data = "".join(f"<li><strong>{esc(d.get('label',''))}</strong>：{esc(d.get('value',''))} <span class='muted'>{esc(d.get('note',''))}</span></li>" for d in l3.get("data", []))
        l3_html = f"<section class='deep'><h2>{esc(l3.get('title','深度研读'))}</h2>{paras}{('<ul>'+data+'</ul>') if data else ''}</section>"

    body = f"""<div class="page-head"><p class="kicker">{esc(e['_unit']['title'])} · {esc(TYPE_LABEL[e['type']])}</p><h1>{esc(e['title'])}</h1><div class="badges">{badge(e)}</div><p class="lead">{esc(e['definition'])}</p></div>
<article class="prose structured">
<section><h2>1. 定义与出处</h2><p>{esc(l2.get('definition_source',''))}</p></section>
<section><h2>2. 构成要件</h2>{ul('elements')}</section>
<section><h2>3. 适用条件</h2>{ul('conditions')}</section>
<section><h2>4. 法律效果</h2>{ul('effects')}</section>
<section><h2>5. 例外与限制</h2>{ul('exceptions')}</section>
<section><h2>6. 典型案例</h2>{case_html}</section>
<section><h2>7. 学说争议与实务分歧</h2>{contro}</section>
<section><h2>8. 与相近制度的区别</h2><ul>{dist}</ul></section>
<section><h2>9. 常见误解</h2><ul>{mis}</ul></section>
<section><h2>10. 一图</h2><figure class="diagram">{diagram}</figure></section>
<section><h2>11. 待核实</h2><p>{esc(e.get('pending_notes') or '无。')}</p></section>
{l3_html}
<section><h2>相关条目</h2><p>{related_html(e, by_id)}</p></section>
<section><h2>来源</h2>{sources_html(e, source_map)}</section>
</article>"""
    return page(e["title"], body, active="units.html")


def render_case(e, by_id, source_map):
    c = e.get("case") or {}
    rows = [
        ("案由", c.get("cause")), ("法院", c.get("court")), ("案号 / 引注", c.get("case_no")),
        ("裁判日期", c.get("date")), ("基本事实", c.get("facts")), ("争议焦点", c.get("issue")),
        ("裁判理由", c.get("reasoning")), ("裁判结果", c.get("result")),
        ("意义与评论", c.get("significance")), ("评论者", c.get("commentator")),
    ]
    table = "".join(f"<tr><th>{esc(k)}</th><td>{esc(v or '待核实')}</td></tr>" for k, v in rows)
    extra = ""
    if c.get("citation"):
        extra = f"<p class='citation'>引注：{esc(c['citation'])}</p>"
    l2_html = ""
    if e.get("l2"):
        l2 = e["l2"]
        l2_html = "<section class='deep'><h2>规范与学理分析</h2>"
        l2_html += f"<p>{esc(l2.get('definition_source',''))}</p>"
        for key, label in [("elements","分析维度"),("conditions","认定条件"),("effects","法律效果"),("exceptions","例外与限制")]:
            vals = l2.get(key) or []
            if vals:
                l2_html += f"<h3>{label}</h3><ul>" + "".join(f"<li>{esc(x)}</li>" for x in vals) + "</ul>"
        l2_html += "</section>"
    body = f"""<div class="page-head"><p class="kicker">{esc(e['_unit']['title'])} · 案例</p><h1>{esc(e['title'])}</h1><div class="badges">{badge(e)}</div><p class="lead">{esc(e['definition'])}</p></div>
<article class="prose">
<table class="case-table">{table}</table>
{extra}
{l2_html}
<section><h2>待核实</h2><p>{esc(e.get('pending_notes') or '无。')}</p></section>
<section><h2>相关条目</h2><p>{related_html(e, by_id)}</p></section>
<section><h2>来源链接</h2>{sources_html(e, source_map)}</section>
</article>"""
    return page(e["title"], body, active="cases.html")


def render_law(e, by_id, source_map):
    l = e.get("law") or {}
    structure = "".join(f"<tr><th>{esc(x.get('name',''))}</th><td>{esc(x.get('content',''))}</td></tr>" for x in l.get("structure", []))
    articles = "".join(f"<li><strong>{esc(x.get('article',''))}</strong>：{esc(x.get('content',''))}</li>" for x in l.get("key_articles", []))
    amendments = "".join(f"<li>{esc(x)}</li>" for x in l.get("amendments", []))
    interp = "".join(f"<li>{esc(x)}</li>" for x in l.get("interpretations", []))
    meta = f"""<div class="law-meta"><span>状态：{esc(l.get('status',''))}</span><span>版本：{esc(l.get('version',''))}</span><span>施行：{esc(l.get('effective_date',''))}</span><span>核对：{esc(l.get('checked_date',''))}</span></div>"""
    diagram = layered_svg(f"{e['title']} · 结构图", [(x.get("name", ""), [str(x.get("content", ""))[:18] + ("…" if len(str(x.get("content", ""))) > 18 else "")]) for x in l.get("structure", [])[:6]]) if l.get("structure") else ""
    kicker = e['_unit']['title'] if e['_unit']['title'] == "法律文本导读" else f"{e['_unit']['title']} · 法律文本导读"
    body = f"""<div class="page-head"><p class="kicker">{esc(kicker)}</p><h1>{esc(e['title'])}</h1><div class="badges">{badge(e)}</div><p class="lead">{esc(e['definition'])}</p>{meta}</div>
<article class="prose">
<section><h2>立法背景</h2><p>{esc(l.get('background',''))}</p></section>
<section><h2>结构</h2><table class="data-table compact">{structure}</table></section>
{('<section><h2>结构图</h2><figure class="diagram">'+diagram+'</figure></section>') if diagram else ''}
<section><h2>关键条文</h2><ul class="article-list">{articles}</ul></section>
<section><h2>修订历程</h2><ul>{amendments}</ul></section>
<section><h2>相关司法解释</h2><ul>{interp}</ul></section>
<section><h2>待核实</h2><p>{esc(e.get('pending_notes') or '无。')}</p></section>
<section><h2>相关条目</h2><p>{related_html(e, by_id)}</p></section>
<section><h2>来源</h2>{sources_html(e, source_map)}</section>
</article>"""
    return page(e["title"], body, active="laws.html")


def render_flow(e, by_id, source_map):
    f = e.get("flow") or {}
    steps = f.get("steps", [])
    diagram = box_svg(f"{e['title']} · 流程图", [s.get("name", "") for s in steps])
    rows = "".join(f"<tr><td>{i+1}</td><td><strong>{esc(s.get('name',''))}</strong><br><span class='muted'>{esc(s.get('note',''))}</span></td><td>{esc(s.get('basis',''))}</td></tr>" for i, s in enumerate(steps))
    body = f"""<div class="page-head"><p class="kicker">{esc(e['_unit']['title'])} · 流程</p><h1>{esc(e['title'])}</h1><div class="badges">{badge(e)}</div><p class="lead">{esc(e['definition'])}</p></div>
<article class="prose">
<section><h2>流程图</h2><figure class="diagram">{diagram}</figure></section>
<section><h2>环节与法律依据</h2><table class="data-table compact"><thead><tr><th>#</th><th>环节</th><th>法律依据 / 说明</th></tr></thead><tbody>{rows}</tbody></table></section>
<section><h2>概述</h2><p>{esc(e['summary'])}</p></section>
<section><h2>待核实</h2><p>{esc(e.get('pending_notes') or '各环节具体条文号需按现行文本核对。')}</p></section>
<section><h2>相关条目</h2><p>{related_html(e, by_id)}</p></section>
<section><h2>来源</h2>{sources_html(e, source_map)}</section>
</article>"""
    return page(e["title"], body, active="flows.html")


def render_entry(e, by_id, source_map):
    if e["type"] == "case":
        return render_case(e, by_id, source_map)
    if e["type"] == "law":
        return render_law(e, by_id, source_map)
    if e["type"] == "flow":
        return render_flow(e, by_id, source_map)
    return render_concept(e, by_id, source_map)


def render_list_page(title, entries, by_id, active, desc=""):
    cards = "".join(entry_card(e) for e in entries)
    body = f"""<div class="page-head"><p class="kicker">{esc(active.replace('.html',''))}</p><h1>{esc(title)}</h1><p>{esc(desc)}</p></div><div class="entry-grid">{cards}</div>"""
    return page(title, body, active=active)


def render_sources(sources):
    rows = []
    for s in sorted(sources, key=lambda x: (not x.get("verified"), x.get("type", ""), x.get("title", ""))):
        link = f'<a href="{esc(s["url"])}" target="_blank" rel="noopener noreferrer">打开</a>' if s.get("url") else "—"
        status = "✅ 已核验" if s.get("verified") else "⚠️ 待核验"
        rows.append(f"<tr><td>{esc(s.get('title',''))}</td><td>{esc(s.get('author',''))}</td><td>{esc(s.get('year',''))}</td><td>{esc(s.get('type',''))}</td><td>{esc(s.get('jurisdiction',''))}</td><td>{status}</td><td>{link}</td></tr>")
    body = f"""<div class="page-head"><p class="kicker">来源库</p><h1>来源与核验状态</h1><p>共 {len(sources)} 条来源，其中 {sum(1 for s in sources if s.get('verified'))} 条已实际打开页面核对标题并标记 verified。</p></div>
<table class="data-table"><thead><tr><th>标题</th><th>作者/机构</th><th>年份</th><th>类型</th><th>辖区</th><th>状态</th><th>链接</th></tr></thead><tbody>{''.join(rows)}</tbody></table>"""
    return page("来源", body, active="sources.html")


def render_coverage(coverage, units):
    lv = coverage["levels"]
    matrix = coverage["matrix"]
    type_keys = ["概念制度", "案例", "文本导读", "流程"]
    head = "".join(f"<th>{k}</th>" for k in type_keys)
    rows = []
    for u in units:
        m = matrix[u["unit_id"]]
        cells = "".join(f"<td>{m['by_type'].get(k,0)}</td>" for k in type_keys)
        rows.append(f"<tr><td><a href='unit-{u['unit_id']}.html'>{esc(u['title'])}</a></td>{cells}<td>{m['total']}</td><td>{'✅' if coverage['core_l2_coverage'].get(u['unit_id']) else ('—' if coverage['core_l2_coverage'].get(u['unit_id']) is None else '❌')}</td></tr>")
    juris_rows = []
    for u in units:
        m = matrix[u["unit_id"]]["by_jurisdiction"]
        juris_rows.append(f"<tr><td>{esc(u['title'])}</td><td>{esc('、'.join(f'{k} {sum(v.values())}' for k,v in m.items()))}</td></tr>")
    body = f"""<div class="page-head"><p class="kicker">覆盖矩阵</p><h1>覆盖与进度</h1><p>总条目 {coverage['total']}；L1 {lv.get('L1',0)}、L2 {lv.get('L2',0)}、L3 {lv.get('L3',0)}。核心条目全部达到 L2 及以上的单元：{sum(1 for v in coverage['core_l2_coverage'].values() if v)}/{sum(1 for v in coverage['core_l2_coverage'].values() if v is not None)}。</p></div>
<h2>部门法 × 页面类型</h2>
<table class="data-table"><thead><tr><th>单元</th>{head}<th>合计</th><th>核心 L2</th></tr></thead><tbody>{''.join(rows)}</tbody></table>
<h2>部门法 × 辖区</h2>
<table class="data-table"><thead><tr><th>单元</th><th>辖区分布</th></tr></thead><tbody>{''.join(juris_rows)}</tbody></table>
<h2>矩阵说明</h2><p>覆盖矩阵按“部门法 × 辖区 × 页面类型（概念制度／案例／文本导读／流程）”统计；核心条目 L2 列检查每个部门法是否至少有一个核心制度完成 L2。</p>"""
    return page("覆盖", body, active="coverage.html")


def render_timeline(entries):
    dated = [e for e in entries if isinstance(e.get("year"), int)]
    dated.sort(key=lambda e: e["year"])
    items = []
    for e in dated:
        y = e["year"]
        ys = f"公元前{abs(y)}" if y < 0 else str(y)
        items.append(f"<li><span class='year'>{ys}</span><a href='entry-{e['id']}.html'>{esc(e['title'])}</a><span class='muted'>{esc(e['_unit']['title'])}</span></li>")
    body = f"""<div class="page-head"><p class="kicker">时间线</p><h1>按时间排列的条目</h1><p>仅显示在数据中标注了明确年份的条目；无明确年份的概念与制度条目请看部门法地图。</p></div><ol class='timeline'>{''.join(items)}</ol>"""
    return page("时间线", body, active="timeline.html")


def render_about():
    body = f"""<div class="page-head"><p class="kicker">关于</p><h1>方法与边界</h1></div>
<article class="prose">
<section><h2>这是什么</h2><p>一个面向学习与查阅的法律知识库。它以中国大陆现行法为主，兼顾比较法与国际法；每个条目都标注辖区、类型与来源。它不是法律意见，也不能替代执业律师对具体案件的分析。</p></section>
<section><h2>怎么做的</h2><ol><li>用四份权威大纲/目录取并集，形成 <code>scope.md</code>。</li><li>逐条建立来源，只有实际打开页面并核对标题的才标记 <code>verified=true</code>。</li><li>先用 <code>check.py</code> 校验字段、来源、日期、链接与 SVG，再生成站点。</li><li>L1 骨架覆盖全部条目；核心条目升 L2；少量核心条目升 L3。</li></ol></section>
<section><h2>五层标注</h2><p>本库尽量区分：法律条文、司法解释、指导性案例、学说观点、实务经验。学说争议会列出各方理由，不替读者下结论。</p></section>
<section><h2>待核实</h2><p>无法核实的案号、裁判日期、条文号与数字，统一写“待核实”。“待核实”不是装饰，而是提醒读者在引用前回到官方文本。</p></section>
<section><h2>页脚声明</h2><p>{esc(DISCLAIMER)}</p></section>
</article>"""
    return page("关于", body, active="about.html")


def main():
    os.makedirs(SITE, exist_ok=True)
    units, entries, by_id, sources, coverage = load()
    source_map = {s["id"]: s for s in sources}

    # pages
    pages = {
        "index.html": render_index(units, entries, sources, coverage),
        "units.html": render_units(units),
        "sources.html": render_sources(sources),
        "coverage.html": render_coverage(coverage, units),
        "timeline.html": render_timeline(entries),
        "about.html": render_about(),
        "cases.html": render_list_page("案例", [e for e in entries if e["type"] == "case"], by_id, "cases.html", "中外经典案例与指导性案例；案号与裁判日期未核实者已标注。"),
        "laws.html": render_list_page("法律文本", [e for e in entries if e["type"] == "law"], by_id, "laws.html", "重要法律的立法背景、结构、关键条文与修订历程。"),
        "flows.html": render_list_page("程序流程", [e for e in entries if e["type"] == "flow"], by_id, "flows.html", "民事诉讼、刑事诉讼、行政诉讼、仲裁、行政复议与执行的操作路径。"),
        "index-all.html": render_list_page("全部条目", sorted(entries, key=lambda e: (e["_unit"]["order"], e["type"], e["title"])), by_id, "index-all.html", f"共 {len(entries)} 条。可按部门法、类型或标题浏览。"),
    }
    for u in units:
        pages[f"unit-{u['unit_id']}.html"] = render_unit(u)
    for e in entries:
        pages[f"entry-{e['id']}.html"] = render_entry(e, by_id, source_map)

    for name, content in pages.items():
        with open(os.path.join(SITE, name), "w", encoding="utf-8") as f:
            f.write(content)

    # CSS
    css = """/* 法律知识库 · 法典卷宗主题 */
:root{
  --paper:#f7f4ec; --paper-2:#fffdf7; --paper-3:#efe9dc;
  --ink:#1b2430; --muted:#5d6672; --line:#d8d0c0;
  --accent:#8c2f2f; --accent-soft:#f3e3df; --navy:#1f3a52; --gold:#a88245;
  --shadow:0 10px 30px rgba(30,35,45,.08); --radius:14px;
}
@media (prefers-color-scheme: dark){
  :root{--paper:#11161d; --paper-2:#171e27; --paper-3:#1e2732; --ink:#e9e3d6; --muted:#a7b0bc; --line:#33404e; --accent:#d07a6a; --accent-soft:#3a2323; --navy:#8fb3d9; --gold:#c9a86a; --shadow:0 10px 30px rgba(0,0,0,.35);}
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:
  radial-gradient(1200px 600px at 12% -10%, color-mix(in srgb, var(--gold) 10%, transparent), transparent 60%),
  radial-gradient(900px 500px at 100% 0%, color-mix(in srgb, var(--accent) 8%, transparent), transparent 55%),
  var(--paper);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;line-height:1.75;font-size:16px}
a{color:var(--accent);text-decoration:none} a:hover{text-decoration:underline}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.skip{position:absolute;left:-999px}.skip:focus{left:12px;top:12px;background:var(--paper-2);padding:8px;z-index:99}
.site-header{border-bottom:1px solid var(--line);background:color-mix(in srgb,var(--paper) 86%,transparent);backdrop-filter:blur(10px);position:sticky;top:0;z-index:20}
.masthead{max-width:1180px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:12px;color:var(--ink)}
.brand:hover{text-decoration:none}
.brand-mark{width:44px;height:44px;border-radius:10px;background:var(--accent);color:#fff;display:grid;place-items:center;font-family:"Songti SC","STSong","Noto Serif SC",serif;font-size:26px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.18)}
.brand-text{display:flex;flex-direction:column;line-height:1.2}
.brand-text strong{font-size:19px;letter-spacing:.06em}.brand-text small{color:var(--muted);font-size:12px;letter-spacing:.18em}
.main-nav{display:flex;gap:6px;flex-wrap:wrap}
.main-nav a{padding:7px 11px;border-radius:8px;color:var(--muted);font-size:14px}
.main-nav a:hover{background:var(--paper-3);text-decoration:none;color:var(--ink)}
.main-nav a.active{color:var(--accent);background:var(--accent-soft);font-weight:600}
.hero{display:grid;grid-template-columns:1.55fr .85fr;gap:35px;padding:64px 0 36px;align-items:center}
.kicker{color:var(--accent);font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;margin:0 0 8px}
.hero h1{font-family:"Songti SC","STSong","Noto Serif SC",Georgia,serif;font-size:clamp(30px,4vw,52px);line-height:1.18;margin:0 0 18px;letter-spacing:-.01em}
.lede{font-size:17px;color:var(--muted);max-width:70ch}
.hero-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}
.btn{display:inline-block;padding:10px 16px;border:1px solid var(--line);border-radius:999px;color:var(--ink);background:var(--paper-2);font-size:14px}
.btn:hover{text-decoration:none;border-color:var(--accent)}
.btn.primary{background:var(--accent);color:#fff;border-color:var(--accent)}
.btn.ghost{background:transparent}
.hero-stats{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.stat{background:var(--paper-2);border:1px solid var(--line);border-radius:var(--radius);padding:18px 16px;box-shadow:var(--shadow)}
.stat strong{display:block;font-size:32px;font-family:"Songti SC","STSong",serif;color:var(--accent)}
.stat span{color:var(--muted);font-size:13px}
.section{padding:34px 0}
.section-head{display:flex;justify-content:space-between;align-items:end;gap:18px;border-bottom:2px solid var(--ink);padding-bottom:12px;margin-bottom:20px}
.section-head h2{margin:0;font-family:"Songti SC","STSong",serif;font-size:26px}
.section-head p{margin:0;color:var(--muted);font-size:14px}
.unit-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.unit-card{display:block;position:relative;background:var(--paper-2);border:1px solid var(--line);border-radius:var(--radius);padding:18px 18px 16px;color:var(--ink);box-shadow:var(--shadow);transition:transform .15s,border-color .15s}
.unit-card:hover{transform:translateY(-2px);border-color:var(--accent);text-decoration:none}
.unit-card h3{margin:0 0 6px;padding-right:42px;font-family:"Songti SC","STSong",serif;font-size:19px}
.unit-card p{margin:0;color:var(--muted);font-size:13.5px}
.unit-num{position:absolute;right:16px;top:12px;font-family:Georgia,serif;color:var(--line);font-size:22px}
.unit-count{display:inline-block;margin-top:10px;font-size:12px;color:var(--accent);border:1px solid var(--accent-soft);background:var(--accent-soft);padding:2px 8px;border-radius:999px}
.entry-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.entry-card{background:var(--paper-2);border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:8px}
.entry-head{display:flex;justify-content:space-between;gap:10px;align-items:start;flex-wrap:wrap}
.entry-head h3{margin:0;font-family:"Songti SC","STSong",serif;font-size:18px;line-height:1.35}
.entry-def{margin:0;color:var(--ink);font-size:14px}
.entry-meta{margin:0;color:var(--muted);font-size:12.5px}
.badges{display:flex;gap:5px;flex-wrap:wrap}
.badge{font-size:11px;line-height:1;padding:4px 7px;border-radius:999px;border:1px solid var(--line);color:var(--muted);white-space:nowrap}
.badge-core{color:#fff;background:var(--accent);border-color:var(--accent)}
.badge-imp{color:var(--navy);border-color:var(--navy)}
.badge-sup{color:var(--muted)}
.badge-l2{background:var(--paper-3);color:var(--ink)}
.badge-l3{background:var(--gold);color:#1b2430;border-color:var(--gold)}
.badge-type{background:var(--accent-soft);color:var(--accent);border-color:var(--accent-soft)}
.page-head{padding:46px 0 24px;border-bottom:1px solid var(--line);margin-bottom:28px}
.page-head h1{font-family:"Songti SC","STSong",serif;font-size:clamp(28px,4vw,44px);margin:0 0 10px}
.page-head .lead{font-size:18px;color:var(--ink);max-width:80ch;margin:14px 0 0}
.muted{color:var(--muted)}
.prose{max-width:960px;padding-bottom:40px}
.prose h2{font-family:"Songti SC","STSong",serif;font-size:24px;margin:38px 0 12px;padding-bottom:6px;border-bottom:1px solid var(--line)}
.prose h3{font-size:18px;margin:20px 0 8px}
.prose p{margin:0 0 12px}
.prose ul,.prose ol{margin:0 0 14px;padding-left:1.4em}
.prose li{margin:4px 0}
.prose code{background:var(--paper-3);padding:1px 5px;border-radius:4px;font-size:.9em}
.structured section{scroll-margin-top:90px}
.law-meta{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.law-meta span{font-size:12.5px;color:var(--muted);border:1px solid var(--line);background:var(--paper-2);padding:4px 10px;border-radius:999px}
.debate{background:var(--paper-2);border-left:3px solid var(--accent);padding:12px 16px;border-radius:0 10px 10px 0;margin:10px 0}
.debate h3{margin:0 0 6px;font-size:16px}
.diagram{background:var(--paper-2);border:1px solid var(--line);border-radius:var(--radius);padding:8px;overflow-x:auto}
.diagram svg{display:block;width:100%;height:auto;min-width:600px}
.deep{background:linear-gradient(180deg,var(--paper-2),transparent);border:1px solid var(--line);border-radius:var(--radius);padding:4px 22px 18px;margin-top:28px}
.data-table{width:100%;border-collapse:collapse;background:var(--paper-2);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;font-size:14px;margin:10px 0 26px}
.data-table th,.data-table td{padding:10px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
.data-table thead th{background:var(--paper-3);font-size:12.5px;letter-spacing:.05em;color:var(--muted)}
.data-table.compact{font-size:13.5px}
.case-table{width:100%;border-collapse:collapse;font-size:14.5px;background:var(--paper-2);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.case-table th{width:140px;text-align:left;padding:11px 14px;background:var(--paper-3);border-bottom:1px solid var(--line);color:var(--muted);vertical-align:top}
.case-table td{padding:11px 14px;border-bottom:1px solid var(--line)}
.source-list{font-size:13.5px}
.source-list li{margin:6px 0}
.timeline{list-style:none;padding:0;border-left:2px solid var(--accent);margin-left:8px}
.timeline li{position:relative;padding:8px 0 8px 22px}
.timeline li:before{content:"";position:absolute;left:-7px;top:16px;width:12px;height:12px;border-radius:50%;background:var(--paper);border:2px solid var(--accent)}
.timeline .year{display:inline-block;min-width:82px;font-family:Georgia,serif;color:var(--accent);font-weight:700}
.timeline .muted{margin-left:10px;font-size:12.5px}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.panel{background:var(--paper-2);border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;box-shadow:var(--shadow)}
.panel h2{margin-top:0;font-family:"Songti SC","STSong",serif}
.clean{padding-left:1.2em}
.more{margin:20px 0 0}
.site-footer{border-top:1px solid var(--line);margin-top:50px;padding:24px;text-align:center;color:var(--muted);font-size:13px}
.site-footer .disclaimer{max-width:900px;margin:0 auto 8px;color:var(--ink)}
.citation{font-size:13px;color:var(--muted)}
@media(max-width:820px){.hero{grid-template-columns:1fr;padding-top:36px}.two-col{grid-template-columns:1fr}.section-head{display:block}.main-nav{gap:2px}.main-nav a{font-size:13px;padding:6px 8px}}
@media print{.site-header,.hero-actions,.main-nav{display:none}.diagram svg{min-width:0}}
"""
    with open(os.path.join(SITE, "style.css"), "w", encoding="utf-8") as f:
        f.write(css)

    # root redirect
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=site/index.html"><title>法律知识库</title></head><body><p>正在进入 <a href="site/index.html">法律知识库</a>…</p></body></html>""")

    print(f"generated {len(pages)} pages + style.css in site/")


if __name__ == "__main__":
    main()
