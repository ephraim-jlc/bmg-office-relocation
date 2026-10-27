#!/usr/bin/env python3
"""Builds north.html, midlands.html and index.html from template.html.

Copy lives in the VARIANTS dict below and mirrors the two source documents:
  source/Office relocation North landing page_Google Ads campaign.docx
  source/Office relocation Midlands landing page_Google Ads campaign.docx
Run:  python3 build.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent

OFFICES = {
    "Leeds": ("The North", "0113 236 0136"),
    "Reading": ("London and the South East", "0118 933 6600"),
    "Halesowen": ("The Midlands", "0121 559 1122"),
    "Glasgow": ("Scotland", "0141 773 4829"),
}

VARIANTS = {
    "north": dict(
        loc="North",
        area="Leeds, Manchester and the wider North of England",
        other="midlands",
        title="Office relocation in the North | Free site survey | Business Moves Group",
        meta="Planning an office move in Leeds, Manchester or across the North? Book a free site survey with a written report and recommendations, with no obligation to move with us.",
        phone="0113 236 0136",
        h1a="Planning an office move in the North?",
        sub="One of our move specialists from our Leeds team will visit your site, look at everything involved and give you a written report with our recommendations. It's free, and there's no obligation to use us for your move.",
        subshort="One of our move specialists from our Leeds team will visit your site... free, no obligation to use us.",
        trust="ISO 9001, 14001 and 45001 certified | British Association of Removers member | Local team for the North based in Leeds, with national coverage from Reading, Halesowen and Glasgow.",
        quotes=[
            ("I just wanted to say a massive thank you to you, Mark, and the BMG team for such a great job in clearing out our 1st floor contact centre. The project went like clockwork and the team you sent were very efficient and personable. Thank you again for a job well done and I’ll be in touch shortly when our stored furniture needs to be moved down to London.",
             "<u>Major airline</u> based in northwest England"),
            ("I would like to say a huge thank you to Colin and the team. There have certainly been some challenges for them today and they were so professional and accommodating!",
             "Gayle Summerly, manager, people administration and operations at <u>Turnitin</u>"),
            ("We are really pleased to be working with BMG. We have a busy programme of works this summer and the service that is provided by BMG is always of high standard. BMG work closely with all of our teams in estates and facilities to ensure we are utilising their services efficiently, and often suggest combining works to bring down overall cost and resource. We look forward to another busy summer working with the team.",
             "Victoria Riley, space and asset data manager, estates &amp; facilities, <u>Leeds Beckett University</u>"),
        ],
        logos=["Newcastle College", "Aviva", "Leeds Beckett University", "Allianz", "Warrington’s Own Buses", "Turnitin"],
        workhead="Recent moves in the North",
        workintro="A few of the projects our team in the North has delivered.",
        cases=[
            ("Leeds Building Society", "We project-managed the Society's move of more than 900 colleagues from three sites into its refurbished head office on Sovereign Street in Leeds, covering move planning, furniture management, IT relocation and post-move support."),
            ("Aviva, including its Sheffield office", "Our work with Aviva, which included its Sheffield office, won the PFM Partners in Relocation award in 2020."),
            ("Newcastle College", "Our work with ISS and Newcastle College saw a successful redistribution and recycling project for the organisations, creating the best environmental solutions with strong commercial benefits. As a result of BMG being able to deliver all works in-house, the project was delivered within the allocated time frames and forecasted costs."),
        ],
        why1="Our own trained, security-checked people and our own vehicles deliver every move. Our team for the North is based in Leeds, so the team that plans your move is the team that delivers it.",
        teamhead="Your local team for the North",
        teamintro="Our team for the North is based at Offco House in Pudsey, Leeds, and supports office moves across Leeds, Manchester, Yorkshire, Lancashire and the wider North of England. With offices in Reading, Halesowen and Glasgow too, we can support your move anywhere in the UK.",
        office_order=["Leeds", "Reading", "Halesowen", "Glasgow"],
        faqarea="Our team for the North covers Leeds, Manchester, Yorkshire, Lancashire and the wider North of England, and we work across the UK from our offices in Reading, Halesowen, Leeds and Glasgow.",
        closehead="Ready to plan your move in the North?",
        close2="Or call our team in the North on 0113 236 0136.",
        thanks_label={"Leeds": "The North (Leeds)"},
    ),
    "midlands": dict(
        loc="Midlands",
        area="Birmingham, the West Midlands and the wider Midlands",
        other="north",
        title="Office relocation in the Midlands | Free site survey | Business Moves Group",
        meta="Planning an office move in the Midlands? Book a free site survey with our Halesowen team, with a written report and recommendations and no obligation to move with us.",
        phone="0121 559 1122",
        h1a="Planning an office move in the Midlands?",
        sub="One of our Midlands move specialists will visit your site, look at everything involved and give you a written report with our recommendations. It's free, and there's no obligation to use us for your move.",
        subshort="One of our Midlands move specialists will visit your site... free, no obligation to use us.",
        trust="ISO 9001, 14001 and 45001 certified | British Association of Removers member | Local Midlands team based in Halesowen, with national coverage from Reading, Leeds and Glasgow.",
        quotes=[
            ("BMG is putting up with all my demands and is making this project so much easier for me. I look forward to working with them again.",
             "Hannah Todd, office manager, <u>West Midlands Trains</u>"),
            ("BMG was instrumental in executing a smooth and swift move of our assets that met stringent regulations at the same time. We were thrilled that the relocation was completed ahead of schedule and appreciate their support in finding sustainable furniture solutions for us.",
             "Project manager, <u>global armour manufacturer</u>"),
            ("BMG handled our short-notice enquiry swiftly and professionally, ensuring we were prioritised and our niche requirements understood and met. The expert planning meant that all stages of packing and moving went very smoothly, and the logistics team on the day went above and beyond to meet the unexpected demands of the move. I heartily recommend them to other NHS providers.",
             "Matthew Edwards, business operations manager at <u>Gordon Street Surgery</u>"),
        ],
        logos=["West Midlands Trains", "Anthony Collins Solicitors", "Allianz", "Ramboll", "Gordon Street Surgery"],
        workhead="Recent moves in the Midlands",
        workintro="A few of the projects our Midlands team has delivered.",
        cases=[
            ("West Midlands Trains, Birmingham", "A phased 36-week programme across two floors of West Midlands Trains' Birmingham city office, covering dismantling, packing, storage, redelivery and reassembly. Delivered to the agreed timeline by our local Midlands team."),
            ("International law firm, Birmingham", "We moved more than 450 desks and packed around 1,600 boxes to help a law firm consolidate its Birmingham office, freeing up a half floor to sub-let. The move was delivered on time and under budget."),
            ("Anthony Collins Solicitors, Birmingham", "We supported the firm's office refurbishment by moving more than 200 items between floors, storing furniture locally during the works, and decommissioning, testing and recommissioning all IT equipment."),
        ],
        why1="Our own trained, security-checked people and our own vehicles deliver every move. Our Midlands team is based locally in Halesowen, so the team that plans your move is the team that delivers it.",
        teamhead="Your local Midlands team",
        teamintro="Our Midlands team is based at Coombswood Business Park in Halesowen and supports office moves across Birmingham, the West Midlands and the wider Midlands. With offices in Reading, Leeds and Glasgow too, we can support your move anywhere in the UK.",
        office_order=["Halesowen", "Reading", "Leeds", "Glasgow"],
        faqarea="Our Midlands team covers Birmingham, the West Midlands and the wider Midlands, and we work across the UK from our offices in Reading, Halesowen, Leeds and Glasgow.",
        closehead="Ready to plan your move in the Midlands?",
        close2="Or call our Midlands team on 0121 559 1122.",
        thanks_label={"Halesowen": "Midlands (Halesowen)"},
    ),
}

NAMES = {"north": "Office Relocation North", "midlands": "Office Relocation Midlands"}
COPYFILES = {
    "north": "source/Office relocation North landing page_Google Ads campaign.docx",
    "midlands": "source/Office relocation Midlands landing page_Google Ads campaign.docx",
}


def render(key, template):
    v = VARIANTS[key]
    quotes = "\n".join(
        f'          <div class="quote"><p>“{q}”</p><span class="small">{a}</span></div>' for q, a in v["quotes"]
    )
    logos = "".join(f'<div class="ph">{n}</div>' for n in v["logos"])
    cases = "\n".join(
        f'          <div class="case"><div class="ph">Photo: {t}</div><h3>{t}</h3><p class="small">{d}</p></div>'
        for t, d in v["cases"]
    )
    offices = []
    for i, name in enumerate(v["office_order"]):
        cover, phone = OFFICES[name]
        cls = ' class="local"' if i == 0 else ""
        offices.append(f"          <tr{cls}><td>{name}</td><td>{cover}</td><td>{phone}</td></tr>")
    thanks = " | ".join(
        f'{v["thanks_label"].get(n, n)}: {OFFICES[n][1]}' for n in v["office_order"]
    )
    tokens = {
        "LOC": v["loc"], "AREA": v["area"], "COPYFILE": COPYFILES[key],
        "OTHERHREF": f'{v["other"]}.html', "OTHERNAME": NAMES[v["other"]],
        "TITLE": v["title"], "META": v["meta"], "PHONE": v["phone"],
        "H1A": v["h1a"], "SUB": v["sub"], "SUBSHORT": v["subshort"], "TRUSTLINE": v["trust"],
        "QUOTES": quotes, "LOGOS": logos, "WORKHEAD": v["workhead"], "WORKINTRO": v["workintro"],
        "CASES": cases, "WHY1": v["why1"], "TEAMHEAD": v["teamhead"], "TEAMINTRO": v["teamintro"],
        "OFFICES": "\n".join(offices), "FAQAREA": v["faqarea"], "CLOSEHEAD": v["closehead"],
        "CLOSE2": v["close2"], "THANKSPHONES": thanks,
    }
    out = template
    for k, val in tokens.items():
        out = out.replace(f"[[{k}]]", val)
    assert "[[" not in out, re.findall(r"\[\[\w+\]\]", out)
    # number the dev-note tags in document order
    n = iter(range(1, 100))
    out = re.sub(r'<b class="tag">(\d+)</b>', lambda m: f'<b class="tag">{next(n)}</b>', out)
    return out


INDEX = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>BMG Office Relocation Wireframes</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap">
<style>
  :root { --ink:#111; --mid:#777; --band:#ececec; --ph:#d9d9d9; }
  * { box-sizing:border-box; }
  body { margin:0; font:14px/1.5 Poppins, Helvetica, Arial, sans-serif; color:var(--ink); background:#fff; }
  main { max-width:960px; margin:0 auto; padding:40px 16px 60px; }
  h1 { font-size:24px; margin:0 0 6px; }
  .lead { color:var(--mid); margin:0 0 28px; }
  .cards { display:grid; grid-template-columns:1fr 1fr; gap:24px; }
  .card { border:1px solid var(--ink); display:flex; flex-direction:column; text-decoration:none; color:inherit; }
  .card .thumb { height:180px; background:var(--ph); border-bottom:1px solid var(--ink); padding:14px; display:flex; flex-direction:column; gap:8px; }
  .card .thumb i { display:block; background:#fff; border:1px solid #888; height:12px; }
  .card .body { padding:18px; flex:1; }
  .card h2 { font-size:18px; margin:0 0 4px; }
  .card p { margin:0 0 10px; font-size:13px; }
  .card dl { margin:0; font-size:12px; }
  .card dt { font-weight:600; float:left; clear:left; margin-right:6px; }
  .card dd { margin:0 0 2px; }
  .btn { display:inline-block; background:var(--ink); color:#fff; border-radius:999px; padding:8px 20px; font-weight:600; font-size:13px; margin-top:12px; }
  .card:hover { background:var(--band); }
  .notes { margin-top:36px; border-top:1px solid var(--ink); padding-top:16px; font-size:13px; }
  .notes h3 { font-size:14px; margin:0 0 6px; }
  .notes ul { margin:0; padding-left:18px; }
  @media (max-width:700px) { .cards { grid-template-columns:1fr; } }
</style>
</head>
<body>
<main>
  <h1>BMG Office Relocation: PPC landing page wireframes</h1>
  <p class="lead">B&amp;W structural wireframes, one per location - 27 Oct, 2026</p>
  <div class="cards">
[[CARDS]]
  </div>
  <div class="notes">
    <h3>Shared across both variants</h3>
    <ul>
      <li>Same layout and components; location copy, phone, testimonials, recent moves, logo strip and local office differ.</li>
      <li>All pages are noindex, separate from the SEO pages, with no main site navigation.</li>
      <li>Each variant has its own thank-you page (shown at the bottom of the wireframe) which triggers the conversion.</li>
      <li>Open copy placeholders (hatched boxes): survey step 1, survey length, report turnaround, review rating and count, ISO certification check.</li>
    </ul>
  </div>
</main>
</body>
</html>
"""


def card(key):
    v = VARIANTS[key]
    return f"""    <a class="card" href="{key}.html">
      <div class="thumb"><i style="width:40%"></i><i style="width:75%;height:20px"></i><i style="width:60%"></i><i style="width:30%;height:22px;background:#111"></i></div>
      <div class="body">
        <h2>{NAMES[key]}</h2>
        <p>{v["area"]}</p>
        <dl>
          <dt>Local office:</dt><dd>{v["office_order"][0]}</dd>
          <dt>Phone:</dt><dd>{v["phone"]}</dd>
          <dt>Page title:</dt><dd>{v["title"]}</dd>
        </dl>
        <span class="btn">Open wireframe</span>
      </div>
    </a>"""


def main():
    template = (HERE / "template.html").read_text()
    for key in VARIANTS:
        (HERE / f"{key}.html").write_text(render(key, template))
    cards = "\n".join(card(k) for k in VARIANTS)
    (HERE / "index.html").write_text(INDEX.replace("[[CARDS]]", cards))
    print("built:", ", ".join(f"{k}.html" for k in VARIANTS), "index.html")


if __name__ == "__main__":
    main()
