# portfolio-policies

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
| `quartz` | Subly — Subscription Tracker | `com.ianskaitis.quartz` | [privacy/quartz.html](privacy/quartz.html) |
| `ember` | Blinkwell — Eye Break Timer | `com.ianskaitis.ember` | [privacy/ember.html](privacy/ember.html) |
| `atlas` | Garage Log — Car Maintenance | `com.ianskaitis.atlas` | [privacy/atlas.html](privacy/atlas.html) |
| `pylon` | Hourly — Timesheet & Pay | `com.ianskaitis.pylon` | [privacy/pylon.html](privacy/pylon.html) |
| `harbour` | Haven — Home Inventory | `com.ianskaitis.harbour` | [privacy/harbour.html](privacy/harbour.html) |
| `vega` | Sproutly — Plant Care | `com.ianskaitis.vega` | [privacy/vega.html](privacy/vega.html) |
| `onyx` | PetFile — Pet Records | `com.ianskaitis.onyx` | [privacy/onyx.html](privacy/onyx.html) |
| `orbit` | Shiftly — Shift Work Calendar | `com.ianskaitis.orbit` | [privacy/orbit.html](privacy/orbit.html) |
| `cinder` | MileMark — Mileage & Receipts | `com.ianskaitis.cinder` | [privacy/cinder.html](privacy/cinder.html) |
| `lumen` | Echo Notes — Offline Voice Notes | `com.ianskaitis.lumen` | [privacy/lumen.html](privacy/lumen.html) |
| `quay` | Fisherman's Wharf Tycoon | `com.iaengineering.wharftycoon` | [privacy/quay.html](privacy/quay.html) |

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
