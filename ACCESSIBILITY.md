# Accessibility

This statement covers the AI Adoption Controls Framework website (https://aacf.adriansaxton.com), its online
self-assessment and its downloads. It was written on 13 November 2026 from a check of the site's own code. The site
has not yet had a formal audit against the Web Content Accessibility Guidelines (WCAG) 2.2, and it has not been tested
with screen readers.

## What the site supports

- **Plain pages.** Every page is plain HTML and works without JavaScript, apart from the self-assessment, search and
  the theme switch.
- **Structure.** The page language is set to British English. The header, main navigation, main content and footer
  are marked as landmarks, each page has one main heading, and a skip link at the top of every page goes straight to
  the main content.
- **Keyboard.** Links, buttons and form controls show a visible focus outline, so the site can be used with a
  keyboard alone.
- **Contrast.** Every text colour meets the WCAG 2.2 AA contrast ratio in both themes: at least 5.3 to 1, and 17 to 1
  for body text in the light theme.
- **Themes.** Light by default, with a dark theme on request. The choice is remembered on that device only.
- **Motion.** The only animation is a short colour change on links and buttons, and it is switched off when the
  device asks for reduced motion.
- **Levels.** On control pages each maturity level is shown with its number and name, not by colour alone.
- **Zoom.** The layout adapts to small screens, and browser zoom is not blocked.
- **Self-assessment.** Each control's choices are grouped and labelled, with a progress indicator. Results can be
  printed or saved as a CSV file. Answers stay in the browser and are not sent anywhere.

## Known limits

- The self-assessment and search need JavaScript. The assessment workbook (Excel) and the controls downloads give the
  same content without it.
- The reference guide PDF is not tagged for screen readers. The same content is on the website and in the CSV and
  JSON downloads.
- The Excel workbooks have not been tested with screen readers.
- The dark theme follows the reader's choice on the site, not the device setting.

## Reporting a barrier

If something on the site or in a download gets in your way, email adrian@adriansaxton.com and say which page or file
it was and what happened. If you are happy for the report to be public, you can open an issue on GitHub instead
(https://github.com/adriansaxton/AACF/issues). You should get a reply within 14 days. The content can also be sent in
another format on request.
