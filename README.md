# Egyptian Courts Dataset — محاكم مصر

An open-source, structured dataset of Egyptian courts with bilingual (Arabic/English) fields. Contains **265 court records** across all governorates and jurisdiction levels.

## Files

| File | Description |
|---|---|
| `egypt_courts_en.json` | English + neutral fields (265 records) |
| `egypt_courts_ar.json` | Arabic + neutral fields (265 records) |
| `egypt_courts_complete.json` | Combined file with all fields |

Every record in `en` and `ar` files shares a matching `uuid` for cross-referencing.

## Schema

### English file (`egypt_courts_en.json`)

| Field | Type | Example |
|---|---|---|
| `uuid` | string | `52100dcf-...` |
| `name_english` | string | `Court of Cassation` |
| `court_type` | string | `cassation` |
| `jurisdiction_level` | string | `national_apex` |
| `governorate` | string | `Cairo` |
| `district` | string | `Downtown Cairo (Wust al-Balad)` |
| `address_english` | string | `26 July Street, ...` |
| `coordinates` | object | `{"lat": 30.0598, "lng": 31.2401}` |
| `phone` | string|null | `+20234955232` |
| `website` | string|null | `https://www.cc.gov.eg` |
| `working_hours` | string | `Sun–Thu 08:30–14:30` |
| `confidence` | string | `high` / `medium` / `low` |
| `notable_notes` | string | `Apex of Egypt's common court hierarchy...` |
| `audit_notes` | string | `Renamed per MOJ restructuring decree...` |

### Arabic file (`egypt_courts_ar.json`)

| Field | Type | Example |
|---|---|---|
| `uuid` | string | `52100dcf-...` |
| `name` | string | `محكمة النقض` |
| `address` | string | `شارع 26 يوليو، ميدان الإسعاف، ...` |
| `court_type_arabic` | string | `نقض` |
| `jurisdiction_level_arabic` | string | `قمة وطنية` |
| `governorate_arabic` | string | `القاهرة` |
| `district_arabic` | string | `وسط البلد، القاهرة` |
| `confidence_arabic` | string | `عالية` / `متوسطة` / `منخفضة` |
| `working_hours_arabic` | string | `الأحد – الخميس 08:30–14:30` |
| `coordinates`, `phone`, `website` | shared | Same as English file |

## Data Coverage

- **265 courts** across all 27 Egyptian governorates
- 10 jurisdiction levels (national apex, appellate, first instance, summary, etc.)
- 12 court types (cassation, constitutional, appellate, first instance, administrative, family, etc.)
- Bilingual: every categorical field has both English and Arabic values
- Geocoded: coordinates for most courts
- Confidence rating: high (257), medium (5), low (3)

## Confidence Rating

| Level | Count | Meaning |
|---|---|---|
| **High** | 257 | Address and details verified from official sources (MOJ website, Official Gazette, verified directories) |
| **Medium** | 5 | Court existence confirmed, address could not be independently verified |
| **Low** | 3 | Court identified through secondary sources only |

## Sources

Data compiled from official Ministry of Justice publications, the Official Gazette (Al-Waqa'i Al-Masriyya), qadaya.net, and news reports.

## License

This dataset is released under the [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/). You are free to share, modify, and use it as long as you attribute the source and share-alike any derived databases.

## Contributing

Found an error or missing court? Open an issue or submit a pull request. Please include your source citation.

## Scripts

| Script | Purpose |
|---|---|
| `count_courts.py` | Print record count and confidence distribution |
