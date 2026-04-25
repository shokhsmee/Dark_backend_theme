# Dark Backend Theme for Odoo 19

A fully standalone backend theme for Odoo 19 Community. Dark navy + industrial orange design with a custom navbar, icon-only sidebar, and a full-screen app grid home menu. All branding is configurable directly from Settings — no code changes required.

---

## Features

- **Dark navy navbar** with orange accent border and custom brand logo
- **Icon-only fixed sidebar** (72px) with active state indicator and hover effects
- **Full-screen home app grid** — 5-column responsive layout with background image
- **Orange primary accent** applied globally: buttons, checkboxes, icons, modals, status bars
- **League Spartan** typography via Google Fonts
- **Bootstrap Icons** integration for app and sidebar icons
- **Configurable branding** — change brand name, icon, and primary color from Settings UI
- **Responsive** — sidebar hides on mobile, grid collapses to 2–3 columns
- No business logic, no models, no menus — pure UI layer

---

## Screenshots

| Home App Grid | Navbar + Sidebar |
|---|---|
| Dark background with 5-column app grid | Fixed 72px navy sidebar with icon-only items |

---

## Installation

### 1. Copy the addon

```bash
cp -r oil_backend_theme /your/odoo/extra-addons/
```

### 2. Restart Odoo

```bash
sudo systemctl restart odoo
```

### 3. Install via Apps menu

Go to **Settings → Apps**, search for **Dark Backend Theme**, and click **Install**.

### 4. Or install via CLI

```bash
python odoo-bin -c odoo.conf -d your_database -i oil_backend_theme --stop-after-init
```

---

## Configuration

After installation, go to **Settings → Dark Backend Theme**:

| Setting | Description | Default |
|---|---|---|
| **Brand Name** | Text shown in the navbar next to the icon | `Oil ERP` |
| **Brand Icon** | Bootstrap icon name (without `bi-` prefix) | `droplet-fill` |
| **Primary Color** | Hex color code for the accent color | `#FF6A00` |

After saving, **reload the page (F5)** to apply changes.

### Icon examples

Browse the full icon list at [icons.getbootstrap.com](https://icons.getbootstrap.com)

| Icon name | Preview description |
|---|---|
| `droplet-fill` | Oil drop (default) |
| `globe` | Globe |
| `fire` | Flame |
| `building` | Building |
| `gear-fill` | Gear |
| `lightning-fill` | Lightning bolt |
| `truck` | Truck |

---

## File Structure

```
oil_backend_theme/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── res_config_settings.py       # Branding config fields
├── views/
│   └── res_config_settings_views.xml # Settings UI section
└── static/
    └── src/
        ├── img/
        │   └── bg/
        │       └── bg.jpg            # Home screen background image
        ├── js/
        │   ├── theme_config_service.js  # Fetches config & applies CSS var at startup
        │   ├── home_menus.js            # OWL component for app grid
        │   └── search_apps.js          # NavBar patch: sidebar & home menu logic
        └── scss/
        │   ├── primary_variables.scss   # Odoo brand color overrides
        │   └── backend_theme.scss       # Full global theme styles
        └── xml/
            ├── nav_bar_panel.xml        # Custom navbar with dynamic brand
            ├── menu_panels.xml          # Back arrow button override
            ├── home_menus.xml           # App grid home screen template
            └── side_bar_panel.xml       # Icon-only sidebar template
```

---

## How It Works

### Theme color

The primary color is stored in `ir.config_parameter` under the key `oil_theme.color`. A lightweight JS service (`theme_config_service.js`) fetches this value via RPC **before** any component renders and sets it as a CSS variable:

```js
document.documentElement.style.setProperty('--oil-primary', color);
```

All SCSS uses `var(--oil-primary)` so the color cascades everywhere instantly on page load.

### Navbar branding

The `NavBar` component is patched via OWL's `patch()` utility. Brand name and icon are read from the `oilThemeConfig` service and rendered reactively. To change the icon, type the Bootstrap icon name (without `bi-`) into the Settings field.

### Sidebar

The sidebar is injected after the navbar element via an `xpath` template extension. It renders all installed apps as icon-only list items. Clicking an app navigates to it and marks it as active with an orange left-border indicator.

### Home app grid

Clicking the back arrow (←) in the navbar hides the sidebar and opens the custom home screen — a full-screen grid of app icons with a background image. Apps with PNG/SVG icons show their image; others fall back to a mapped Bootstrap icon.

---

## Compatibility

| Odoo Version | Status |
|---|---|
| 19.0 Community | Supported |
| 17.0 | Not tested |
| Enterprise | Not tested |

---

## Dependencies

- `web` — Odoo core web module
- `base_setup` — Required for Settings section
- [Bootstrap Icons 1.4.0](https://icons.getbootstrap.com) — loaded via CDN
- [League Spartan](https://fonts.google.com/specimen/League+Spartan) — loaded via Google Fonts

> **Note:** The theme loads Bootstrap Icons and League Spartan from external CDNs. In offline environments, host these locally and update the `@import` URLs in `backend_theme.scss`.

---

## Author

**Shohjahon Obruyev**

---

## License

[LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.html)
