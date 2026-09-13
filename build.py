#!/usr/bin/env python
"""Generate the portfolio privacy-policy static site (no external deps)."""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
PRIV = os.path.join(ROOT, "privacy")
os.makedirs(PRIV, exist_ok=True)

EFFECTIVE = "10 September 2026"
DEV = "Ignas Anskaitis"
DEV_DESC = "an individual developer"
EMAIL = "ianskaitis@gmail.com"

APPS = [
    ("quartz", "Subly — Subscription Tracker", "com.ianskaitis.quartz",
     "Subly helps you keep track of your recurring subscriptions and their renewal dates."),
    ("ember", "Blinkwell — Eye Break Timer", "com.ianskaitis.ember",
     "Blinkwell reminds you to take regular screen breaks to reduce eye strain."),
    ("atlas", "Garage Log — Car Maintenance", "com.ianskaitis.atlas",
     "Garage Log lets you record maintenance, repairs and service history for your vehicles."),
    ("pylon", "Hourly — Timesheet & Pay", "com.ianskaitis.pylon",
     "Hourly lets you log your working hours and estimate your pay."),
    ("harbour", "Haven — Home Inventory", "com.ianskaitis.harbour",
     "Haven lets you catalogue the belongings and rooms in your home."),
    ("vega", "Sproutly — Plant Care", "com.ianskaitis.vega",
     "Sproutly helps you schedule watering and care for your plants."),
    ("onyx", "PetFile — Pet Records", "com.ianskaitis.onyx",
     "PetFile lets you keep health, vaccination and care records for your pets."),
    ("orbit", "Shiftly — Shift Work Calendar", "com.ianskaitis.orbit",
     "Shiftly lets shift workers plan and track their rotating work schedules."),
    ("cinder", "MileMark — Mileage & Receipts", "com.ianskaitis.cinder",
     "MileMark lets you record trips, mileage and receipt details for expense tracking."),
    ("lumen", "Echo Notes — Offline Voice Notes", "com.ianskaitis.lumen",
     "Echo Notes lets you record, store and play back voice notes entirely on your device."),
    ("quay", "Fisherman's Wharf Tycoon", "com.iaengineering.wharftycoon",
     "Fisherman's Wharf Tycoon is an offline harbour tycoon game: catch fish at the pier, "
     "clean them at the table, stock the ice display, serve the queue at the till, hire a "
     "crew and expand across eight plots of the quay."),
]

STYLE = """/* Shared stylesheet for the portfolio privacy-policy site.
   No external fonts, no tracking, no analytics, no cookies. */
:root {
  color-scheme: light dark;
  --bg: #ffffff;
  --fg: #1c1f23;
  --muted: #5b6570;
  --rule: #dfe3e8;
  --accent: #1a4d8f;
  --card: #f6f8fa;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #14171a;
    --fg: #e8eaed;
    --muted: #9aa4ae;
    --rule: #2b3138;
    --accent: #79b0f0;
    --card: #1c2126;
  }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  padding: 1.25rem 1rem 3rem;
  background: var(--bg);
  color: var(--fg);
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 17px;
  line-height: 1.6;
}
main { max-width: 46rem; margin: 0 auto; }
h1 { font-size: 1.55rem; line-height: 1.25; margin: 0 0 .35rem; }
h2 { font-size: 1.12rem; margin: 1.8rem 0 .5rem; }
p, li { margin: .6rem 0; }
ul { padding-left: 1.25rem; }
a { color: var(--accent); }
.lede { color: var(--muted); margin-top: 0; }
.meta { margin: .9rem 0 1.4rem; padding: .85rem 1rem; background: var(--card);
        border: 1px solid var(--rule); border-radius: 8px; font-size: .95rem; }
.meta dl { margin: 0; display: grid; grid-template-columns: max-content 1fr; gap: .25rem .85rem; }
.meta dt { color: var(--muted); }
.meta dd { margin: 0; overflow-wrap: anywhere; }
hr { border: 0; border-top: 1px solid var(--rule); margin: 2rem 0 1rem; }
footer { color: var(--muted); font-size: .9rem; margin-top: 2rem; }
ul.apps { list-style: none; padding: 0; margin: 1.5rem 0 0; }
ul.apps li { margin: 0 0 .75rem; padding: .85rem 1rem; background: var(--card);
             border: 1px solid var(--rule); border-radius: 8px; }
ul.apps a { font-weight: 600; text-decoration: none; }
ul.apps a:hover, ul.apps a:focus { text-decoration: underline; }
ul.apps .pkg { display: block; color: var(--muted); font-size: .85rem;
               font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
               overflow-wrap: anywhere; }
ul.apps .desc { display: block; color: var(--muted); font-size: .92rem; margin-top: .15rem; }
.policy-list { padding-left: 1.25rem; }
.policy-list a { text-decoration: none; }
.policy-list a:hover, .policy-list a:focus { text-decoration: underline; }
@media (max-width: 30rem) {
  body { font-size: 16px; padding: 1rem .85rem 2.5rem; }
  .meta dl { grid-template-columns: 1fr; gap: 0; }
  .meta dd { margin-bottom: .5rem; }
}
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Privacy Policy</title>
<meta name="description" content="Privacy policy for {title} ({pkg}), an offline Android app by {dev}.">
<meta name="robots" content="index, follow">
<meta name="referrer" content="no-referrer">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<main>
<h1>Privacy Policy &mdash; {title}</h1>
<p class="lede">{blurb}</p>

<div class="meta">
<dl>
<dt>App</dt><dd>{title}</dd>
<dt>Package name</dt><dd>{pkg}</dd>
<dt>Developer</dt><dd>{dev}, {devdesc}</dd>
<dt>Contact</dt><dd><a href="mailto:{email}">{email}</a></dd>
<dt>Effective date</dt><dd>{effective}</dd>
</dl>
</div>

<p>This policy explains what {title} does and does not do with your information.
It applies to the Android application <strong>{title}</strong> published under the
package name <strong>{pkg}</strong>. By installing and using the app you agree to
this policy. If you do not agree, please uninstall the app.</p>

<h2>Summary</h2>
<p>{title} is designed to work entirely on your device. It has no account system,
no sign-in, no analytics, no advertising, and no third-party tracking. It does not
send your personal information to the developer or to anyone else. All content you
create in the app is stored locally on your own device.</p>

<h2>Information we collect</h2>
<p>We collect nothing. The developer of {title} does not collect, receive, store,
sell, rent or share any personal information about you. Specifically, the app does
not collect:</p>
<ul>
<li>your name, email address, phone number or postal address;</li>
<li>your contacts, calendar, photos, files or messages;</li>
<li>your location, precise or approximate;</li>
<li>your device identifiers, advertising ID or hardware identifiers;</li>
<li>your usage behaviour, app interaction logs, crash reports or diagnostics;</li>
<li>any other personal data or personally identifiable information.</li>
</ul>
<p>The app does not ask you to create an account and has no sign-in or registration
of any kind. There is no analytics SDK, no advertising SDK, no crash-reporting SDK
and no third-party tracking library included in the app.</p>

<h2>Information you enter, and where it is stored</h2>
<p>Everything you enter into {title} is stored locally on your device, in the app's
own private storage area. This data is created and kept for the sole purpose of
making the app work for you. It stays on your device.</p>
<p>The developer has no server that receives this data and cannot see, access,
retrieve or read it. The data is not backed up to the developer and is not shared
with any third party by the app. If your device is configured to sync app data to a
cloud backup service you have chosen (for example a device-level backup provided by
your phone's manufacturer or operating system), that backup is controlled by you and
by that provider's own terms and privacy policy, not by this app.</p>

<h2>Network use and in-app purchases</h2>
<p>{title} does not transmit your personal data over the internet to the developer or
to anyone else.</p>
<p>The only network activity in the app is Google Play's own billing service, used
for optional in-app purchases. If you choose to make a purchase, the transaction is
processed entirely by Google Play; the app never sees or stores your payment card
details. Purchase processing is handled by Google and is governed by Google's privacy
policy, available at
<a href="https://policies.google.com/privacy" rel="noopener noreferrer nofollow">https://policies.google.com/privacy</a>.
If you never make an in-app purchase, the app does not need to use the network at all.</p>

<h2>Notifications</h2>
<p>Any notifications or reminders {title} shows you are generated locally on your
device from data already stored on your device. No notification content is sent to
the developer or to any third party. You can turn notifications off at any time in
the app or in your device's system settings.</p>

<h2>Permissions</h2>
<p>{title} requests only the device permissions it needs to provide its features, and
those permissions are used on your device. The app does not use permissions to
collect or transmit personal data.</p>

<h2>Children's privacy</h2>
<p>{title} is not directed at children under the age of 13. The app is intended for a
general adult audience, and the developer does not knowingly collect any personal
information from children under 13. Because the app collects no personal information
at all and stores everything locally on the device, no such information can reach the
developer. If you believe a child under 13 has used the app, you can remove all data
created by the app by uninstalling it; if you have any concern, please contact the
developer at <a href="mailto:{email}">{email}</a>.</p>

<h2>Your control over your data, and deletion</h2>
<p>You are in full control of the information in {title}, because it lives on your
device and nowhere else. You can delete it at any time by either of these methods:</p>
<ul>
<li>using the in-app delete or reset controls, which clear the data the app stores; or</li>
<li>uninstalling the app, which removes the app and its locally stored data from your
device.</li>
</ul>
<p>Because the developer never receives your data, there is no copy of it held by the
developer to delete, export or correct, and no deletion request needs to be sent.
Uninstalling the app or using the in-app reset is complete and final. If you would
like help with deleting data, or have any question about it, you can email the
developer at <a href="mailto:{email}">{email}</a>.</p>

<h2>Data security</h2>
<p>Your data is protected by your device's own security, including any screen lock,
device encryption and operating-system protections you have enabled. Because the data
is not transmitted to the developer, there is no developer-held database that could
be breached. You should keep your device's operating system up to date and use a
screen lock to protect the data on your device.</p>

<h2>Third-party services</h2>
<p>{title} does not include advertising networks, analytics providers, data brokers
or social-media tracking. The only third party involved is Google Play, and only if
you choose to make an in-app purchase, in which case Google's privacy policy applies
to the processing of that purchase. This privacy-policy website contains no cookies,
no analytics and no tracking scripts.</p>

<h2>Changes to this policy</h2>
<p>If this policy changes, the updated version will be published on this page with a
new effective date. Continued use of the app after a change means you accept the
updated policy.</p>

<h2>Contact the developer</h2>
<p>{title} is developed and published by {dev}, {devdesc}. If you have any questions
about this privacy policy or about privacy in the app, please contact:</p>
<p>{dev}<br>
Email: <a href="mailto:{email}">{email}</a></p>

<hr>
<p class="lede">This policy applies to the Android app <strong>{title}</strong>
(package name <strong>{pkg}</strong>) and was last updated on {effective}.</p>
<footer>
<p><a href="../index.html">All apps and privacy policies</a></p>
</footer>
</main>
</body>
</html>
"""

INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Privacy Policies &mdash; Android apps by Ignas Anskaitis</title>
<meta name="description" content="Privacy policies for Android apps published by Ignas Anskaitis. Each app stores data locally on your device and collects nothing.">
<meta name="robots" content="index, follow">
<meta name="referrer" content="no-referrer">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
<h1>Privacy Policies</h1>
<p class="lede">Android apps published by Ignas Anskaitis, an individual developer.</p>

<div class="meta">
<dl>
<dt>Developer</dt><dd>Ignas Anskaitis, individual developer</dd>
<dt>Contact</dt><dd><a href="mailto:ianskaitis@gmail.com">ianskaitis@gmail.com</a></dd>
<dt>Effective date</dt><dd>10 September 2026</dd>
<dt>Applies to</dt><dd>10 Android applications, listed below</dd>
</dl>
</div>

<p>Every app listed here is designed to work entirely offline. Each one stores all of
its data locally on your device, has no account system and no sign-in, contains no
analytics and no advertising SDK, and does not transmit your personal data to the
developer or to anyone else. The only network use is Google Play's own billing service
for optional in-app purchases, which Google processes under
<a href="https://policies.google.com/privacy" rel="noopener noreferrer nofollow">Google's privacy policy</a>.
You can delete all app data at any time by uninstalling the app or by using its in-app
delete or reset controls.</p>
<p>Select an app to read its full privacy policy:</p>

<ul class="apps">
{items}
</ul>

<hr>
<h2>About this site</h2>
<p>This site is a plain static GitHub Pages site. It sets no cookies, loads no external
fonts, runs no analytics and contains no tracking scripts. It contains only the text of
the privacy policies linked above.</p>
<footer>
<p>Published by Ignas Anskaitis. Effective date: 10 September 2026.</p>
</footer>
</main>
</body>
</html>
"""

ITEM = """<li>
<a href="privacy/{code}.html">{name}</a>
<span class="pkg">{pkg}</span>
<span class="desc">{desc}</span>
</li>"""

READMEmd = """# portfolio-policies

Public privacy-policy pages for the Android applications published by Ignas Anskaitis
(`com.ianskaitis.*`), served via GitHub Pages.

Live site: https://ignasans.github.io/portfolio-policies/

## Contents

- `index.html` — index of all apps with links to their policies
- `style.css` — single shared stylesheet (responsive, light/dark, no external fonts)
- `privacy/<code>.html` — one privacy policy per app
- `privacy/template.html` — blank template used to generate new policies
- `.nojekyll` — serve files as-is

## Apps

| Code | App | Package name | Policy |
| --- | --- | --- | --- |
{table}

## Use with Google Play

Each app's Play Console listing should use its policy URL from the table above.

## Site properties

No cookies, no analytics, no tracking scripts, no external fonts, no external
resources of any kind. Every page is self-contained HTML plus one shared stylesheet.
The pages make no network requests other than loading `style.css` from this same origin.

## Adding a new app

1. Copy `privacy/template.html` to `privacy/<code>.html`.
2. Replace every `{{PLACEHOLDER}}`.
3. Add the app to the table above and to the list in `index.html`.
4. Commit and push; GitHub Pages redeploys automatically.
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{APP_NAME}} — Privacy Policy</title>
<meta name="description" content="Privacy policy for {{APP_NAME}} ({{PACKAGE_NAME}}), an offline Android app by Ignas Anskaitis.">
<meta name="robots" content="index, follow">
<meta name="referrer" content="no-referrer">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<main>
<h1>Privacy Policy &mdash; {{APP_NAME}}</h1>
<p class="lede">{{ONE_LINE_DESCRIPTION}}</p>

<div class="meta">
<dl>
<dt>App</dt><dd>{{APP_NAME}}</dd>
<dt>Package name</dt><dd>{{PACKAGE_NAME}}</dd>
<dt>Developer</dt><dd>{{DEVELOPER}}, an individual developer</dd>
<dt>Contact</dt><dd><a href="mailto:ianskaitis@gmail.com">ianskaitis@gmail.com</a></dd>
<dt>Effective date</dt><dd>{{EFFECTIVE_DATE}}</dd>
</dl>
</div>

<p>This policy explains what {{APP_NAME}} does and does not do with your information.
It applies to the Android application <strong>{{APP_NAME}}</strong> published under the
package name <strong>{{PACKAGE_NAME}}</strong>. By installing and using the app you
agree to this policy. If you do not agree, please uninstall the app.</p>

<h2>Summary</h2>
<p>{{APP_NAME}} is designed to work entirely on your device. It has no account system,
no sign-in, no analytics, no advertising, and no third-party tracking. It does not
send your personal information to the developer or to anyone else. All content you
create in the app is stored locally on your own device.</p>

<h2>Information we collect</h2>
<p>We collect nothing. The developer of {{APP_NAME}} does not collect, receive, store,
sell, rent or share any personal information about you. Specifically, the app does not
collect your name, email address, phone number, postal address, contacts, calendar,
photos, files, messages, location, device identifiers, advertising ID, usage behaviour,
crash reports, diagnostics, or any other personal data or personally identifiable
information. The app does not ask you to create an account and has no sign-in or
registration of any kind. There is no analytics SDK, no advertising SDK, no
crash-reporting SDK and no third-party tracking library included in the app.</p>

<h2>Information you enter, and where it is stored</h2>
<p>Everything you enter into {{APP_NAME}} is stored locally on your device, in the
app's own private storage area, for the sole purpose of making the app work for you.
The developer has no server that receives this data and cannot see, access, retrieve
or read it. The data is not backed up to the developer and is not shared with any third
party by the app.</p>

<h2>Network use and in-app purchases</h2>
<p>{{APP_NAME}} does not transmit your personal data over the internet to the developer
or to anyone else. The only network activity in the app is Google Play's own billing
service, used for optional in-app purchases. Purchase processing is handled by Google
and is governed by Google's privacy policy, available at
<a href="https://policies.google.com/privacy" rel="noopener noreferrer nofollow">https://policies.google.com/privacy</a>.</p>

<h2>Notifications</h2>
<p>Any notifications or reminders {{APP_NAME}} shows you are generated locally on your
device from data already stored on your device. No notification content is sent to the
developer or to any third party.</p>

<h2>Children's privacy</h2>
<p>{{APP_NAME}} is not directed at children under the age of 13. The developer does not
knowingly collect any personal information from children under 13. Because the app
collects no personal information at all and stores everything locally on the device, no
such information can reach the developer.</p>

<h2>Your control over your data, and deletion</h2>
<p>You can delete all data created by {{APP_NAME}} at any time by using the in-app
delete or reset controls, or by uninstalling the app, which removes the app and its
locally stored data from your device. Because the developer never receives your data,
there is no copy of it held by the developer to delete, export or correct.</p>

<h2>Contact the developer</h2>
<p>{{APP_NAME}} is developed and published by {{DEVELOPER}}, an individual developer.
If you have any questions about this privacy policy, please contact:
<a href="mailto:ianskaitis@gmail.com">ianskaitis@gmail.com</a></p>

<hr>
<p class="lede">This policy applies to the Android app <strong>{{APP_NAME}}</strong>
(package name <strong>{{PACKAGE_NAME}}</strong>) and was last updated on
{{EFFECTIVE_DATE}}.</p>
<footer>
<p><a href="../index.html">All apps and privacy policies</a></p>
</footer>
</main>
</body>
</html>
"""

# ---- write files ----
with open(os.path.join(ROOT, "style.css"), "w", encoding="utf-8", newline="\n") as f:
    f.write(STYLE)

items = []
rows = []
for code, name, pkg, blurb in APPS:
    page = (PAGE.replace("{title}", html.escape(name))
                .replace("{pkg}", html.escape(pkg))
                .replace("{devdesc}", DEV_DESC)
                .replace("{dev}", DEV)
                .replace("{email}", EMAIL)
                .replace("{effective}", EFFECTIVE)
                .replace("{blurb}", html.escape(blurb)))
    with open(os.path.join(PRIV, code + ".html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    items.append(ITEM.format(code=code, name=html.escape(name),
                             pkg=html.escape(pkg), desc=html.escape(blurb)))
    rows.append("| `{}` | {} | `{}` | [privacy/{}.html](privacy/{}.html) |".format(
        code, name, pkg, code, code))

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(INDEX.replace("{items}", "\n".join(items)))

with open(os.path.join(PRIV, "template.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(TEMPLATE)

with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(READMEmd.replace("{table}", "\n".join(rows)))

with open(os.path.join(ROOT, ".nojekyll"), "w", encoding="utf-8", newline="\n") as f:
    f.write("")

print("generated", len(APPS), "policies")
for code, name, pkg, _ in APPS:
    p = os.path.join(PRIV, code + ".html")
    print(code, os.path.getsize(p), "bytes")
